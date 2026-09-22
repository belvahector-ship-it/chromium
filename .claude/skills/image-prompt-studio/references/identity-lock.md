# Identity Lock — menjaga orangnya tetap orang yang sama

Referensi ini dipakai pada **setiap tugas EDIT foto yang ada manusianya.**
Isinya kalimat siap pakai untuk blok `[2 LOCK]` dan `[6 LARANGAN]` dari rumus prompt.

## Daftar isi
- [Kenapa model mengubah wajah](#kenapa-model-mengubah-wajah)
- [Lock standar](#lock-standar-pakai-ini-kalau-ragu)
- [Lock bertingkat](#lock-bertingkat)
- [Blok larangan](#blok-larangan)
- [Lock untuk bagian selain wajah](#lock-untuk-bagian-selain-wajah)
- [Kapan lock dilonggarkan](#kapan-lock-dilonggarkan)
- [Mendiagnosis lock yang gagal](#mendiagnosis-lock-yang-gagal)

## Kenapa model mengubah wajah

Model gambar dilatih pada foto internet yang didominasi wajah hasil retouch,
filter kecantikan, dan seleksi estetis. Jadi saat diminta "perbaiki foto ini",
arah "perbaikan" yang ia pelajari adalah: kulit lebih mulus, rahang lebih tirus,
mata lebih besar, hidung lebih kecil, kulit lebih terang, pori hilang.

Model tidak menganggap itu mengubah identitas — baginya itu bagian dari
"membuat foto lebih baik". Maka lock harus menyebut hal-hal itu **secara eksplisit
dan spesifik**. Kalimat umum seperti "keep it natural" hampir tidak berpengaruh,
karena model merasa hasil retouch-nya memang sudah natural.

Aturan praktisnya: **sebut bagian tubuhnya, bukan konsepnya.** "Preserve my
identity" lemah. "Keep my jawline width, nose shape, eye size, and skin texture
unchanged" kuat.

## Lock standar (pakai ini kalau ragu)

Satu kalimat, cukup untuk mayoritas kasus:

> Keep my face, facial structure, body shape, expression, hair, and skin texture
> exactly the same as the original. Do not beautify, slim, smooth, or reshape
> anything.

Versi lebih pendek untuk prompt yang sudah panjang:

> Keep my exact identity, facial structure, body, and skin texture unchanged.
> No beautification.

## Lock bertingkat

Pilih sesuai seberapa besar risiko perubahan wajah pada tugas tersebut.

**Tingkat 1 — ringan.** Untuk edit yang tidak menyentuh subjek sama sekali
(ganti background, crop, ubah rasio):

> Leave the subject completely untouched — only the background changes.

**Tingkat 2 — standar.** Untuk edit cahaya, warna, atau gaya menyeluruh:

> Keep my face, body, expression, clothing, and identity exactly the same.
> Do not beautify or alter any shape.

**Tingkat 3 — ketat.** Untuk restyle besar (editorial, sinematik, ganti setting)
di mana model paling mungkin "menggambar ulang" wajah:

> This is a real photograph of a real person and the person must remain
> recognizably identical. Preserve exactly: facial structure and proportions,
> jawline width, nose shape and size, eye shape and spacing, lip shape, hairline,
> ear shape, skin tone, skin texture including pores and fine lines, and every
> existing mole, freckle, scar, and blemish. Treat the face as a fixed, protected
> region — the edit applies to lighting, background, and color only.

**Tingkat 4 — maksimum.** Untuk foto identitas/dokumen, foto keluarga yang
bernilai sentimental, atau saat tingkat 3 sudah gagal sekali:

> Do not regenerate the face. Keep the original face pixels and only relight
> them. The output must be verifiably the same person — if any facial feature
> would need to be redrawn to achieve the requested style, skip that part of
> the style instead of changing the face.

Tingkat 4 mengorbankan sebagian kualitas gaya demi kemiripan. Jelaskan trade-off
ini ke user saat memakainya.

## Blok larangan

Larangan bekerja paling baik kalau spesifik dan tidak terlalu banyak. Pilih 4–6
yang paling relevan dengan tugasnya, jangan tempel semuanya sekaligus — daftar
larangan yang terlalu panjang justru melemahkan tiap butirnya.

**Anti-mempercantik (hampir selalu dipakai):**
- `Do not beautify.`
- `Do not smooth or blur the skin; keep visible pores and natural texture.`
- `Do not slim the face, jaw, nose, waist, or arms.`
- `Do not enlarge the eyes or alter eye spacing.`
- `Do not whiten or lighten the skin tone.`
- `Do not whiten the teeth.`
- `Do not remove moles, freckles, scars, acne, wrinkles, or fine lines.`
- `Do not remove or reshape facial hair.`
- `Do not change the hairline or add hair density.`

**Anti-artefak (untuk edit berat dan ganti background):**
- `No plastic or waxy skin.`
- `No hard cutout edge or halo around the hair.`
- `No mismatched lighting between the subject and the new background.`
- `No warped or melted background geometry.`
- `No extra or missing fingers.`
- `No duplicated jewelry, buttons, or patterns.`
- `No AI-looking oversharpening or haloing along high-contrast edges.`

**Anti-lebay (untuk gaya sinematik dan color grade):**
- `No exaggerated saturation.`
- `No artificial shine or glow on the skin.`
- `No heavy HDR look.`
- `No crushed blacks that lose shadow detail.`

## Lock untuk bagian selain wajah

Yang sering luput dan bikin hasil terasa "bukan aku":

| Yang dikunci | Kalimat |
|---|---|
| Pakaian | `Keep my clothing identical — same garment, color, fabric texture, folds, and fit.` |
| Kacamata | `Keep my glasses identical in frame shape, thickness, and color, with realistic lens reflections.` |
| Jilbab / penutup kepala | `Keep the headscarf identical in color, fabric, draping, and how it frames the face.` |
| Perhiasan | `Keep all jewelry exactly as it is — same pieces, same positions.` |
| Tato | `Preserve all tattoos exactly, with the same placement, scale, and linework.` |
| Postur | `Keep the exact same pose, head tilt, shoulder angle, and hand positions.` |
| Ekspresi | `Keep the exact same expression and the same degree of smile — do not widen it.` |
| Bentuk badan | `Keep my body proportions unchanged — no slimming, no broadening of shoulders.` |
| Usia | `Do not make me look younger or older than I am in the original.` |

## Kapan lock dilonggarkan

Lock bukan dogma. Longgarkan kalau perubahan itu memang yang diminta:

- User **memang minta** dipercantik ("bikin kulitku mulus dong") — turuti, tapi
  tetap kunci struktur wajah supaya tetap orang yang sama. Hapus larangan soal
  tekstur kulit, pertahankan larangan soal bentuk.
- Foto lama yang rusak dan perlu **restorasi** — di sini model memang harus
  merekonstruksi bagian yang hilang. Ganti larangan jadi: `Reconstruct only the
  physically damaged areas; leave all intact areas untouched.`
- **Ganti pakaian atau gaya rambut** yang disengaja — lepas lock untuk bagian itu
  saja, kunci sisanya lebih ketat dari biasanya.
- **GENERATE dari nol** — tidak ada orang nyata, lock tidak relevan sama sekali.

## Mendiagnosis lock yang gagal

| Gejala pada hasil | Sebab | Perbaikan |
|---|---|---|
| Mirip tapi terasa "bukan aku" | Struktur wajah bergeser halus | Naik ke tingkat 3, sebut jawline / nose / eye spacing satu per satu |
| Kulit seperti lilin atau plastik | Smoothing default model | Tambah `keep visible skin pores and natural texture, no smoothing` |
| Wajah jadi lebih muda | Bias kecantikan | Tambah `preserve all fine lines and wrinkles; do not de-age` |
| Kulit jadi lebih terang | Bias pencerahan | Tambah `keep my exact skin tone and undertone; do not lighten` |
| Jadi orang yang jelas berbeda | Model menggambar ulang wajah, bukan mengedit | Naik ke tingkat 4, dan pecah edit jadi beberapa langkah kecil |
| Wajah benar, badan berubah | Lock cuma menyebut wajah | Tambahkan lock bentuk badan dari tabel di atas |
| Background bagus, subjek "tertempel" | Cahaya subjek dan background tidak nyambung | Tambah `match the background lighting to the existing light direction on me` |
| Rambut punya garis potong kaku | Masking kasar | Tambah `render individual hair strands at the edge; no hard cutout, no halo` |

Kalau dua percobaan berturut-turut tetap gagal, **pecah jadi beberapa langkah**:
edit satu hal per generasi (cahaya dulu, baru background, baru grading) daripada
menyuruh model melakukan semuanya sekaligus. Tiap generasi yang lebih sederhana
berarti lebih sedikit alasan bagi model untuk menyentuh wajah.
