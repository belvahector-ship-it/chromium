'use strict';

const { WebContentsView, shell } = require('electron');

const { CHROME_HEIGHT, NEW_TAB_URL } = require('./config');
const { isLoadableInTab } = require('./url');

let nextTabId = 1;

/**
 * Owns the set of open tabs for one window. Each tab is a WebContentsView that
 * is only attached to the window while it is the active tab, so background
 * tabs never paint over the foreground one.
 */
class TabManager {
  /**
   * @param {import('electron').BaseWindow} window
   * @param {() => void} onChange called whenever the state the UI renders changes
   */
  constructor(window, onChange) {
    this.window = window;
    this.onChange = onChange;
    this.tabs = [];
    this.activeId = null;
  }

  get activeTab() {
    return this.tabs.find((tab) => tab.id === this.activeId) || null;
  }

  find(id) {
    return this.tabs.find((tab) => tab.id === id) || null;
  }

  create(url = NEW_TAB_URL, { active = true, index = this.tabs.length } = {}) {
    const view = new WebContentsView({
      webPreferences: {
        sandbox: true,
        contextIsolation: true,
        nodeIntegration: false,
      },
    });

    const tab = {
      id: nextTabId++,
      view,
      title: 'New Tab',
      url,
      loading: true,
      canGoBack: false,
      canGoForward: false,
    };

    this.tabs.splice(index, 0, tab);
    this.#wire(tab);
    view.webContents.loadURL(url);

    if (active || this.activeId === null) {
      this.select(tab.id);
    } else {
      this.onChange();
    }
    return tab.id;
  }

  close(id) {
    const index = this.tabs.findIndex((tab) => tab.id === id);
    if (index === -1) return;

    const [tab] = this.tabs.splice(index, 1);
    if (this.activeId === id) {
      this.window.contentView.removeChildView(tab.view);
      this.activeId = null;
    }
    tab.view.webContents.close();

    if (this.tabs.length === 0) {
      this.window.close();
      return;
    }
    if (this.activeId === null) {
      // Prefer the tab that slid into the closed tab's slot, else the last one.
      this.select((this.tabs[index] || this.tabs[this.tabs.length - 1]).id);
      return;
    }
    this.onChange();
  }

  select(id) {
    const tab = this.find(id);
    if (!tab || this.activeId === id) return;

    const previous = this.activeTab;
    if (previous) this.window.contentView.removeChildView(previous.view);

    this.activeId = id;
    this.window.contentView.addChildView(tab.view);
    this.layout();
    tab.view.webContents.focus();
    this.onChange();
  }

  /** Resize the active tab to fill the window below the browser chrome. */
  layout() {
    const tab = this.activeTab;
    if (!tab) return;
    const { width, height } = this.window.getContentBounds();
    tab.view.setBounds({
      x: 0,
      y: CHROME_HEIGHT,
      width,
      height: Math.max(0, height - CHROME_HEIGHT),
    });
  }

  /** A plain snapshot of everything the UI needs to draw itself. */
  serialize() {
    const active = this.activeTab;
    return {
      activeId: this.activeId,
      tabs: this.tabs.map((tab) => ({
        id: tab.id,
        title: tab.title,
        url: tab.url,
        loading: tab.loading,
      })),
      canGoBack: active ? active.canGoBack : false,
      canGoForward: active ? active.canGoForward : false,
      loading: active ? active.loading : false,
      url: active ? active.url : '',
    };
  }

  destroy() {
    for (const tab of this.tabs) tab.view.webContents.close();
    this.tabs = [];
    this.activeId = null;
  }

  #wire(tab) {
    const { webContents } = tab.view;

    const refresh = () => {
      const history = webContents.navigationHistory;
      tab.canGoBack = history.canGoBack();
      tab.canGoForward = history.canGoForward();
      tab.url = webContents.getURL() || tab.url;
      this.onChange();
    };

    webContents.on('page-title-updated', (_event, title) => {
      tab.title = title;
      this.onChange();
    });
    webContents.on('did-start-loading', () => {
      tab.loading = true;
      this.onChange();
    });
    webContents.on('did-stop-loading', () => {
      tab.loading = false;
      refresh();
    });
    webContents.on('did-navigate', refresh);
    webContents.on('did-navigate-in-page', refresh);
    webContents.on('did-fail-load', (_event, code, description, failedUrl, isMainFrame) => {
      if (!isMainFrame || code === -3) return; // -3 is a user-initiated abort.
      tab.title = 'Failed to load';
      tab.url = failedUrl || tab.url;
      tab.loading = false;
      this.onChange();
      console.error(`load failed (${code} ${description}): ${failedUrl}`);
    });

    // window.open() and target=_blank become tabs; other schemes go to the OS.
    webContents.setWindowOpenHandler(({ url }) => {
      const index = this.tabs.findIndex((candidate) => candidate.id === tab.id);
      if (isLoadableInTab(url)) {
        this.create(url, { active: true, index: index + 1 });
      } else {
        shell.openExternal(url);
      }
      return { action: 'deny' };
    });
  }
}

module.exports = TabManager;
