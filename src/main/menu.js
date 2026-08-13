'use strict';

const { Menu } = require('electron');

const isMac = process.platform === 'darwin';

/**
 * Accelerators have to live in the application menu rather than in the UI's
 * keydown handler: while a page has focus, key events go to that page's
 * renderer and never reach the browser chrome.
 *
 * @param {() => {window: import('electron').BaseWindow, chrome: import('electron').WebContentsView, tabs: import('./tabs')} | null} getBrowser
 */
function buildMenu(getBrowser) {
  const withTabs = (fn) => () => {
    const browser = getBrowser();
    if (browser) fn(browser);
  };

  const focusAddress = withTabs(({ chrome }) => {
    chrome.webContents.focus();
    chrome.webContents.send('browser:focus-address');
  });

  const template = [
    ...(isMac ? [{ role: 'appMenu' }] : []),
    {
      label: '&File',
      submenu: [
        {
          label: 'New Tab',
          accelerator: 'CmdOrCtrl+T',
          click: withTabs(({ tabs }) => tabs.create()),
        },
        {
          label: 'Close Tab',
          accelerator: 'CmdOrCtrl+W',
          click: withTabs(({ tabs }) => {
            if (tabs.activeId !== null) tabs.close(tabs.activeId);
          }),
        },
        { type: 'separator' },
        isMac ? { role: 'close' } : { role: 'quit' },
      ],
    },
    { role: 'editMenu' },
    {
      label: '&View',
      submenu: [
        {
          label: 'Reload',
          accelerator: 'CmdOrCtrl+R',
          click: withTabs(({ tabs }) => tabs.activeTab?.view.webContents.reload()),
        },
        {
          label: 'Stop',
          accelerator: 'Esc',
          click: withTabs(({ tabs }) => tabs.activeTab?.view.webContents.stop()),
        },
        { type: 'separator' },
        {
          label: 'Back',
          accelerator: isMac ? 'Cmd+Left' : 'Alt+Left',
          click: withTabs(({ tabs }) => {
            const history = tabs.activeTab?.view.webContents.navigationHistory;
            if (history?.canGoBack()) history.goBack();
          }),
        },
        {
          label: 'Forward',
          accelerator: isMac ? 'Cmd+Right' : 'Alt+Right',
          click: withTabs(({ tabs }) => {
            const history = tabs.activeTab?.view.webContents.navigationHistory;
            if (history?.canGoForward()) history.goForward();
          }),
        },
        { type: 'separator' },
        { label: 'Focus Address Bar', accelerator: 'CmdOrCtrl+L', click: focusAddress },
        {
          label: 'Toggle Developer Tools',
          accelerator: isMac ? 'Alt+Cmd+I' : 'Ctrl+Shift+I',
          click: withTabs(({ tabs }) => tabs.activeTab?.view.webContents.toggleDevTools()),
        },
      ],
    },
    { role: 'windowMenu' },
  ];

  Menu.setApplicationMenu(Menu.buildFromTemplate(template));
}

module.exports = { buildMenu };
