'use strict';

const { app } = require('electron');

const TIMEOUT_MS = 30_000;

function waitFor(label, predicate) {
  return new Promise((resolve, reject) => {
    const startedAt = Date.now();
    const tick = () => {
      let value;
      try {
        value = predicate();
      } catch (error) {
        reject(error);
        return;
      }
      if (value) {
        resolve(value);
      } else if (Date.now() - startedAt > TIMEOUT_MS) {
        reject(new Error(`timed out waiting for ${label}`));
      } else {
        setTimeout(tick, 50);
      }
    };
    tick();
  });
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
  console.log(`  ok  ${message}`);
}

/**
 * Drives the real browser window through its core interactions and exits with
 * a non-zero status if any of them regress. Runs headless under xvfb.
 */
async function runSmokeTest({ chrome, tabs }) {
  try {
    await waitFor('browser chrome to load', () => !chrome.webContents.isLoading());

    const firstState = await waitFor('the initial tab to finish loading', () => {
      const state = tabs.serialize();
      return state.tabs.length === 1 && !state.loading ? state : null;
    });
    assert(firstState.tabs.length === 1, 'window opens with exactly one tab');
    assert(firstState.url.startsWith('file:'), 'the initial tab shows the local start page');
    assert(firstState.canGoBack === false, 'a fresh tab cannot navigate back');

    const firstId = firstState.tabs[0].id;
    const secondId = tabs.create('data:text/html,<title>Second</title>second', { active: true });
    await waitFor('the second tab to finish loading', () => !tabs.serialize().loading);
    assert(tabs.serialize().tabs.length === 2, 'opening a tab appends it to the strip');
    assert(tabs.activeId === secondId, 'a newly opened tab becomes active');
    assert(
      tabs.find(secondId).title === 'Second',
      'the tab title follows the loaded page title',
    );

    tabs.select(firstId);
    assert(tabs.activeId === firstId, 'selecting a tab activates it');

    tabs.close(secondId);
    assert(tabs.serialize().tabs.length === 1, 'closing a tab removes it from the strip');
    assert(tabs.activeId === firstId, 'closing a background tab keeps the active tab');

    console.log('smoke test passed');
    app.exit(0);
  } catch (error) {
    console.error(`smoke test failed: ${error.message}`);
    app.exit(1);
  }
}

module.exports = { runSmokeTest };
