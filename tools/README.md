# tools/

Skrip pembangkit katalog HTML.

- `extract.py` — membaca tabel & blockquote dari
  `.claude/skills/image-prompt-studio/references/*.md` lalu menulis `corpus.json`
- `build.py` — menyuntikkan `corpus.json` ke template dan menghasilkan
  `dist/katalog-prompt.html`

Jalankan ulang keduanya setiap kali korpus di `references/` berubah, supaya
katalog dan skill tidak pernah berbeda isi.
