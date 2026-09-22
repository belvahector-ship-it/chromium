# 50 Kode Sudut & Framing Kamera

Setiap kode adalah singkatan. Model gambar tidak mengenali `/droneview` sebagai
perintah — yang dikenali adalah **kalimat penjabarannya**. Jadi kode dipakai untuk
komunikasi cepat dengan user ("mau /heroangle atau /eyelevel?"), lalu yang
dimasukkan ke prompt adalah kolom **Kalimat prompt**.

## Daftar isi
- [Cara memilih](#cara-memilih)
- [01 — Sudut dasar (1–10)](#01--sudut-dasar-110)
- [02 — Arah pandang (11–20)](#02--arah-pandang-1120)
- [03 — Posisi subjek (21–30)](#03--posisi-subjek-2130)
- [04 — Level & orientasi (31–40)](#04--level--orientasi-3140)
- [05 — Framing & perspektif (41–50)](#05--framing--perspektif-4150)
- [Efek psikologis tiap sudut](#efek-psikologis-tiap-sudut)
- [Menggabungkan kode](#menggabungkan-kode)

## Cara memilih

Sudut kamera menentukan bagaimana subjek **dibaca** oleh yang melihat, jauh
sebelum detail apa pun diperhatikan. Kamera di bawah mata membuat subjek terasa
berkuasa; di atas mata membuatnya terasa kecil atau akrab. Ini bukan selera — ini
konvensi visual yang sudah tertanam, dan model gambar mereproduksinya dengan setia.

Tiga pertanyaan yang cukup untuk memilih:
1. **Setinggi apa kameranya?** (drone → mata → lantai)
2. **Sejauh apa?** (extreme close-up → long shot)
3. **Subjek menghadap ke mana?** (depan → tiga perempat → samping → belakang)

Untuk potret yang jujur dan netral, `/eyelevel` + `/mediumshot` + `/threequarter`
adalah kombinasi paling aman. Menyimpang dari situ harus punya alasan.

> **Peringatan untuk mode EDIT:** mengubah sudut pada foto yang sudah ada berarti
> menyuruh model membayangkan wajah dari sudut yang tidak pernah difoto. Kemiripan
> hampir pasti berkurang. Pada EDIT, gunakan kode hanya untuk **mempertahankan**
> sudut asli (`Maintain the original eye-level framing`) atau menggeser sedikit.
> Kebebasan penuh memakai 50 kode ini ada di mode GENERATE. Kalau user memang
> butuh sudut baru dari foto yang ada, itu tugas tersendiri — buka
> `angle-change.md`, jangan hanya menempelkan kode dari tabel di bawah.

---

## 01 — Sudut dasar (1–10)

| # | Kode | Kalimat prompt |
|---|---|---|
| 1 | `/droneview` | Shot from a drone high above the subject, looking down, with the surrounding environment visible around them |
| 2 | `/birdsview` | Bird's-eye view from directly above, the subject seen from the top down against the ground |
| 3 | `/wormview` | Worm's-eye view from ground level looking steeply upward, the subject towering against the sky |
| 4 | `/highangle` | Camera positioned above the subject and angled down toward them |
| 5 | `/lowangle` | Camera positioned below the subject and angled up toward them |
| 6 | `/topleft` | Camera above and to the left of the subject, looking down diagonally |
| 7 | `/topright` | Camera above and to the right of the subject, looking down diagonally |
| 8 | `/bottomleft` | Camera below and to the left of the subject, looking up diagonally |
| 9 | `/bottomright` | Camera below and to the right of the subject, looking up diagonally |
| 10 | `/topdown` | Straight top-down shot, camera perfectly perpendicular above the subject |

## 02 — Arah pandang (11–20)

| # | Kode | Kalimat prompt |
|---|---|---|
| 11 | `/groundview` | Camera resting at ground level looking up, with the foreground ground plane prominent in frame |
| 12 | `/eyelevel` | Camera at the subject's eye level, looking straight at them — neutral and natural |
| 13 | `/sideview` | Camera positioned to the subject's side, capturing them side-on |
| 14 | `/backview` | Camera behind the subject, showing their back as they face away |
| 15 | `/overhead` | Camera directly overhead looking down at the subject standing below |
| 16 | `/closeup` | Close-up framing filling the frame with the subject's face and shoulders |
| 17 | `/wideangle` | Wide-angle lens showing the subject small within a broad environment |
| 18 | `/dutchangle` | Dutch angle with the camera deliberately tilted, creating a slanted, unsettled horizon |
| 19 | `/shoulderview` | Over-the-shoulder view from just behind the subject, looking past them at what they see |
| 20 | `/cinematiclow` | Low cinematic angle looking up at the subject with a wide lens and dramatic depth |

## 03 — Posisi subjek (21–30)

| # | Kode | Kalimat prompt |
|---|---|---|
| 21 | `/frontview` | Subject facing the camera directly, straight-on and symmetrical |
| 22 | `/threequarter` | Subject turned about 45 degrees from the camera — the classic flattering portrait angle |
| 23 | `/profileview` | Strict side profile, the subject's face seen at 90 degrees to the camera |
| 24 | `/fullbody` | Full-body framing from head to feet with the surroundings visible |
| 25 | `/ultrawide` | Ultra-wide lens with expansive surroundings and pronounced perspective at the frame edges |
| 26 | `/fisheye` | Fisheye lens with strong circular barrel distortion bowing the frame outward |
| 27 | `/heroangle` | Heroic low angle looking slightly up at the subject, making them appear confident and commanding |
| 28 | `/aerialview` | Aerial view from above and at a distance, showing the subject within the wider scene |
| 29 | `/floorlevel` | Camera placed on the floor near the subject, with the nearest part of them large in the foreground |
| 30 | `/dynamicangle` | Dynamic, energetic angle with a tilted frame and the subject caught mid-movement |

## 04 — Level & orientasi (31–40)

| # | Kode | Kalimat prompt |
|---|---|---|
| 31 | `/leftside` | Camera positioned to the subject's left, framing them from that side |
| 32 | `/rightside` | Camera positioned to the subject's right, framing them from that side |
| 33 | `/rearangle` | Camera behind and slightly to one side, showing the back and a sliver of the profile |
| 34 | `/diagonalview` | Camera on a diagonal to the subject, with strong receding diagonal lines in the scene |
| 35 | `/cornerangle` | Camera at a corner-on angle, capturing two converging planes of the environment behind the subject |
| 36 | `/tiltedview` | Camera tilted downward from above with the frame rotated, looking at the subject who looks back up |
| 37 | `/extremelow` | Extreme low angle almost at ground level, looking sharply up so the subject dominates the sky |
| 38 | `/extremehigh` | Extreme high angle far above, looking sharply down so the subject appears small on the ground |
| 39 | `/waistlevel` | Camera at the subject's waist height, looking slightly upward |
| 40 | `/chestlevel` | Camera at the subject's chest height — subtly flattering and very natural for portraits |

## 05 — Framing & perspektif (41–50)

| # | Kode | Kalimat prompt |
|---|---|---|
| 41 | `/kneelevel` | Camera at knee height, looking slightly up at the subject |
| 42 | `/footlevel` | Camera at foot level, the subject's feet nearest the lens and their body receding upward |
| 43 | `/headlevel` | Camera level with the top of the subject's head, looking horizontally across |
| 44 | `/POVview` | First-person point of view, as if seen through the subject's own eyes |
| 45 | `/selfieangle` | Selfie framing — arm's length, slightly above eye level, the subject looking into the lens |
| 46 | `/longshot` | Long shot with the full figure small in frame and the environment dominant |
| 47 | `/mediumshot` | Medium shot framing the subject from the waist up |
| 48 | `/extremecloseup` | Extreme close-up filling the frame with a single feature, such as the eyes |
| 49 | `/cinematicwide` | Wide cinematic composition with the subject small against a vast, carefully composed background |
| 50 | `/perspectiveview` | Strong one-point perspective with converging lines leading toward the subject |

---

## Efek psikologis tiap sudut

Ini yang sebenarnya dipilih user saat mereka memilih sudut, walau mereka
menyebutnya dengan kata lain.

| Kesan yang diinginkan | Kode yang bekerja |
|---|---|
| Berwibawa, percaya diri, berkuasa | `/lowangle` `/heroangle` `/cinematiclow` `/extremelow` |
| Setara, jujur, bisa dipercaya | `/eyelevel` `/chestlevel` `/frontview` |
| Ramah, mudah didekati | `/highangle` sedikit saja, `/selfieangle` |
| Kecil, rentan, terisolasi | `/extremehigh` `/birdsview` `/longshot` |
| Megah, sinematik, berskala | `/cinematicwide` `/ultrawide` `/aerialview` |
| Intim, emosional | `/closeup` `/extremecloseup` |
| Gelisah, tegang | `/dutchangle` `/tiltedview` |
| Energik, bergerak | `/dynamicangle` `/POVview` |
| Formal, netral, dokumenter | `/frontview` + `/eyelevel` |
| Klasik, paling menguntungkan wajah | `/threequarter` + `/chestlevel` |

**Catatan potret:** `/lowangle` yang terlalu ekstrem menonjolkan lubang hidung dan
dagu; `/highangle` yang berlebihan mengecilkan dahi dan badan. Untuk potret orang
sungguhan, pergeseran kecil dari eye level hampir selalu lebih baik daripada sudut
dramatis.

## Menggabungkan kode

Tiga kode maksimal, masing-masing menjawab pertanyaan berbeda — **tinggi**,
**jarak**, dan **orientasi subjek**. Menumpuk dua kode yang menjawab pertanyaan
sama akan saling membatalkan.

✅ `/chestlevel` + `/mediumshot` + `/threequarter`
→ *Camera at chest height, framing the subject from the waist up, with the subject
turned about 45 degrees from the lens.*

✅ `/lowangle` + `/fullbody` + `/perspectiveview`
→ *Camera below the subject looking up, full-body framing head to feet, with strong
converging perspective lines leading toward them.*

❌ `/closeup` + `/longshot` — bertabrakan, dua jarak sekaligus
❌ `/birdsview` + `/wormview` — bertabrakan, dua ketinggian berlawanan
❌ `/frontview` + `/profileview` — bertabrakan, dua orientasi sekaligus

Kalau user meminta kombinasi yang bertabrakan, tanyakan mana yang lebih penting
bagi mereka daripada menebak — dua kode yang bertentangan biasanya membuat model
memilih salah satu secara acak, dan hasilnya tidak bisa diulang.
