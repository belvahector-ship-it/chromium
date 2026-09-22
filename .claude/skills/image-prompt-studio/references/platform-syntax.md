# Perbedaan Platform

Prompt yang sama memberi hasil berbeda di tiap model. Baca bagian yang relevan
sebelum menyerahkan prompt final ke user, terutama kalau tugasnya EDIT foto orang.

## Daftar isi
- [Ringkasan perbandingan](#ringkasan-perbandingan)
- [Nano Banana / Gemini Image](#nano-banana--gemini-image)
- [ChatGPT / GPT Image](#chatgpt--gpt-image)
- [Prinsip yang berlaku di semua model](#prinsip-yang-berlaku-di-semua-model)
- [Kalau user memakai model lain](#kalau-user-memakai-model-lain)
- [Diagnosis kegagalan umum](#diagnosis-kegagalan-umum)

## Ringkasan perbandingan

| | Nano Banana / Gemini | ChatGPT / GPT Image |
|---|---|---|
| Edit foto asli | Kekuatan utamanya | Bisa, tapi lebih sering menggambar ulang |
| Menjaga kemiripan wajah | Relatif baik | Perlu lock lebih keras |
| Perbaikan bertahap | Sangat baik — paham "sekarang kurangi sedikit" | Terbatas — cenderung memulai ulang |
| Panjang prompt ideal | 50–120 kata | 40–80 kata |
| Gaya penulisan | Instruksi ke retoucher | Instruksi ringkas dan tegas |
| Edit beberapa objek sekaligus | Menangani dengan baik | Lebih baik dipecah |
| Teks di dalam gambar | Cukup baik | Baik |

## Nano Banana / Gemini Image

Model ini paling kuat untuk **mengubah foto yang sudah ada** tanpa kehilangan
orangnya. Perlakukan seperti memberi arahan ke retoucher berpengalaman: sebut apa
yang berubah, sebut apa yang jangan disentuh, dan biarkan ia mengurus caranya.

**Yang bekerja baik:**
- Kalimat lengkap dalam bentuk perintah — *"Replace the background behind me with…"*
- Menyebut lokasi spesifik di foto — *"the harsh shadow across the left side of my face"*
- Meminta beberapa perubahan sekaligus, asal saling berkaitan
- **Iterasi.** Ini kelebihan terbesarnya. Jangan kejar prompt sempurna dalam sekali
  jalan; keluarkan prompt dasar yang bagus, lalu sediakan kalimat lanjutan untuk
  menyetel hasilnya.

**Yang tidak bekerja:**
- Daftar kata kunci (`portrait, 8k, ultra detailed, masterpiece`) — mendorong model
  ke arah estetika generik dan justru memicu "mempercantik"
- Parameter ala Midjourney (`--ar 16:9`, `--v 6`) — diabaikan, kadang malah muncul
  sebagai teks di gambar
- Negasi tanpa alternatif — *"no bad lighting"* tidak berarti apa-apa; sebut cahaya
  seperti apa yang diinginkan

**Pola iterasi yang disarankan.** Selalu sertakan ini saat menyerahkan prompt untuk
Nano Banana — inilah cara memakainya yang benar:

```
Generasi 1 → prompt dasar
Generasi 2 → "Keep everything, but [satu penyesuaian]."
Generasi 3 → "Keep everything, but [satu penyesuaian lagi]."
```

Kalimat *"Keep everything, but…"* penting. Tanpa itu, model sering menafsirkan
permintaan lanjutan sebagai tugas baru dan mengulang dari awal.

**Edit bertahap untuk tugas berat.** Kalau satu prompt harus melakukan koreksi
cahaya + ganti background + color grade sekaligus, pecah jadi tiga generasi. Tiap
generasi yang lebih sederhana memberi model lebih sedikit alasan menyentuh wajah.

## ChatGPT / GPT Image

Unggul untuk **membuat gambar dari nol** dan untuk restyle yang tegas. Saat
mengedit foto orang, ia lebih sering merekonstruksi wajah daripada mengeditnya.

**Yang bekerja baik:**
- Prompt sedang dan padat — 40–80 kata lebih patuh daripada 150 kata
- **Identity lock diletakkan di awal, bukan di akhir.** Ini berbeda dari Nano
  Banana. Kalimat pembuka yang menyatakan wajah tidak boleh berubah jauh lebih
  efektif daripada kalimat penutup yang sama isinya.
- Satu tugas per generasi
- Deskripsi konkret dan bisa dibayangkan, bukan kata sifat abstrak

**Yang tidak bekerja:**
- Daftar larangan yang panjang — setelah sekitar lima larangan, kepatuhannya menurun
  tajam. Pilih yang paling penting saja.
- Meminta perbaikan halus lewat percakapan — biasanya menghasilkan gambar yang
  berbeda sama sekali, bukan versi yang disetel. Untuk menyetel, kirim ulang prompt
  lengkap dengan satu frasa diubah.
- Mengandalkan model mengingat generasi sebelumnya

**Susunan prompt yang disarankan untuk GPT Image saat EDIT:**

```
[LOCK dulu]     Keep the person's face, facial structure, and skin texture
                exactly as in the source photo — this must remain the same
                recognizable person.
[baru AKSI]     Relight the photo as a professional studio headshot with soft
                key light from the left and a clean grey backdrop.
[larangan singkat] No beautification, no skin smoothing, no reshaping.
```

## Prinsip yang berlaku di semua model

**Deskripsikan, jangan beri label.** *"Professional"* adalah label — tiap model
mengartikannya beda. *"Soft key light from the left, clean grey backdrop, chest-up
framing"* adalah deskripsi, dan hasilnya bisa diulang.

**Positif mengalahkan negatif.** Model memahami apa yang harus digambar lebih baik
daripada apa yang harus dihindari. Ubah *"not blurry"* jadi *"sharp focus on the
eyes"*. Pengecualian: larangan seputar identitas memang harus negatif, karena
memang itu satu-satunya cara menyatakannya — dan di situ spesifisitas menggantikan
bentuk positif.

**Yang di depan lebih berbobot.** Taruh hal terpenting di kalimat pertama.

**Satu keputusan per kalimat.** Kalimat yang memuat cahaya, warna, sudut, dan mood
sekaligus akan dijalankan sebagian saja.

**Angka jarang membantu.** *"85mm f/1.4"* kurang andal dibanding *"shallow depth of
field with the background softly blurred"*, kecuali user memang paham fotografi dan
menginginkan istilah itu.

**Jangan sebut merek.** Nama merek kamera atau software hampir tidak berpengaruh
pada hasil, dan mengisi ruang prompt yang lebih berguna untuk deskripsi fisik.

## Kalau user memakai model lain

- **Midjourney** — pakai parameter (`--ar`, `--stylize`, `--sref`) dan merespons
  daftar kata kunci. Skill ini tidak menyetel gaya penulisan untuk Midjourney;
  kalau user memakainya, katakan terus terang bahwa prompt perlu disusun ulang
  dengan konvensi Midjourney, lalu bantu susun berdasarkan isi korpus yang sama.
- **Stable Diffusion / Flux** — mendukung negative prompt terpisah. Pindahkan blok
  larangan dari prompt utama ke kolom negative prompt.
- **Adobe Firefly / Photoshop Generative Fill** — bekerja pada area terseleksi;
  prompt harus mendeskripsikan **isi area itu saja**, bukan keseluruhan foto.

## Diagnosis kegagalan umum

| Gejala | Kemungkinan sebab | Perbaikan |
|---|---|---|
| Model mengabaikan sebagian prompt | Terlalu banyak instruksi | Pecah jadi beberapa generasi |
| Hasil generik, tidak sesuai foto | Prompt terlalu abstrak | Sebut detail nyata yang terlihat di foto |
| Setiap generasi sangat berbeda | Prompt kurang mengikat | Tambah detail konkret pada cahaya, framing, dan warna |
| Gaya masuk tapi wajah berubah | Lock terlalu lemah untuk beratnya restyle | Naikkan tingkat lock, atau kurangi beratnya gaya |
| Parameter muncul jadi teks di gambar | Sintaks Midjourney dipakai di model lain | Hapus semua `--flag` |
| Background bagus, subjek tertempel | Cahaya tidak dicocokkan | Tambah kalimat pencocokan arah cahaya |
| Perbaikan lanjutan malah bikin gambar baru | Tidak ada jangkar konteks | Awali dengan `Keep everything, but…` |
| Hasil terlalu "AI" | Terlalu mulus, terlalu simetris, terlalu tajam | Tambah grain, tekstur kulit asli, dan ketidaksempurnaan cahaya |
