---
name: image-prompt-studio
description: Bikin dan sempurnakan prompt untuk edit maupun generate foto di Nano Banana (Gemini Image), ChatGPT/GPT Image, dan model gambar lain — berisi korpus 50 kode sudut kamera, pustaka lighting, efek visual, film emulation, dan identity lock yang menjaga wajah tetap sama persis. Pakai skill ini setiap kali user menyinggung edit foto, prompt gambar, AI photo editing, headshot profesional, foto ala DSLR, golden hour, ganti background, perbaiki pencahayaan, bokeh, atau angle kamera — termasuk kalau mereka cuma bilang "bikin fotoku kelihatan profesional", "prompt buat editin foto ini", "enhance foto ini", "mau hasil kayak studio", "bikin prompt nano banana", atau sekadar melampirkan foto dan minta diperbagus. Trigger juga untuk "write me a prompt to retouch this photo", "make this look cinematic", dan "what prompt gives me a professional headshot". Jangan mengarang prompt gambar dari hafalan — buka skill ini dulu supaya identity lock dan istilah yang dipakai memang dikenali model.
license: Dibuat untuk penggunaan pribadi rrahma154. Bebas dimodifikasi.
---

# Image Prompt Studio

Pabrik prompt untuk foto. Tugasnya mengubah permintaan sehari-hari yang kabur
("bikin fotoku bagusan dong") menjadi prompt yang presisi, bisa diulang, dan —
paling penting — **tidak mengubah orang di dalam foto menjadi orang lain**.

Teks prompt selalu ditulis **bahasa Inggris** karena model gambar jauh lebih
akurat menafsirkannya. Semua penjelasan, label, dan percakapan ke user pakai
**bahasa Indonesia**.

## Kenapa identity lock adalah inti skill ini

Kegagalan paling umum pada editing foto dengan AI bukan hasil yang jelek —
tapi hasil yang bagus untuk **wajah yang salah**. Model punya bias kuat ke arah
"mempercantik": menirus kan rahang, memutihkan kulit, memuluskan pori,
membesarkan mata, menghapus tahi lalat. Hasilnya orang asing yang mirip.

Semua prompt bagus di korpus ini punya pola yang sama: satu kalimat menyatakan
perubahan yang diinginkan, lalu satu kalimat lagi mengunci apa yang **tidak boleh**
berubah. Kalimat kedua itu yang biasanya dilupakan orang. Jangan pernah keluarkan
prompt edit foto orang tanpa kalimat kedua.

## Alur kerja

**1. Pahami dulu: EDIT atau GENERATE?**

- **EDIT** — ada foto sumber yang mau diubah. Identity lock wajib. Ini kasus
  mayoritas.
- **GENERATE** — bikin gambar dari nol, tidak ada orang nyata yang dijaga.
  Identity lock tidak relevan; fokus ke deskripsi subjek, angle, lighting, gaya.

Ada satu kasus di antara keduanya yang butuh penanganan tersendiri: **mengubah
sudut kamera pada foto yang sudah ada.** Ini EDIT, tapi memaksa model mengarang
permukaan yang tidak pernah terekam, sehingga identity lock saja tidak cukup.
Langsung buka `references/angle-change.md` begitu permintaannya menyentuh ini.

**2. Kalau ada fotonya, lihat dulu.** Kalau user melampirkan foto, perhatikan
masalah nyatanya sebelum menulis apa pun — backlight parah, warna kulit menguning
karena lampu ruangan, background berantakan, noise tinggi, blur gerakan, atau
komposisi terpotong. Prompt yang menyebut masalah spesifik ("recover the crushed
shadows on the left side of the face") jauh lebih efektif daripada prompt umum
("improve the lighting"). Kalau fotonya tidak dilampirkan, tanya kondisi fotonya
atau tawarkan preset yang paling mendekati.

**3. Rakit prompt pakai rumus enam blok.** Lihat bagian *Rumus prompt* di bawah.

**4. Sesuaikan dengan platform tujuan.** Nano Banana dan GPT Image berperilaku
berbeda, terutama soal seberapa patuh mereka pada perintah "jangan ubah wajah".
Baca `references/platform-syntax.md` sebelum menyerahkan prompt final.

**5. Serahkan dalam format yang gampang dipakai.** Lihat *Format output* di bawah.

## Rumus prompt

Enam blok, urutannya penting — model memberi bobot lebih besar pada yang di depan.

```
[1 AKSI]  apa yang berubah, satu kalimat, kata kerja di depan
[2 LOCK]  apa yang wajib tetap sama persis          ← lewati ini dan wajahnya berubah
[3 KAMERA] sudut, jarak, lensa                      ← references/camera-codes.md
[4 CAHAYA] arah, kualitas, suasana                  ← references/lighting.md
[5 RASA]  efek optik, grain, color grade            ← references/visual-effects.md
[6 LARANGAN] yang eksplisit dilarang
```

Tidak semua blok selalu dipakai. Untuk permintaan sederhana, blok 1 + 2 + 6 sudah
cukup dan justru lebih akurat — prompt pendek yang tegas mengalahkan prompt panjang
yang bertele-tele. Tambahkan blok 3–5 saat user memang menginginkan gaya tertentu.

**Contoh perakitan:**

> `[1]` Replace the cluttered background behind me with a seamless neutral studio
> backdrop in soft warm grey. `[2]` Keep my face, hair, glasses, clothing, pose, and
> the lighting falling on me exactly as they are. `[3]` Maintain the original
> chest-level, eye-level framing. `[4]` Match the new backdrop's light direction to
> the existing key light coming from my left. `[5]` Add a gentle falloff so the
> backdrop is slightly darker at the edges. `[6]` Do not beautify, reshape, or smooth
> anything. Render the hair edge naturally, with no hard cutout halo.

## Peta referensi

Buka file yang relevan saja — jangan baca semuanya sekaligus.

| File | Isi | Buka saat |
|---|---|---|
| `references/identity-lock.md` | Kalimat pengunci identitas, daftar larangan, kapan lock dilonggarkan | **Setiap tugas EDIT foto orang** |
| `references/photo-transform.md` | 6 prompt inti (DSLR, editorial, golden hour, headshot, koreksi cahaya, background) + 18 preset turunan | User minta transformasi foto jadi gaya tertentu |
| `references/camera-codes.md` | 50 kode sudut & framing, dikelompokkan 5 kategori, plus terjemahan tiap kode jadi kalimat penuh | Butuh sudut, jarak, atau perspektif tertentu |
| `references/angle-change.md` | Cara mengubah sudut kamera pada foto yang sudah ada tanpa kehilangan kemiripan: turntable sheet, fusi multi-referensi, rotasi bertahap, dan batas nyatanya | **User minta ubah angle tapi subjek harus tetap sama** |
| `references/lighting.md` | Pola cahaya potret, arah, kualitas, setup studio, cahaya alami, cahaya berwarna, mood sinematik | Masalah atau keinginannya soal cahaya |
| `references/visual-effects.md` | Optik lensa, bokeh, flare, motion, tekstur film, color grading, film stock, atmosfer | User mau "rasa" atau gaya visual tertentu |
| `references/platform-syntax.md` | Perbedaan perilaku Nano Banana vs GPT Image, panjang prompt ideal, cara iterasi, kenapa sebuah prompt gagal | **Sebelum menyerahkan prompt final** |

## Aturan singkat per platform

Ringkasannya saja; detail dan penanganan kegagalan ada di `platform-syntax.md`.

- **Nano Banana / Gemini Image** — paling kuat untuk edit foto asli. Pahami
  instruksi percakapan dan bisa diperbaiki bertahap ("sekarang turunkan sedikit
  kontrasnya"). Tulis prompt sebagai instruksi ke seorang retoucher, bukan sebagai
  daftar kata kunci.
- **ChatGPT / GPT Image** — bagus untuk generate dan restyle, tapi lebih agresif
  mengubah wajah saat mengedit. Identity lock harus lebih keras dan diletakkan di
  awal, bukan di akhir. Prompt sedang (40–80 kata) lebih patuh daripada prompt panjang.
- Untuk keduanya: **hindari daftar kata kunci ala Midjourney** (`portrait, 8k,
  ultra detailed, masterpiece`). Keduanya dilatih untuk kalimat natural, dan kata
  kunci semacam itu justru mendorong model ke arah "mempercantik" yang kita hindari.

## Format output

Serahkan seperti ini — user biasanya menyalinnya langsung ke aplikasi lain, jadi
teks prompt harus berdiri sendiri tanpa perlu diedit:

```
**[Nama preset yang dipakai]** — untuk [platform]

> teks prompt bahasa Inggris, satu blok, siap salin

**Kenapa begini:** 1–2 kalimat menjelaskan pilihan kunci —
misalnya kenapa memilih chest-level daripada eye-level.

**Kalau hasilnya meleset:**
- [gejala] → [kalimat perbaikan yang ditambahkan ke prompt]
- [gejala] → [kalimat perbaikan]
```

Bagian "kalau hasilnya meleset" jangan dilewati. Generasi pertama jarang langsung
pas, dan user yang tidak tahu cara memperbaiki akan mengulang prompt yang sama
berkali-kali sambil berharap hasil berbeda. Dua sampai tiga jalur perbaikan sudah
cukup — pilih kegagalan yang paling mungkin terjadi pada prompt tersebut.

Kalau user minta beberapa variasi, beri **3 opsi yang benar-benar berbeda arah**
(misalnya: natural, editorial, sinematik), bukan tiga parafrase dari prompt yang sama.

## Batasan

Skill ini untuk memperbaiki dan menata ulang foto, bukan untuk memalsukan realita.

- Jangan susun prompt yang membuat orang nyata tampak melakukan sesuatu yang tidak
  mereka lakukan, berada di tempat yang tidak mereka datangi, atau mengucapkan hal
  yang tidak mereka ucapkan — ini berlaku untuk tokoh publik maupun orang biasa.
- Jangan bantu membuka pakaian, menyeksualisasi, atau membuat citra intim dari foto
  siapa pun.
- Jangan buat prompt untuk memalsukan dokumen identitas, bukti, tanda tangan, atau
  stempel resmi.
- Kalau user minta memakai wajah orang lain di foto mereka, pastikan dulu itu memang
  orang yang mengizinkan.

Kalau permintaannya menabrak salah satu batas ini, katakan singkat dalam satu kalimat
lalu tawarkan versi yang bisa dikerjakan — biasanya ada bentuk yang sah dari keinginan
yang sama.
