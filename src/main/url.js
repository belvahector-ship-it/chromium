'use strict';

const { SEARCH_URL } = require('./config');

// Schemes we are willing to load inside a tab. Anything else (mailto:, tel:,
// custom app handlers) is handed off to the OS instead.
const IN_TAB_SCHEMES = new Set(['http:', 'https:', 'file:', 'about:', 'data:']);

const HOSTNAME_LIKE = /^[^\s/?#]+\.[^\s/?#]{2,}(?:[/?#]|$)/;

/**
 * Turn whatever the user typed in the address bar into something loadable:
 * an explicit URL is kept, a bare hostname gets an https:// prefix, and
 * anything else becomes a search query.
 */
function resolveInput(input) {
  const text = String(input || '').trim();
  if (!text) return null;

  if (/^[a-z][a-z0-9+.-]*:/i.test(text)) {
    try {
      return new URL(text).href;
    } catch {
      // Not a well-formed URL after all — fall through to search.
    }
  }

  if (text === 'localhost' || text.startsWith('localhost:') || HOSTNAME_LIKE.test(text)) {
    try {
      return new URL(`https://${text}`).href;
    } catch {
      // Fall through to search.
    }
  }

  return SEARCH_URL + encodeURIComponent(text);
}

function isLoadableInTab(url) {
  try {
    return IN_TAB_SCHEMES.has(new URL(url).protocol);
  } catch {
    return false;
  }
}

module.exports = { resolveInput, isLoadableInTab };
