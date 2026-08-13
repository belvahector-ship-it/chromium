'use strict';

const path = require('node:path');
const { pathToFileURL } = require('node:url');

const RENDERER_DIR = path.join(__dirname, '..', 'renderer');

module.exports = {
  // Height of the browser chrome (tab strip + toolbar) in CSS pixels.
  // The renderer stylesheet must stay in sync with this value.
  CHROME_HEIGHT: 80,

  WINDOW_DEFAULTS: {
    width: 1280,
    height: 820,
    minWidth: 520,
    minHeight: 360,
  },

  CHROME_URL: pathToFileURL(path.join(RENDERER_DIR, 'chrome.html')).href,
  NEW_TAB_URL: pathToFileURL(path.join(RENDERER_DIR, 'newtab.html')).href,

  CHROME_PRELOAD: path.join(__dirname, '..', 'preload', 'chrome.js'),

  SEARCH_URL: 'https://duckduckgo.com/?q=',
};
