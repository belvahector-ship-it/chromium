# chromium

A minimal tabbed web browser built on Electron.

## Run it

```sh
npm install
npm start
```

`npm install` downloads the Electron runtime (which bundles Chromium), so the
first install needs network access and a few hundred MB of disk.

## Features

- Tab strip: open, switch, and close tabs; middle-click a tab to close it
- Address bar that accepts a URL, a bare hostname, or a search query
- Back / forward / reload, with reload turning into stop while a page loads
- `window.open()` and `target="_blank"` open as new tabs; `mailto:` and other
  non-web schemes are handed to the OS
- Keyboard shortcuts: `Ctrl+T` new tab, `Ctrl+W` close tab, `Ctrl+L` focus the
  address bar, `Ctrl+R` reload, `Esc` stop, `Alt+←` / `Alt+→` navigate history
  (`Cmd` in place of `Ctrl`/`Alt` on macOS)
- Light and dark UI, following the system theme

## Layout

```
src/
  main/       Electron main process
    main.js     app lifecycle, window assembly, IPC entry points
    tabs.js     TabManager — owns the tab list and each tab's WebContentsView
    menu.js     application menu, which is where the accelerators live
    url.js      address-bar input → URL or search
    config.js   shared constants (chrome height, file URLs, search engine)
    smoke.js    the scripted run behind `npm test`
  preload/
    chrome.js   contextBridge API exposed to the browser UI
  renderer/
    chrome.html/.css/.js   tab strip and toolbar
    newtab.html            local start page
```

Each tab is a `WebContentsView` owned by the main process and attached to the
window only while it is active. The browser UI is a separate `WebContentsView`
pinned to the top 80px; it never touches Node and talks to the main process
through the narrow preload bridge. Page content runs sandboxed with context
isolation on and node integration off.

Keyboard accelerators are registered on the application menu rather than in the
UI's `keydown` handler, because while a page has focus its renderer receives
key events and the browser chrome never sees them.

## Tests

```sh
npm test
```

Launches the real app under `xvfb` and drives it through opening, switching,
and closing tabs, asserting the observable state after each step. Exits
non-zero on failure.

When running as root (containers, most CI images) Chromium refuses to start
without an extra flag — use `npm test -- --no-sandbox` there.
