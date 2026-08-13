'use strict';

const { app, BaseWindow, WebContentsView, ipcMain, shell } = require('electron');

const {
  CHROME_HEIGHT,
  CHROME_PRELOAD,
  CHROME_URL,
  NEW_TAB_URL,
  WINDOW_DEFAULTS,
} = require('./config');
const TabManager = require('./tabs');
const { buildMenu } = require('./menu');
const { resolveInput, isLoadableInTab } = require('./url');
const { runSmokeTest } = require('./smoke');

const SMOKE_TEST = process.argv.includes('--smoke-test');

/** @type {{window: BaseWindow, chrome: WebContentsView, tabs: TabManager} | null} */
let browser = null;

function createBrowserWindow() {
  const window = new BaseWindow({ ...WINDOW_DEFAULTS, title: 'chromium' });

  const chrome = new WebContentsView({
    webPreferences: {
      preload: CHROME_PRELOAD,
      sandbox: true,
      contextIsolation: true,
      nodeIntegration: false,
    },
  });
  window.contentView.addChildView(chrome);

  const tabs = new TabManager(window, () => {
    if (chrome.webContents.isDestroyed()) return;
    chrome.webContents.send('browser:state', tabs.serialize());
  });

  const layout = () => {
    const { width } = window.getContentBounds();
    chrome.setBounds({ x: 0, y: 0, width, height: CHROME_HEIGHT });
    tabs.layout();
  };

  window.on('resize', layout);
  window.on('closed', () => {
    tabs.destroy();
    browser = null;
  });

  // The UI asks for a state push once its listeners are attached.
  chrome.webContents.on('did-finish-load', layout);
  chrome.webContents.loadURL(CHROME_URL);

  browser = { window, chrome, tabs };
  tabs.create(NEW_TAB_URL);
  layout();
  return browser;
}

/** Register an IPC listener that only accepts messages from the chrome UI. */
function onChromeMessage(channel, handler) {
  ipcMain.on(channel, (event, ...args) => {
    if (!browser || event.sender !== browser.chrome.webContents) return;
    handler(browser, ...args);
  });
}

onChromeMessage('browser:ready', ({ tabs }) => tabs.onChange());
onChromeMessage('tab:new', ({ tabs }, url) => tabs.create(url || NEW_TAB_URL));
onChromeMessage('tab:close', ({ tabs }, id) => tabs.close(id));
onChromeMessage('tab:select', ({ tabs }, id) => tabs.select(id));

onChromeMessage('nav:go', ({ tabs }, input) => {
  const tab = tabs.activeTab;
  const url = resolveInput(input);
  if (!tab || !url) return;
  if (isLoadableInTab(url)) {
    tab.view.webContents.loadURL(url);
  } else {
    shell.openExternal(url);
  }
});

onChromeMessage('nav:back', ({ tabs }) => {
  const history = tabs.activeTab?.view.webContents.navigationHistory;
  if (history?.canGoBack()) history.goBack();
});

onChromeMessage('nav:forward', ({ tabs }) => {
  const history = tabs.activeTab?.view.webContents.navigationHistory;
  if (history?.canGoForward()) history.goForward();
});

onChromeMessage('nav:reload', ({ tabs }) => tabs.activeTab?.view.webContents.reload());
onChromeMessage('nav:stop', ({ tabs }) => tabs.activeTab?.view.webContents.stop());

app.whenReady().then(() => {
  buildMenu(() => browser);
  const instance = createBrowserWindow();
  if (SMOKE_TEST) runSmokeTest(instance);

  app.on('activate', () => {
    if (!browser) createBrowserWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin' || SMOKE_TEST) app.quit();
});
