# Cara Memasang Skill Ini

Skill ini bisa dipasang di tiga tempat. Pilih sesuai kebutuhan.

## 1. Akun claude.ai — permanen, ikut ke semua sesi (disarankan)

Ini satu-satunya cara agar skill tersimpan di akun dan otomatis tersedia di
Claude Code web, aplikasi desktop, maupun claude.ai.

1. Unduh `dist/image-prompt-studio.zip` dari repo ini
2. Buka **claude.ai → Settings → Capabilities → Skills**
3. Klik **Upload skill**, pilih file `.zip` tadi
4. Pastikan toggle-nya aktif

Langkah ini harus dilakukan manual — Claude tidak punya akses tulis ke
pengaturan akun.

## 2. Claude Code lokal — per mesin

```bash
cp -r .claude/skills/image-prompt-studio ~/.claude/skills/
```

Berlaku untuk semua proyek di mesin tersebut. Catatan: di sesi Claude Code on
the web, container bersifat sementara, jadi salinan ini hilang saat sesi
berakhir — gunakan cara 1 untuk penyimpanan permanen.

## 3. Per proyek — ikut repo

Sudah terpasang di repo ini pada `.claude/skills/image-prompt-studio/`.
Otomatis aktif untuk siapa pun yang membuka repo ini dengan Claude Code.

## Memastikan skill aktif

Ketik `/` di Claude Code dan cari `image-prompt-studio`, atau langsung minta
sesuatu seperti "bikin prompt buat editin foto ini jadi headshot profesional" —
skill akan terpanggil sendiri.
