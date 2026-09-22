# Mengubah Sudut Kamera Tanpa Kehilangan Orangnya

Permintaan tersulit di seluruh korpus: *"ubah angle-nya, tapi orangnya harus
100% sama persis."*

## Daftar isi
- [Kenapa 100% tidak mungkin, dan apa yang mungkin](#kenapa-100-tidak-mungkin-dan-apa-yang-mungkin)
- [Lima pengungkit, urut dari yang paling berpengaruh](#lima-pengungkit-urut-dari-yang-paling-berpengaruh)
- [Prompt A — Turntable sheet](#prompt-a--turntable-sheet)
- [Prompt B — Fusi multi-referensi](#prompt-b--fusi-multi-referensi)
- [Prompt C — Rotasi bertahap](#prompt-c--rotasi-bertahap)
- [Prompt D — Satu langkah aman](#prompt-d--satu-langkah-aman)
- [Alur kerja gabungan](#alur-kerja-gabungan)
- [Yang tidak bisa diselamatkan prompt apa pun](#yang-tidak-bisa-diselamatkan-prompt-apa-pun)
- [Diagnosis](#diagnosis)

## Kenapa 100% tidak mungkin, dan apa yang mungkin

Foto adalah proyeksi dua dimensi. Saat memutar kamera, sebagian permukaan yang
diminta muncul **tidak pernah terekam di foto aslinya** — sisi wajah yang jauh,
bentuk telinga, garis rahang dari samping, belahan rambut di sisi seberang. Model
tidak bisa mengambilnya dari mana pun, jadi ia menyusunnya dari kemungkinan
statistik. Itu menebak, bukan mengedit.

Jadi kalau ada yang menjanjikan satu prompt ajaib yang menjaga subjek 100% sama
sambil memutar sudut, yang sebenarnya terjadi adalah salah satu dari ini: sudutnya
hanya bergeser sedikit, atau hasilnya sebenarnya tidak seidentik yang diklaim.

Yang bisa dicapai jauh lebih berguna daripada kedengarannya: **kemiripan yang
bertahan pada pandangan orang yang mengenal subjeknya.** Teknik di bawah ini
memindahkan hasil dari "mirip-mirip" ke "ini memang dia" — bukan lewat satu
kalimat sakti, melainkan dengan mengurangi seberapa banyak yang harus ditebak model.

Itu prinsip tunggal yang mendasari semua teknik di halaman ini: **jangan buat
prompt lebih kuat, buat tebakannya lebih kecil.**

## Lima pengungkit, urut dari yang paling berpengaruh

**1. Beri lebih dari satu foto.** Ini pengungkit terbesar, dan bedanya bukan
sedikit. Dengan 3–4 foto dari sudut berbeda, model tidak lagi mengarang sisi wajah
yang tak terlihat — ia membacanya. Tugasnya berubah dari mengarang jadi
menyambungkan. Nano Banana menerima beberapa gambar masukan sekaligus; gunakan itu.
Kalau user hanya punya satu foto, sarankan mencari 2–3 foto lama dari sudut lain
sebelum apa pun yang lain — itu lebih berpengaruh daripada seluruh sisa halaman ini.

**2. Minta semua sudut dalam satu gambar.** Model menjaga konsistensi **di dalam**
satu gambar jauh lebih baik daripada **antar** generasi terpisah. Jadi minta satu
lembar berisi 3–4 panel sudut berbeda, lalu potong panel yang dibutuhkan. Ini
trik yang paling sering terlewat, dan sering kali jadi selisih antara gagal dan
berhasil.

**3. Putar sedikit-sedikit.** 15–25 derajat per langkah, tiap hasil jadi masukan
langkah berikutnya. Enam langkah 15 derajat mempertahankan kemiripan jauh lebih
baik daripada satu lompatan 90 derajat, walau totalnya sama.

**4. Sebut ini gerakan kamera, bukan penggambaran ulang.** *"Kamera bergeser
mengelilingi orangnya; orangnya tidak bergerak dan tidak digambar ulang"* memicu
perilaku yang berbeda dari *"buatkan tampak samping"*. Kalimat pertama membingkai
tugasnya sebagai perpindahan titik pandang; kalimat kedua sebagai pembuatan gambar
baru. Model memperlakukan keduanya berbeda.

**5. Bekukan segalanya selain sudut.** Momen yang sama, pakaian yang sama dengan
lipatan yang sama, ekspresi yang sama, cahaya yang tetap di tempatnya di ruangan.
Setiap hal yang dibiarkan bebas berubah memberi model izin untuk ikut mengubah
wajah.

## Prompt A — Turntable sheet

Untuk **satu foto sumber**. Ini yang paling mendekati "prompt powerful" yang
dimaksud orang — kekuatannya bukan pada kata-katanya, tapi pada meminta semua
sudut sekaligus sehingga model wajib konsisten di dalam satu kanvas.

> Using the attached photo as the single source of truth for this person's
> identity, produce one image containing four views of the exact same person in a
> single row against the same plain background: front view, 45-degree three-quarter
> view, 90-degree profile, and rear three-quarter view. This is one person
> photographed by a camera moving around them in one continuous take — not four
> different people, and not four separate photo sessions. Facial geometry, head
> proportions, jawline width, nose shape, eye shape and spacing, hairstyle and hair
> part, skin tone, skin texture with visible pores, every mole and freckle, facial
> hair, glasses, clothing, and body proportions must be identical across all four
> views. Only the viewing angle changes. Keep the lighting fixed in world space, so
> the light stays where it is while the camera moves around the subject. Do not
> beautify, slim, or smooth anything in any view.

Lalu potong panel yang dibutuhkan dan perbesar. Kalau butuh sudut yang tidak ada
di lembar itu, ganti daftar empat panelnya.

## Prompt B — Fusi multi-referensi

Untuk **2–4 foto sumber**. Kalau user punya ini, inilah yang dipakai — hasilnya
di kelas yang berbeda dari Prompt A.

> The attached images are the same person photographed from different angles. Use
> all of them together to build one complete understanding of this person's head,
> face, and build. Now render this same person at a 45-degree three-quarter angle.
> Every feature must match what the reference images actually show rather than
> anything invented: the exact facial geometry and proportions, the nose shape as
> seen in the profile reference, the ear shape, the hairline and hair part, the skin
> tone and texture, and all moles and marks. Where a detail is visible in any
> reference image, take it from that reference. Where a detail is visible in none of
> them, reconstruct it conservatively and keep it understated. Use the clothing and
> lighting from the first image. Do not beautify or alter any feature.

Kalimat *"where a detail is visible in none of them, reconstruct it conservatively
and keep it understated"* penting: tanpa itu, model mengisi bagian yang tidak
diketahui dengan tebakan yang mencolok dan justru menarik perhatian.

## Prompt C — Rotasi bertahap

Untuk perubahan sudut besar. Jalankan berulang, tiap hasil jadi masukan berikutnya.

> Rotate the camera 20 degrees to the right around this person, as if the
> photographer took one step sideways. The person does not move, does not change
> expression, and is not redrawn — only the camera position changes. Keep the
> identical face, the identical hairstyle and hair part, the identical clothing with
> the same folds, and the identical lighting fixed in the room. This is the same
> instant in time seen from a slightly different position. No beautification, no
> reshaping, no smoothing.

Perhatikan pada tiap langkah: begitu kemiripan mulai luntur, **berhenti dan mundur
satu langkah**. Kesalahan menumpuk, dan langkah kesembilan mewarisi setiap
penyimpangan dari delapan langkah sebelumnya. Lebih baik berhenti di 60 derajat
yang masih dia, daripada sampai 90 derajat yang bukan dia lagi.

## Prompt D — Satu langkah aman

Untuk kebutuhan sehari-hari: menggeser sudut secukupnya agar foto terasa berbeda,
tanpa mempertaruhkan kemiripan. Ini yang dipakai kalau user tidak menyebut sudut
tertentu.

> Reposition the camera to a three-quarter angle, about 30 degrees to the left of
> the current view. This is the same photograph taken from a slightly different
> camera position at the same moment — the person is not re-posed and not redrawn.
> Preserve exactly: facial structure and proportions, jawline width, nose shape, eye
> shape and spacing, hairline and hair part, skin tone and texture, every mole and
> freckle, the glasses, and the clothing with the same fabric and folds. Keep the
> light source fixed where it is in the room, so the shadows fall differently only
> because the camera moved. Do not beautify, slim, or smooth anything.

**30 derajat adalah titik manis.** Cukup untuk mengubah karakter foto, masih dalam
jangkauan yang bisa disimpulkan model dari satu gambar. Di bawah 20 derajat
perubahannya nyaris tak terasa; di atas 45 derajat dari satu foto, kemiripan mulai
runtuh dengan cepat.

## Alur kerja gabungan

Inilah jawaban sebenarnya untuk "prompt powerful" — sebuah alur, bukan satu kalimat:

1. **Kumpulkan foto.** Tanya apakah ada 2–3 foto lain dari sudut berbeda. Kalau
   ada, lompat ke Prompt B dan selesai — sisanya tidak perlu.
2. **Kalau hanya satu foto**, jalankan Prompt A untuk membuat turntable sheet.
3. **Potong panel** yang paling mendekati sudut yang diinginkan.
4. **Umpankan balik panel itu** bersama foto asli sebagai dua referensi, lalu
   jalankan Prompt B. Sekarang model punya dua sudut untuk dibaca, bukan satu.
5. **Perbaiki dengan edit kecil** — cahaya, background, grading — satu per satu,
   jangan sekaligus.
6. **Verifikasi jujur.** Tempatkan hasil bersebelahan dengan foto asli dan
   perhatikan jarak antar mata, lebar rahang, garis rambut, dan bentuk telinga.
   Kalau salah satunya bergeser, itu bukan sudut baru dari orang yang sama.

Langkah 4 adalah yang paling sering dilewati dan paling besar hasilnya: ia mengubah
masalah satu-foto menjadi masalah multi-referensi, memakai output model sendiri
sebagai referensi tambahan.

## Yang tidak bisa diselamatkan prompt apa pun

Bersikap terus terang soal ini ke user — lebih baik daripada mereka mengulang
puluhan generasi mengejar sesuatu yang memang tidak ada di datanya.

| Diminta | Tersedia di foto depan? | Hasil realistis |
|---|---|---|
| Sudut 15–30° | Sebagian besar tersimpulkan | Sangat baik |
| Tiga perempat 45° | Sebagian tersimpulkan | Baik, biasanya meyakinkan |
| Profil penuh 90° | Bentuk hidung & rahang dari samping tidak ada | Masuk akal, tapi jarang tepat |
| Tampak belakang | Belahan rambut & mahkota tidak ada | Murni karangan |
| Bentuk telinga | Tertutup rambut pada kebanyakan foto | Karangan |
| Gigi yang tak terlihat | Tidak ada | Karangan |
| Tahi lalat di sisi jauh | Tidak ada | Tidak akan muncul, atau muncul di tempat salah |

Kalau tujuan user adalah foto identitas, lamaran kerja, atau apa pun yang perlu
akurat — sudut baru hasil generasi bukan jalannya. Sarankan memotret ulang. Satu
menit dengan kamera HP mengalahkan satu jam prompt.

## Diagnosis

| Gejala | Perbaikan |
|---|---|
| Wajah berubah begitu sudut bergerak | Kurangi derajatnya; pecah jadi langkah 15–20° |
| Panel-panel di turntable sheet tidak seperti orang yang sama | Tambahkan `not four different people` dan `one continuous take`; kurangi jadi 3 panel |
| Model malah menghasilkan foto depan lagi | Sebut derajat dan arahnya eksplisit, bukan nama sudut saja |
| Pakaian berubah ikut sudut | Tambah `identical clothing with the same folds and the same fabric` |
| Cahaya ikut berputar bersama kamera | Tambah `keep the lighting fixed in world space while the camera moves` |
| Hasil bagus tapi terasa "dibersihkan" | Tambah larangan tekstur kulit; model mulus saat merekonstruksi |
| Telinga atau garis rambut terasa salah | Memang tidak ada di sumbernya — butuh foto referensi tambahan |
| Makin banyak langkah makin melenceng | Mundur ke langkah terakhir yang masih mirip dan berhenti di situ |
