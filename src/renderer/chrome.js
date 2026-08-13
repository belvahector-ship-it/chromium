'use strict';

const tabsEl = document.getElementById('tabs');
const addressEl = document.getElementById('address');
const addressForm = document.getElementById('address-form');
const backEl = document.getElementById('back');
const forwardEl = document.getElementById('forward');
const reloadEl = document.getElementById('reload');
const newTabEl = document.getElementById('new-tab');

const START_PAGE = 'newtab.html';

let state = { tabs: [], activeId: null, url: '', loading: false, canGoBack: false, canGoForward: false };
let addressEdited = false;

/** The start page is an implementation detail — show an empty address bar. */
function displayUrl(url) {
  return !url || url.endsWith(START_PAGE) ? '' : url;
}

function renderTabs() {
  tabsEl.replaceChildren(
    ...state.tabs.map((tab) => {
      const el = document.createElement('div');
      el.className = tab.id === state.activeId ? 'tab active' : 'tab';
      el.title = tab.title;
      el.addEventListener('mousedown', (event) => {
        if (event.button === 1) {
          browser.closeTab(tab.id); // Middle-click closes, as everywhere else.
        } else if (event.button === 0) {
          browser.selectTab(tab.id);
        }
      });

      if (tab.loading) {
        const spinner = document.createElement('div');
        spinner.className = 'spinner';
        el.append(spinner);
      }

      const title = document.createElement('span');
      title.className = 'tab-title';
      title.textContent = tab.title || 'Untitled';
      el.append(title);

      const close = document.createElement('button');
      close.className = 'tab-close';
      close.textContent = '×';
      close.title = 'Close tab';
      close.setAttribute('aria-label', `Close ${tab.title || 'tab'}`);
      close.addEventListener('mousedown', (event) => event.stopPropagation());
      close.addEventListener('click', (event) => {
        event.stopPropagation();
        browser.closeTab(tab.id);
      });
      el.append(close);

      return el;
    }),
  );
}

function render() {
  renderTabs();
  backEl.disabled = !state.canGoBack;
  forwardEl.disabled = !state.canGoForward;
  reloadEl.title = state.loading ? 'Stop (Esc)' : 'Reload (Ctrl+R)';
  document.body.classList.toggle('loading', state.loading);

  // Never overwrite a URL the user is in the middle of typing.
  if (document.activeElement !== addressEl || !addressEdited) {
    addressEl.value = displayUrl(state.url);
    addressEdited = false;
  }
}

browser.onState((next) => {
  state = next;
  render();
});

addressForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const value = addressEl.value.trim();
  if (!value) return;
  addressEdited = false;
  addressEl.blur();
  browser.go(value);
});

addressEl.addEventListener('input', () => {
  addressEdited = true;
});
addressEl.addEventListener('focus', () => addressEl.select());
addressEl.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  addressEdited = false;
  addressEl.value = displayUrl(state.url);
  addressEl.blur();
});

newTabEl.addEventListener('click', () => browser.newTab());
backEl.addEventListener('click', () => browser.back());
forwardEl.addEventListener('click', () => browser.forward());
reloadEl.addEventListener('click', () => (state.loading ? browser.stop() : browser.reload()));

browser.onFocusAddress(() => {
  addressEl.focus();
  addressEl.select();
});

browser.ready();
