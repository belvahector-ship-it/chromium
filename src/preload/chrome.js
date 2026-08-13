'use strict';

const { contextBridge, ipcRenderer } = require('electron');

const send = (channel, ...args) => ipcRenderer.send(channel, ...args);

// The only surface the browser UI gets. No node, no arbitrary IPC.
contextBridge.exposeInMainWorld('browser', {
  ready: () => send('browser:ready'),
  onState: (listener) => {
    ipcRenderer.on('browser:state', (_event, state) => listener(state));
  },
  onFocusAddress: (listener) => {
    ipcRenderer.on('browser:focus-address', () => listener());
  },

  newTab: (url) => send('tab:new', url),
  closeTab: (id) => send('tab:close', id),
  selectTab: (id) => send('tab:select', id),

  go: (input) => send('nav:go', input),
  back: () => send('nav:back'),
  forward: () => send('nav:forward'),
  reload: () => send('nav:reload'),
  stop: () => send('nav:stop'),
});
