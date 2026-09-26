# Riset: Membangun Speaker Bluetooth Aktif AC/DC ±400 W RMS Berbasis Modul

> **Untuk:** hobiis audio Indonesia · **Tanggal riset:** September 2026 · **Pendekatan:** modul siap pakai (tanpa desain PCB)
>
> **Catu daya:** listrik PLN 220–230 V AC → SMPS 48 V DC di dalam kabinet. **Tanpa baterai.** (Revisi dari versi sebelumnya yang memakai baterai LiFePO4; semua komponen dan biaya baterai sudah dihapus.)
>
> **Konvensi label data** (dipakai di seluruh dokumen):
> - **[T]** = *terverifikasi*: angka diambil langsung dari datasheet/halaman produk/review, nomor sumber ditulis sebagai [R#] (lihat bagian 13).
> - **[E]** = *estimasi/perhitungan*: hasil rumus atau asumsi penulis. Rumus dan asumsinya selalu dicantumkan.
> - **[V]** = *perlu verifikasi*: informasi yang belum bisa dikonfirmasi dari sumber primer, atau yang berbeda-beda antar penjual. Cek sendiri sebelum membeli.
>
> Semua harga dalam Rupiah adalah **[E]**, disusun dari listing Tokopedia/Shopee/AliExpress/toko luar yang ditemukan pada 2025–2026. Untuk harga luar negeri dipakai kurs asumsi **US$1 ≈ Rp16.500** dan **€1 ≈ Rp19.000**, ditambah ongkir/bea kira-kira 15–30%.

---

## Daftar Isi

1. [Ringkasan & Rekomendasi Utama](#1-ringkasan--rekomendasi-utama)
2. [Spesifikasi Target](#2-spesifikasi-target)
3. [Arsitektur & Diagram Blok](#3-arsitektur--diagram-blok)
4. [Perhitungan Daya, Tegangan, Arus, dan Konsumsi Listrik](#4-perhitungan-daya-tegangan-arus-dan-konsumsi-listrik)
5. [Pilihan Modul: Tabel Perbandingan](#5-pilihan-modul-tabel-perbandingan)
6. [Skema Wiring](#6-skema-wiring)
7. [Driver & Enclosure](#7-driver--enclosure)
8. [Catu Daya AC/DC & Proteksi](#8-catu-daya-acdc--proteksi)
9. [BOM: Dua Varian](#9-bom-dua-varian)
10. [Perakitan](#10-perakitan)
11. [Tuning & Pengujian](#11-tuning--pengujian)
12. [Keselamatan](#12-keselamatan)
13. [Sumber/Referensi](#13-sumberreferensi)

---

## 1. Ringkasan & Rekomendasi Utama

**Kesimpulan singkat**

1. **Arsitektur: 2.1.** Dua satelit 2-way (woofer 6,5" + tweeter, crossover pasif sekitar 2,5–2,8 kHz) ditambah satu subwoofer 8–10". DSP memotong satelit di atas ±90 Hz dan subwoofer di bawahnya. Untuk speaker aktif satu kabinet, 2.1 lebih efisien daripada 2.0: bass di bawah ±100 Hz praktis tidak terdengar arahnya, jadi cukup satu kabinet bass yang besar, dan satelit bisa dibuat kecil.
2. **Tegangan: rail 48 V DC dari SMPS.** Dengan beban 4–8 Ω, rail 12 V atau 24 V tidak bisa menghasilkan 400 W nyata. Batasnya dijelaskan oleh rumus **P = V²/(2R)** di bagian 4. SMPS memberi tegangan konstan, jadi daya amp selalu penuh (tidak turun seiring pemakaian).
3. **Amplifier: TPA3255 (TI)**, dipakai dua board. Board #1 stereo (BTL) untuk satelit 8 Ω, board #2 mono (PBTL) untuk sub 4 Ω. Menurut datasheet TI, satu TPA3255 menghasilkan 255 W/4 Ω (BTL, 1% THD+N, 51 V) dan 315 W/4 Ω (PBTL, 1% THD+N, 53,5 V) [T][R2].
4. **Bluetooth:** modul **Qualcomm QCC5125** (aptX HD/Adaptive; LDAC tergantung firmware modul [V]) atau **QCC3034** (aptX HD). Keluarannya **analog** ke DSP. Jalur analog paling mudah dan paling bebas masalah clock. I2S langsung ke ADAU1701 tidak disarankan karena ADAU1701 hanya bisa menjadi slave yang sinkron ke MCLK-nya sendiri [T][R21][R22].
5. **DSP:** **miniDSP 2x4 HD** untuk High-end (catu 12 V DC, 10 PEQ per kanal, crossover, compressor/limiter, input optik [T][R23]). Untuk Menengah dipakai **Wondom APM2 (ADAU1701)** + programmer ICP5 dan SigmaStudio [T][R19].
6. **Catu daya: SMPS 48 V dari listrik PLN**, disetel tepat **48,0 V** (di bawah batas TPA3255 51 V untuk beban 4 Ω dan 53,5 V untuk beban ≥6 Ω [T][R2]).
   - **Menengah: Mean Well LRS-600-48** (48 V 12,5 A, 600 W, efisiensi 92%, output bisa disetel 45,6–52,8 V) [T][R61].
   - **High-end: Mean Well HRP-600-48** (48 V 13 A, 624 W, **PFC aktif**, input 85–264 VAC) [T][R62]. PFC membuat arus yang ditarik dari PLN lebih kecil dan bersih, jadi lebih ramah untuk langganan listrik rumah 900–1.300 VA.
   - Rail 12 V untuk DSP/Bluetooth/kipas diambil dari **SMPS kecil terpisah** (mis. Mean Well LRS-35-12) supaya derau amp tidak masuk ke jalur sinyal.

**Kombinasi modul yang direkomendasikan**

| Blok | **Varian Menengah** (≈ Rp9,2–13,3 jt) [E] | **Varian High-end** (≈ Rp20,3–28,1 jt) [E] |
|---|---|---|
| Bluetooth | ZK-QCC (QCC3034 atau QCC5125) + DAC PCM5102A, catu 8–32 V [T][R31] | QCC5125 (LDAC/aptX HD) + DAC, atau QCC5125 → optik ke DSP [R29][R30][R32] |
| DSP | Wondom APM2 AA-AP23122 (ADAU1701, 2-in/4-out) + ICP5 [R19] | miniDSP 2x4 HD (2-in/4-out, 12 V, limiter) [R23] |
| Amp satelit | ZK-3002 (TPA3255) BTL stereo [R13] | 3e Audio 260-2-29A (2×TPA3255, PFFB, input balanced) [R12] |
| Amp sub | ZK-3002 (TPA3255) PBTL mono [R13] | ZK-3002 PBTL (sub tidak butuh THD ultra-rendah) |
| Power | SMPS **Mean Well LRS-600-48** (48 V 12,5 A) + SMPS kecil 12 V [R61] | SMPS **Mean Well HRP-600-48** (48 V 13 A, PFC aktif) + SMPS kecil 12 V [R62] |
| Driver | 2× Dayton DC160-8 + 2× DC28FS-8 + 1× RSS210HO-4 | 2× SB Acoustics SB17NRX2C35-8 + 2× SB26STCN-C000-4 + 1× Dayton RSS265HO-4 |
| Kapasitas daya amp | 2×≈125 W (8 Ω) + ≈254 W (4 Ω) ≈ **500 W** @48 V [E] | 2×≈125 W (8 Ω) + ≈254 W (4 Ω) ≈ **500 W** @48 V [E] |

**Alternatif ringkas (paling sedikit kabel):** Wondom **JAB5** (AA-JA33286) all-in-one: QCC3034 + ADAU1701 + amp 4 kanal, 10–39 V, mode 2.1 = 2×100 W + 1×200 W menurut pabrikan [T][R15][R16]. Catu dengan SMPS **36 V** (mis. Mean Well LRS-350-36 [V]), bukan 48 V, karena batas board 39 V. Hitungan di bagian 4 menunjukkan daya nyatanya (1% THD) lebih mungkin di kisaran **300–350 W** [E], jadi sedikit di bawah target 400 W.

---

## 2. Spesifikasi Target

| Parameter | Target | Catatan |
|---|---|---|
| Sumber daya | Listrik PLN 220–230 V AC → SMPS 48 V DC internal | Stop kontak **berarde**; tegangan AC hanya ada di ruang elektronik tertutup (lihat bagian 8 & 12) |
| Daya | ±400 W RMS nyata (kapasitas amp @1% THD+N) | Bukan PMPO. Daya kontinu ke driver dibatasi limiter DSP sesuai rating thermal driver |
| Konfigurasi | 2.1: satelit 2-way + sub | Crossover DSP ±80–100 Hz, LR4 (24 dB/okt) |
| Input | Bluetooth 5.x aptX HD (LDAC opsional), AUX analog | Jalur analog dari modul BT ke DSP |
| Respons target | ±35 Hz – 20 kHz (−6 dB) | Sub sealed + EQ, atau ported (verifikasi di WinISD) |
| SPL maks. | ±110–115 dB @1 m (puncak) [E] | Tergantung sensitivitas driver dan ukuran box |
| Konsumsi listrik | ±80–100 W saat musik keras, ±15–20 W idle [E] | Lihat 4.5 |
| Proteksi | Fuse AC di inlet, arde (PE) ke chassis, fuse DC per amp, OCP/OVP/OTP SMPS, limiter DSP, OTP/OCP internal amp | Lihat bagian 8 |

---

## 3. Arsitektur & Diagram Blok

### 3.1 Perbandingan 2.0 dan 2.1

| Aspek | **2.0 stereo (mis. 2×200 W)** | **2.1 (mis. 2×100 W + 1×200 W)** |
|---|---|---|
| Kebutuhan driver | Tiap sisi butuh woofer besar (8"+) untuk bass dalam | Satelit cukup 5–6,5"; satu sub 8–10" |
| Volume kabinet | Dua kabinet besar | Dua satelit kecil (5–10 L) + satu box sub (10–30 L) |
| Efisiensi daya | Kedua kanal harus kuat di bass | Daya besar hanya di kanal sub, satelit lebih ringan |
| Distorsi/IMD | Woofer menangani bass + vokal sekaligus | Satelit bebas ekskursi besar, sehingga vokal lebih bersih |
| Stereo image | Sedikit unggul di bass (tidak signifikan di bawah ±100 Hz) | Setara di atas crossover |
| Kompleksitas DSP | Cukup PEQ + HPF subsonik | Perlu crossover, sum mono sub, delay/phase |
| Jumlah kanal amp | 2 | 3 (atau 2 board TPA3255: 1 BTL stereo + 1 PBTL) |
| Portabilitas (boombox) | Kurang: dua kabinet berat | Baik: sub dan satelit bisa disatukan dalam satu kabinet bersekat |

**Rekomendasi: 2.1.** Daya amp paling banyak terpakai di bass. Menaruh bass di satu driver besar dalam box yang optimal lebih efisien daripada dua woofer kecil, sehingga SMPS dan amp tidak perlu sebesar sistem 2.0 untuk kerasnya bass yang sama. Satu kabinet "boombox" bersekat (dua ruang satelit tertutup + ruang sub + ruang elektronik) juga lebih praktis dipindah-pindah.

### 3.2 Diagram blok sistem (daya + sinyal)

```mermaid
flowchart LR
    subgraph POWER["Jalur Daya (AC → DC)"]
        PLN["Stop kontak PLN<br/>220–230V AC berarde"]
        INLET["Inlet IEC C14<br/>+ saklar + fuse T6,3A"]
        SMPS48["SMPS 48V<br/>Menengah: LRS-600-48<br/>High-end: HRP-600-48"]
        SMPS12["SMPS kecil 12V<br/>LRS-35-12"]
        BUS["Bus DC amp<br/>48,0V konstan"]
        BUCK["Buck 12V→5V<br/>(APM2, Menengah)"]
        PLN --> INLET --> SMPS48 --> BUS
        INLET --> SMPS12
        SMPS12 --> BUCK
    end

    subgraph SIGNAL["Jalur Sinyal"]
        PHONE(("Ponsel"))
        BT["Modul BT<br/>QCC3034/QCC5125 + DAC"]
        DSP["DSP<br/>APM2 (ADAU1701) / miniDSP 2x4 HD"]
        AMP1["Amp #1 TPA3255<br/>BTL stereo"]
        AMP2["Amp #2 TPA3255<br/>PBTL mono"]
        XL["Crossover pasif L"]
        XR["Crossover pasif R"]
        WL["Woofer L"]; TL["Tweeter L"]
        WR["Woofer R"]; TR["Tweeter R"]
        SUB["Subwoofer 4Ω"]
        PHONE -- "aptX HD / LDAC" --> BT
        BT -- "analog L/R" --> DSP
        DSP -- "OUT1 L (HPF)" --> AMP1
        DSP -- "OUT2 R (HPF)" --> AMP1
        DSP -- "OUT3 Sub (LPF)" --> AMP2
        AMP1 --> XL --> WL & TL
        AMP1 --> XR --> WR & TR
        AMP2 --> SUB
    end

    BUS --> AMP1
    BUS --> AMP2
    SMPS12 --> DSP
    SMPS12 --> BT
```

### 3.3 Diagram sinyal audio (I2S/analog dan crossover)

```mermaid
flowchart TB
    SRC["Bluetooth A2DP<br/>SBC/AAC/aptX/aptX HD/(LDAC)"] --> DEC["Decoder di QCC5125/QCC3034<br/>(domain digital, 44,1/48/96 kHz)"]
    DEC -- "I2S internal board" --> DAC["DAC on-board<br/>PCM5102A / ES9023"]
    DEC -. "Opsi High-end: I2S → S/PDIF optik<br/>(board FYF QCC5125)" .-> DSPIN
    DAC -- "Analog ±2 Vrms" --> DSPIN["Input DSP<br/>ADC ADAU1701 / input miniDSP"]
    DSPIN --> MIX["Matrix: L, R, Mono (L+R)/2"]
    MIX --> HPL["L: HPF LR4 90 Hz<br/>+ PEQ + Limiter"] --> O1["OUT1"]
    MIX --> HPR["R: HPF LR4 90 Hz<br/>+ PEQ + Limiter"] --> O2["OUT2"]
    MIX --> LPS["Sub: LPF LR4 90 Hz<br/>+ HPF subsonik 25 Hz (BW2)<br/>+ Low-shelf/Linkwitz Transform<br/>+ Delay/Polaritas + Limiter"] --> O3["OUT3"]
    O1 --> A1L["TPA3255 BTL kanal A"] --> XO1["Crossover pasif LR2 ±2,5–2,8 kHz"] --> W1["Woofer L"] & T1["Tweeter L"]
    O2 --> A1R["TPA3255 BTL kanal B"] --> XO2["Crossover pasif LR2"] --> W2["Woofer R"] & T2["Tweeter R"]
    O3 --> A2["TPA3255 PBTL"] --> S1["Sub 4 Ω"]
```

**Mengapa jalur analog, bukan I2S langsung?** Modul BT hampir selalu menjadi *I2S master*. Port serial ADAU1701 harus sinkron dengan MCLK DSP (rasio 64/256/384/512×Fs) dan tidak punya ASRC, sehingga menyambung I2S dari modul BT biasanya memaksa modifikasi clock [T][R21][R22]. Jalur analog (DAC PCM5102A/ES9023 di modul BT → ADC ADAU1701) menambah satu konversi. Namun dengan ADC ADAU1701 (SNR 100 dB, THD+N −83 dB [T][R20]), kualitasnya jauh melampaui kebutuhan speaker aktif ini. Untuk jalur full-digital di High-end, pakai board QCC5125 dengan output optik [T][R32] ke input TOSLINK miniDSP 2x4 HD [T][R23]. Apakah input optik miniDSP menerima sample rate BT secara asinkron masih **[V]** dan perlu dicek di manual miniDSP.

---

## 4. Perhitungan Daya, Tegangan, Arus, dan Konsumsi Listrik

### 4.1 Rumus dasar: kenapa tegangannya harus tinggi

Amplifier class-D BTL (bridge) mengayunkan beban dari hampir 0 sampai hampir PVDD di kedua sisinya. Tegangan puncak di speaker ≈ PVDD × k, dengan *k* ≈ 0,87–0,94 karena rugi R_DS(on) MOSFET, induktor filter, dan batas clipping. Daya sinus kontinu:

$$P = \frac{V_{rms}^2}{R} = \frac{V_{peak}^2}{2R} \approx \frac{(k \cdot PVDD)^2}{2R}$$

**Kalibrasi *k* dari datasheet TPA3255 [T][R2]:**

| Kondisi datasheet (1% THD+N) | Daya | V_peak = √(2PR) | k = V_peak/PVDD |
|---|---|---|---|
| BTL, 4 Ω, PVDD 51 V | 255 W | 45,2 V | **0,89** |
| BTL, 8 Ω, PVDD 53,5 V | 155 W | 49,8 V | **0,93** |
| PBTL, 4 Ω, PVDD 53,5 V | 315 W | 50,2 V | **0,94** |
| PBTL, 2 Ω, PVDD 51 V | 495 W | 44,5 V | **0,87** |

Perbandingan dengan pengukuran independen: Archimago mengukur Fosi V3 Mono (TPA3255, 48 V/10 A) sekitar **200 W/4 Ω dan 100 W/8 Ω pada ambang 0,1% THD+N** [T][R8]. ASR mencatat ±190 W/4 Ω dengan PSU 48 V/5 A [T][R9]. Angka ini konsisten dengan model di atas: batas 0,1% sedikit di bawah batas 1%.

**Contoh: kenapa 12 V gagal.** Dengan adaptor/SMPS 12 V ke 4 Ω BTL: P ≈ (0,89×12)²/(2×4) ≈ **14 W** per kanal. Untuk 400 W total dibutuhkan beban < 1 Ω atau belasan chip, jadi tidak realistis.

### 4.2 Daya per tegangan SMPS (TPA3255, 1% THD+N) [E]

| Tegangan SMPS | Contoh model | BTL 8 Ω | BTL 4 Ω | PBTL 4 Ω | PBTL 2 Ω | **2×BTL8 + PBTL4** | Cocok untuk target 400 W? |
|---|---|---|---|---|---|---|---|
| 12 V | adaptor laptop/LED | 8 | 15 | 16 | 27 | 31 W | Tidak |
| 24 V | LRS-350-24 [V] | 31 | 58 | 64 | 109 | 126 W | Tidak |
| 36 V | LRS-350-36 [V] | 70 | 131 | 143 | 245 | 283 W | Hanya bila beban 4 Ω + sub 2 Ω (2×131 + 245 = 507 W), atau untuk JAB5 |
| **48 V** | **LRS-600-48 / HRP-600-48** [R61][R62] | **125** | **233** | **254** | **436** | **504 W** | **Ya (rekomendasi)** |

Batas PVDD TPA3255 menurut *Recommended Operating Conditions*: 18–51 V untuk R_L = 4 Ω dan 18–53,5 V untuk R_L ≥ 6 Ω [T][R2]. Board yang dipakai juga punya batas sendiri: ZK-3002 18–50 V [T][R13], 3e 260-2-29A 36–51 V [T][R12]. Output LRS-600-48 bisa disetel **45,6–52,8 V** [T][R61], jadi **setel tepat 48,0 V dengan multimeter dan jangan pernah di atas 50 V**.

Keunggulan SMPS dibanding baterai: tegangan **konstan**, jadi daya maksimum amp sama di menit pertama maupun jam kelima, dan tidak ada komponen BMS, charger, atau boost.

### 4.3 Memilih SMPS 48 V

Kebutuhan dari bus 48 V saat **sinus penuh di semua kanal** (kondisi uji terberat): 504 W / η 0,88 ≈ **573 W → 11,9 A** [E]. Musik keras rata-rata hanya ±1/8 dari itu (lihat 4.4).

| Kriteria | Mean Well LRS-350-48 | **Mean Well LRS-600-48** | **Mean Well HRP-600-48** | 2× SMPS terpisah (satu per amp) |
|---|---|---|---|---|
| Daya / arus | 350 W / ±7,3 A [V] | 600 W / 12,5 A [T][R61] | 624 W / 13 A [T][R62] | mis. 2× LRS-350-48 ≈ 700 W |
| Sinus penuh 573 W | Tidak (OCP bisa memutus di bass panjang) | Ya, mepet (±95%) | Ya | Ya |
| Musik keras (±80 W) | Ya | Ya | Ya | Ya |
| Input AC | [V] cek saklar pilih tegangan | Saklar pilih 90–132 / 180–264 VAC: **wajib posisi 230 V** [T][R61] | 85–264 VAC otomatis, **PFC aktif** [T][R62] | – |
| Pendinginan | [V] | Kipas dengan kontrol ON/OFF [T][R61] | [V] | – |
| Harga [E] | ±Rp550–800 rb [V] | ±Rp1,1–1,3 jt (US$59,90 [R61]) | ±Rp2,6–3 jt (US$138,30 [R62]) | ±Rp1,1–1,6 jt |
| **Kesimpulan** | Hemat, hanya bila limiter DSP disetel ketat | **Menengah** | **High-end** | Alternatif: satelit dan sub tidak saling "menarik" rail |

**Kenapa tidak cukup SMPS 400 W untuk amp 400 W?** Puncak transien musik dipasok kapasitor bulk di board amp, tetapi bass yang panjang dan keras (EDM, dangdut koplo dengan kendang/bass berat) bisa menahan arus tinggi cukup lama sampai proteksi arus lebih SMPS bekerja dan suara putus-putus. Margin ±20–50% di atas kebutuhan rata-rata keras membuat sistem tidak pernah menyentuh batas itu.

**Langganan listrik PLN 900 VA:** musik normal (±80–100 W) sangat aman. Uji sinus penuh ±620–650 W dengan SMPS tanpa PFC aktif bisa menarik VA lebih besar dari W-nya dan berisiko menjatuhkan MCB meteran bila bersamaan dengan beban lain [E]. PFC aktif pada HRP-600-48 [T][R62] membuat VA ≈ W, jadi lebih aman untuk rumah 900–1.300 VA. Apakah LRS-600-48 punya PFC aktif tidak tercantum di ringkasan spesifikasi yang ditemukan **[V]**.

### 4.4 Arus per cabang (untuk fuse dan kabel) [E]

Asumsi: efisiensi amp η ≈ 0,88 (TI: 90% @4 Ω [T][R1]), efisiensi SMPS 92% [T][R61]. Kedua varian memakai bus 48 V yang sama.

| Cabang | Arus / daya |
|---|---|
| Amp satelit (2×125 W) | 250/0,88 = 284 W → **5,9 A** |
| Amp sub (254 W) | 289 W → **6,0 A** |
| DSP + BT + kipas | Dari **SMPS 12 V terpisah** (±0,5 A di 12 V), tidak membebani bus 48 V |
| **Total bus 48 V (sinus penuh)** | ≈ 573 W → **11,9 A** |
| Musik keras (rata-rata ±63 W audio) | ≈ 72 W + idle → ±1,7 A |
| Sisi AC 230 V (sinus penuh) | ±623 W input SMPS → ±2,7 A bila PF ≈ 1 (HRP); lebih besar bila PF rendah |

Catatan: musik punya *crest factor* (rasio puncak/rata-rata) besar. Pada volume "sangat keras tapi belum clipping", daya rata-rata biasanya hanya ±1/8 dari daya maksimum [E, aturan praktis]. Puncak transien dipasok kapasitor bulk di board amp. Karena itu fuse dipilih dari arus sinus penuh, bukan dari rata-rata.

### 4.5 Konsumsi listrik [E]

$$E\,[kWh] = \frac{P_{AC}\,[W] \times t\,[jam]}{1000}$$

| Kondisi | Daya dari PLN | Per jam | Pemakaian 4 jam/hari × 30 hari |
|---|---|---|---|
| Idle (BT tersambung, hening) | ±15–20 W | ±0,02 kWh | ±2,4 kWh |
| Volume sedang | ±30–35 W | ±0,035 kWh | ±4 kWh |
| Musik keras | ±80–100 W | ±0,1 kWh | ±12 kWh |
| Sinus penuh (uji, beberapa detik saja) | ±620–650 W | – | – |

Dengan tarif rumah tangga ±Rp1.444,70/kWh (golongan R-1 ≥1.300 VA) **[V]**, pemakaian musik keras 4 jam/hari ≈ 12 kWh ≈ **Rp17 ribu/bulan**. Matikan saklar utama bila tidak dipakai karena SMPS tetap menarik daya kecil tanpa beban.

---

## 5. Pilihan Modul: Tabel Perbandingan

### 5.1 Chip/modul amplifier class-D

| Chip | Rentang PVDD | Daya per datasheet | THD+N / noise | Idle | Panas & heatsink | Status untuk target 400 W |
|---|---|---|---|---|---|---|
| **TI TPA3255** | 18–53,5 V (51 V untuk 4 Ω) [T][R2] | BTL: 255 W/4 Ω @51 V, 155 W/8 Ω @53,5 V (1%); PBTL: 495 W/2 Ω @51 V, 315 W/4 Ω @53,5 V (1%) [T][R2] | 0,006% @1 W/4 Ω; noise <85 µV; SNR >111 dB [T][R1] | <2,5 W [T][R2] | Kemasan pad-up (HTSSOP-44 DDV), **wajib heatsink atas**; data termal diukur dengan heatsink 85 °C [T][R2]. Board biasanya pakai heatsink besar + kipas | **Pilihan utama** |
| TI TPA3251 | 12–36 V [T][R3] | BTL 140 W/4 Ω, 175 W/3 Ω; PBTL 285 W/2 Ω (1%, 36 V) [T][R3] | 0,005% @1 W; noise <60 µV [T][R3] | Rendah | Heatsink wajib | Bisa: 2×140 (4 Ω) + 285 (2 Ω) ≈ 565 W, tapi butuh beban 4 Ω/2 Ω dan rail 36 V teregulasi (mis. SMPS 36 V) |
| TI TPA3221 | 7–30 V [T][R5] | 2×105 W/4 Ω; 1×208 W/2 Ω PBTL [T][R5] | Loop feedback 100 kHz; idle <0,25 W (mode HEAD) [T][R5] | **Sangat rendah** | Heatsink sedang | Terbatas: 2×105 + 208 ≈ 420 W hanya dengan 3 chip & beban 4/2 Ω di 30 V. Punya proteksi DC speaker bawaan |
| TI TPA3116D2 | 4,5–26 V [T][R4] | 2×50 W/4 Ω @21 V; 100 W/2 Ω PBTL [T][R4] | 0,1% @1 kHz [T][R4] | Rendah | Heatsink kecil | **Tidak cukup** (butuh 4 chip PBTL 2 Ω untuk 400 W); cocok untuk proyek 50–200 W |
| TI TAS5630B | 25–52,5 V [T][R6] | 2×300 W BTL; 400 W PBTL (10% THD) [T][R6] | 0,03% @1 W/4 Ω; SNR >100 dB [T][R6] | Lebih tinggi | Heatsink besar; butuh catu 12 V terpisah untuk GVDD | Generasi lama (PurePath HD). Masih aktif, tetapi THD kalah dari TPA3255 |
| Infineon MA12070 | 4–26 V [T][R7] | 2×80 W/4 Ω @26 V (10% THD, puncak) [T][R7] | 0,004% (klaim); efisiensi >91% @8 Ω [T][R7] | **<160 mW** @26 V [T][R7] | Sangat ringan | **Tidak cukup** untuk 400 W (rail maks. 26 V). Unggul untuk konsumsi idle (sangat kecil). Varian MA12070P punya input I2S |
| Infineon MA12040 | ≤26 V [V] | Lebih kecil dari MA12070 [V] | Tidak diverifikasi | Rendah | Ringan | Tidak cocok |

### 5.2 Board amplifier siap pakai (TPA3255)

| Board | Konfigurasi | Catu | Klaim daya | Fitur | Harga [E] |
|---|---|---|---|---|---|
| **ZK-3002** (Wuzhi/ZK) | BTL 2 kanal atau PBTL mono (bisa dipilih) [T][R13] | 18–50 V (batas 53 V); sarankan 36–48 V ≥10 A [T][R13] | BTL 2×300 W/4 Ω @50 V; PBTL 600 W/2 Ω @50 V (klaim penjual, kemungkinan 10% THD) [R13] | Gain depan 26–36 dB bisa disetel, kipas berkontrol suhu [R13] | ±Rp600–800 rb (Tokopedia) [R14] |
| **3e Audio 260-2-29A** | Stereo, **2× TPA3255** (tiap kanal PBTL), **PFFB** [T][R12] | 36–51 V [T][R12] | 2×260 W/4 Ω, 2×150 W/8 Ω @1% THD+N [T][R12] | Input XLR + RCA, THD+N 0,0007%, noise 18 µV, Zout 10 mΩ [T][R12] | €149 → ±Rp2,8–3,3 jt |
| 3e Audio TPA3255-2CH-260W | Stereo BTL saja [T][R11] | 24–51 V, UVP 24 V [T][R11] | 260 W/4 Ω @1%; 150 W/8 Ω [T][R11] | Output AUX 12 V/0,2 A untuk DSP [T][R11] | [V] |
| BDM8 / "TPA3255 2.0" generik | BTL stereo | 19–48 V [R14] | 2×300 W (klaim) | Beberapa varian punya BT 5.x on-board | ±Rp750 rb–1 jt [R14] |

**Catatan kualitas:** PFFB (*post-filter feedback*) membuat respons frekuensi tidak bergantung beban dan impedansi output sangat rendah (±10 mΩ) [T][R10]. Pengaruhnya paling terasa di satelit (tweeter/woofer 8 Ω). Untuk sub, board ZK-3002 non-PFFB sudah memadai.

### 5.3 Modul Bluetooth

| Modul/chip | BT | Codec | Output | Catu | Catatan | Harga [E] |
|---|---|---|---|---|---|---|
| **ZK-QCC (QCC3034 atau QCC5125)** | 5.0 / 5.1 | SBC, AAC, aptX, aptX LL, aptX HD; **LDAC hanya versi QCC5125** [T][R31] | Analog (PCM5102A) + header I2S; USB-C sound card (QCC5125) [T][R31] | **DC 8–32 V** [T][R31] | SNR 112 dB (klaim) [R31]; bisa langsung dari bus 12 V/24 V | ±Rp350–700 rb [E] |
| QCC5125 → I2S (Audiophonics) | 5.0 | aptX, aptX HD, aptX Adaptive, LDAC [T][R29] | **I2S** (pad solder) | 5 V [T][R29] | Modul "SJR-BTM525"; pinout dari datasheet chip [R29] | €32,90 |
| QCC5125 + ES9023 (Audiophonics) | 5.1 | aptX, aptX HD, LDAC [T][R30] | Analog RCA [T][R30] | 5 V DC / 7–12 V AC [T][R30] | Ukuran 52×35 mm | €32,90 |
| FYF QCC5125 digital board | 5.1 | s.d. LDAC [T][R32] | Optik/koaksial/AES 192k/24; I2S 384k/32 [T][R32] | [V] | Jalur full-digital ke miniDSP (TOSLINK) | US$39–50 |
| Qualcomm QCC3040 (Arylic B50/BP50) | 5.2 | aptX HD, aptX Adaptive, AAC [T][R26] | Produk jadi | – | Referensi chip; modul DIY-nya jarang | – |

**Tentang LDAC:** di halaman resmi Qualcomm, QCC5125 disebut mendukung aptX/aptX HD/aptX LL/aptX Adaptive/AAC/SBC serta antarmuka I2S/PCM/SPDIF [T][R27]. **LDAC (codec Sony) tidak tercantum di sana**; dukungan LDAC berasal dari firmware pembuat modul [V]. QCC3034 mendukung aptX HD tetapi tidak Adaptive [T][R28]. Untuk iPhone (AAC saja) semua modul di atas setara.

**Noise dan ground loop:** masalah paling umum pada speaker BT + class-D yang berbagi satu catu adalah dengung/"cuit" saat modul BT aktif. Arus burst radio BT dan arus besar amp mengalir lewat ground sinyal. Solusi yang terbukti di diyAudio: catu BT lewat **DC-DC terisolasi** atau regulator + filter sendiri, **ground bintang**, kapasitor bypass tepat di pin 5 V/GND modul, atau trafo isolasi audio [T][R33][R34][R35]. *Ground loop isolator* murah bisa menghilangkan dengung tetapi dilaporkan mengurangi bass [T][R33]. Lihat 8.6.

### 5.4 DSP

| DSP | I/O | Catu | Fitur | Pemrograman | Harga [E] |
|---|---|---|---|---|---|
| **Wondom APM2 (AA-AP23122)**, ADAU1701 | 2 in / 4 out analog; ADC/DAC 24-bit 48 kHz; DR 98,5 dB [T][R19] | **5 V USB-C** [T][R19] | Apa pun yang bisa dibuat di SigmaStudio: crossover, PEQ, **limiter/compressor**, bass enhancement, delay. 4 potensiometer on-board [T][R19] | SigmaStudio via **ICP5** atau USBi; EEPROM self-boot | ±Rp400–600 rb + ICP5 ±Rp400–600 rb |
| ADAU1701 (chip) | 2 ADC (SNR 100 dB, THD+N −83 dB), 4 DAC (SNR 104 dB, THD+N −90 dB) [T][R20] | 3,3 V | 28/56-bit, 50 MIPS [T][R20] | SigmaStudio | – |
| **miniDSP 2x4 HD** | 2 in (analog/USB/TOSLINK), 4 out analog; maks. 2 Vrms [T][R23] | **12 V DC**, ±2,5 W; tidak bisa dicatu USB [T][R23] | 10 PEQ per input & output, crossover, delay s.d. 80 ms, **soft-limit compressor**, 2048 tap FIR [T][R23] | GUI miniDSP (Windows/macOS) | ±US$225–250 → ±Rp4–5,5 jt |
| Dayton Audio DSP-408 (ADAU1701) | 4 in / 8 out RCA; input maks. 3,2 V [T][R24] | **9–17 V** (adaptor 12 V/1,5 A) [T][R24] | PEQ 10 band/kanal; crossover LR/BW/Bessel s.d. 24 dB/okt; delay. **Limiter tidak tercantum** di spesifikasi [T][R24] | GUI Windows + opsi BT | US$199,98 [T][R24] |
| Arylic (ACPWorkbench) | Tertanam di board Up2Stream | – | EQ 10 band, virtual bass, noise suppressor, konfigurasi kanal [T][R25] | ACPWorkbench (Windows) | – |

### 5.5 Board all-in-one (BT + DSP + amp)

| Board | Isi | Catu | Daya (klaim) | Kelebihan | Kekurangan |
|---|---|---|---|---|---|
| **Wondom JAB5 (AA-JA33286)** | BT 5.0 **QCC3034** (aptX HD), **ADAU1701**, amp 4 kanal [T][R15][R16] | **10–39 V** [T][R15] | 4×100 W/6 Ω; 2.1: 2×100 W + 1×200 W; 2.0: 2×200 W/4 Ω [T][R15] | Paling ringkas; SigmaStudio; input line + I2S; bisa di-cascade [T][R15] | IC amp **tidak dipublikasikan resmi** (satu reseller menyebut "TDA749x") [V][R16]. Beban min. 6 Ω per kanal. Daya nyata @1% di 36 V ±70–87 W/kanal (6–8 Ω) [E]. SNR 97 dB [T][R15] |
| Wondom JAB3+ (AA-JA32173) | BT 5.0 aptX HD + ADAU1701, 2×50 W/4 Ω [T][R18] | [V] | 2×50 W | Bisa dicatu baterai [R18] | Daya kecil |
| Wondom JAB4 (AA-JA33285) | **TPA3118** 4×30 W/8 Ω + ADAU1701 + BT 5.0 [T][R17] | [V] | 4×30 W | Cocok untuk 4-way aktif kecil | Daya kecil |
| Arylic Up2Stream Amp 2.1 | WiFi + BT 5.0 + DSP; 2×50 W + 100 W [T][R25] | [V] | 200 W | Streaming WiFi/AirPlay; LPF sub 50–200 Hz (default 110 Hz) [T][R25] | Daya kecil |
| ZK-TB21 | 2× TPA3116D2, BT 5.0, 2×50 W + 100 W | 12–24 V | 200 W (klaim) | Murah | Tidak ada DSP sejati (hanya tone control); daya jauh di bawah target |

### 5.6 Rekomendasi kombinasi terbaik

| Tujuan | Kombinasi |
|---|---|
| **Kualitas terbaik per rupiah (Menengah)** | ZK-QCC (QCC5125) → **APM2 ADAU1701** → 2× **ZK-3002** (BTL + PBTL) @48 V dari SMPS LRS-600-48 |
| **Kualitas tertinggi (High-end)** | QCC5125 (analog ES9023/PCM5102A, atau optik) → **miniDSP 2x4 HD** → **3e 260-2-29A** (satelit) + **ZK-3002 PBTL** (sub) @48 V dari SMPS HRP-600-48 |
| **Paling mudah/ringkas** | **Wondom JAB5** + SMPS **36 V** disetel ke ±35 V (margin di bawah 39 V). Target daya turun menjadi ±300–350 W |
| **Upgrade full-aktif 5 kanal** | Dayton DSP-408 (8 out) + amp ketiga untuk tweeter. Crossover pasif dihapus, tetapi limiter harus dicek dulu [V] |

---

## 6. Skema Wiring

### 6.1 Wiring daya (kedua varian)

```text
 STOP KONTAK PLN 220–230V berarde (L, N, PE)
     │  kabel power 3×0,75–1 mm² dengan arde
     ▼
 ┌──────────────────────────────────────────────────────┐
 │ INLET IEC C14 3-in-1: saklar + fuse T6,3A 250V        │ ← panel belakang
 └───┬──────────────┬───────────────┬────────────────────┘
     L              N               PE ──────────────► baut chassis/panel logam
     │  kabel AC 0,75–1 mm² 300/500V, terminal tertutup     (ring terminal bergerigi, cat dikerok)
     ├──────────────────────────────────┐                 └─► terminal FG (⏚) kedua SMPS
     ▼                                  ▼
 ┌────────────────────────────┐   ┌──────────────────────────┐
 │ SMPS 48V                   │   │ SMPS 12V (LRS-35-12)     │
 │ Menengah: LRS-600-48       │   │ 12V 3A, set 12,0V        │
 │  (saklar input → 230V!)    │   └──────┬─────────────┬─────┘
 │ High-end: HRP-600-48       │        +12V           −V ──────────────┐
 │ V.ADJ set 48,0V (maks 50V) │          │                             │
 └────┬───────────────┬───────┘       [F5 1A]─► miniDSP (High-end)    │
    +V 48V          −V (0V)            │     / buck 12→5V → APM2 (Menengah)
      │ 14 AWG        │ 14 AWG        [F6 0,5A]─► ZK-QCC (8–32V)      │
      ▼               ▼                [F7 1A]─► kipas + termostat,    │
 ═══ BUS+ 48V ═══  ═══ STAR GROUND (busbar di −V SMPS 48V) ◄──────────┘
      │       │         ▲      ▲                 ▲
    [F2]    [F3]        │      │                 └── chassis (satu titik; lihat 8.6)
  MINI 58V MINI 58V     │      │
    15A     15A         │      │
      │14AWG  │14AWG    │      │
 ┌────────┐ ┌────────┐  │      │
 │AMP #1  │ │AMP #2  │  │      │
 │satelit │ │sub PBTL│  │      │
 │≈5,9A   │ │≈6,0A   │  │      │
 └┬─┬──┬──┘ └┬─┬──┬──┘  │      │
  │ │  └GND──┼─┼──┴─────┘      │   (tiap modul punya kabel GND SENDIRI ke star)
  │ │        │ │               │
 L± R±     SUB±   ← output BTL/PBTL: KEDUA terminal "hidup", JANGAN ke GND/chassis
```

**Perhitungan fuse dan kabel [E]:**
- **Fuse inlet T6,3 A slow-blow 250 V.** Melindungi kabel AC dan menahan arus inrush saat SMPS dinyalakan. Cek arus input maksimum dan inrush di datasheet SMPS **[V]**.
- **SMPS → busbar 14 AWG.** Arus maks. 11,9 A; 14 AWG dirating 32 A *chassis* [T][R57]. SMPS punya proteksi hubung singkat/beban lebih sendiri [T][R61], jadi tidak perlu fuse utama DC.
- **F2/F3 15 A / 14 AWG.** Tiap amp maks. ±6,0 A kontinu. Fuse cabang tetap wajib agar satu board yang rusak tidak membakar kabelnya sebelum OCP SMPS bereaksi.
- **Fuse wajib dirating tegangan DC ≥ tegangan sistem.** Fuse blade mobil standar umumnya dirating 32 V DC. Untuk bus 48 V pakai seri **58 V** (Littelfuse MINI 58 V / MAXI 58 V) [T][R58].

### 6.2 Perbedaan wiring antarvarian

| Bagian | Varian Menengah | Varian High-end |
|---|---|---|
| SMPS 48 V | LRS-600-48, **set saklar input ke 230 V** sebelum colok pertama [T][R61] | HRP-600-48, input otomatis 85–264 VAC [T][R62] |
| Rail 12 V | LRS-35-12 → buck 12→5 V 3 A + LC → APM2 (USB-C 5 V); ZK-QCC langsung 12 V | LRS-35-12 → miniDSP 2x4 HD (12 V) dan ZK-QCC (12 V) |
| Amp | 2× ZK-3002 (BTL + PBTL) | 3e 260-2-29A (satelit) + ZK-3002 PBTL (sub) |

### 6.3 Tabel koneksi antar-modul: Varian High-end

| # | Dari (modul, konektor/pin) | Ke (modul, konektor/pin) | Sinyal / level | Kabel | Catatan |
|---|---|---|---|---|---|
| 0 | Inlet IEC L / N / PE | SMPS 48 V & SMPS 12 V (L / N / FG) + baut chassis | 230 V AC; PE = arde | Kabel AC 0,75–1 mm²; PE hijau-kuning | Terminal AC ditutup; lihat 8.2 |
| 1 | SMPS 48 V **+V** | BUS+ busbar | 48,0 V DC | 14 AWG | Setel V.ADJ ke 48,0 V sebelum amp disambung |
| 2 | SMPS 48 V **−V** | Star ground busbar | 0 V | 14 AWG | Satu-satunya titik 0 V utama |
| 3 | BUS+ → F2 15 A | 3e 260-2-29A VIN+ | 36–51 V [T][R12] | 14 AWG | GND board → star (14 AWG) |
| 4 | BUS+ → F3 15 A | ZK-3002 VIN+ | 18–50 V [T][R13] | 14 AWG | Mode PBTL: set jumper/switch sesuai manual [V] |
| 5 | SMPS 12 V **−V** | Star ground busbar | 0 V | 18–20 AWG | – |
| 6 | SMPS 12 V **+V** → F5 1 A | miniDSP 2x4 HD DC in | 12 V, ±0,21 A [T][R23] | 20 AWG + jack DC | Polaritas jack **[V]** (cek manual) |
| 7 | SMPS 12 V **+V** → F6 0,5 A | ZK-QCC P3 (power) | 8–32 V [T][R31] | 22 AWG | Tambah LC 10 µH + 470 µF di pin |
| 8 | ZK-QCC P1 **LGL / LGR / GND** [T][R31] | miniDSP IN1 (L) / IN2 (R), RCA | Analog ±2,1 Vrms (PCM5102A) [E] | Kabel RCA berpelindung ≤30 cm | Jumper input miniDSP ke rentang lebih tinggi bila ada [V] |
| 8b | (Opsi) FYF QCC5125 optik out | miniDSP TOSLINK in | S/PDIF ≤192k/24 [T][R32] | Kabel optik | Jalur full-digital |
| 9 | miniDSP **OUT1** | 3e 260-2-29A input L (RCA) | Maks. 2 Vrms [T][R23]; board jenuh di 1,4 Vrms RCA [T][R12] | RCA | Batasi output DSP ≤ −3 dB (lihat 11.4) |
| 10 | miniDSP **OUT2** | 3e 260-2-29A input R (RCA) | idem | RCA | – |
| 11 | miniDSP **OUT3** | ZK-3002 input (kanal yang dipakai PBTL) | ≤2 Vrms | RCA | Kanal input PBTL mengikuti manual board [V] |
| 12 | miniDSP OUT4 | (cadangan) | – | – | Bisa untuk sub kedua atau output line |
| 13 | 3e OUT **L+ / L−** | Crossover pasif L (input +/−) | ≤ ±30 Vrms | 16 AWG | **L− bukan ground** |
| 14 | 3e OUT **R+ / R−** | Crossover pasif R | idem | 16 AWG | – |
| 15 | ZK-3002 PBTL **OUT+ / OUT−** | RSS265HO-4 (+/−) | ≤ ±32 Vrms | 14 AWG | Terminal output PBTL sesuai silkscreen [V] |
| 16 | Crossover L: W+/W−, T+/T− | SB17NRX2C35-8 L, SB26STCN L | – | 16/18 AWG | Polaritas tweeter mengikuti simulasi (LR2 → tweeter dibalik) |
| 17 | SMPS 12 V → F7 1 A → kipas 12 V + termostat 45 °C | Heatsink amp | 12 V ±0,2 A | 22 AWG | – |

### 6.4 Tabel koneksi antar-modul: Varian Menengah

| # | Dari | Ke | Sinyal / level | Catatan |
|---|---|---|---|---|
| 1 | ZK-QCC P1 LGL/LGR/GND | APM2 ADC IN L/R (lewat APM3 atau header 10-pin) [T][R19] | Analog ±2 Vrms | Konektor APM2/APM3 sesuai datasheet [V] |
| 2 | APM2 DAC OUT0/OUT1 | ZK-3002 #1 IN L/R | DAC ADAU1701 ±0,9 Vrms FS [V] | Gain ZK-3002 disetel ±30–32 dB (lihat 11.4) |
| 3 | APM2 DAC OUT2 | ZK-3002 #2 IN (PBTL) | idem | – |
| 4 | APM2 DAC OUT3 | cadangan / line out | – | – |
| 5 | ICP5 | APM2 **J11** (PH 6-pin 2 mm) [T][R19] | I2C pemrograman | Lepas setelah program ditulis ke EEPROM |
| 6 | SMPS 12 V → buck 12→5 V | APM2 **J2** USB-C 5 V [T][R19] | 5 V | Beri filter LC |
| 7 | SMPS 12 V | ZK-QCC P3 | 8–32 V [T][R31] | Fuse 0,5 A + LC |
| 8 | SMPS 48 V (BUS+) | ZK-3002 #1 & #2 VIN | 48,0 V | 14 AWG, fuse 58 V 15 A masing-masing |

---

## 7. Driver & Enclosure

### 7.1 Parameter driver (data pabrikan)

| Driver | Peran | Z | Re | Fs | Qts | Vas | Xmax | Sens. (2,83 V/1 m) | RMS | Sumber |
|---|---|---|---|---|---|---|---|---|---|---|
| **Dayton RSS265HO-4** (10") | Sub High-end | 4 Ω | 3,5 Ω | 26,9 Hz | 0,35 | 29,4 L | 12,3 mm | 87,2 dB | 600 W | [T][R39] |
| **Dayton RSS210HO-4** (8") | Sub Menengah | 4 Ω | 3,6 Ω | 29,6 Hz | 0,40 | 18,7 L | 11 mm | 85,7 dB | 300 W | [T][R38] |
| Dayton DCS205-4 (8") | Sub hemat | 4 Ω | – | 32,3 Hz | 0,37 | 27 L | 8,8 mm | 88,6 dB | 150 W | [T][R40] |
| **SB Acoustics SB17NRX2C35-8** (6,5") | Woofer satelit High-end | 8 Ω | 5,7 Ω | 36,5 Hz | 0,42 | 27 L | ±5,5 mm (coil 16 mm − gap 5 mm)/2 | 87 dB | 50 W (IEC) | [T][R43] |
| Dayton RS180-8 (7") | Alternatif woofer High-end | 8 Ω | 6,4 Ω | 35,7 Hz | 0,31 | 24,4 L | 6 mm | 87,1 dB | 60 W | [T][R37] |
| **Dayton DC160-8** (6,5") | Woofer satelit Menengah | 8 Ω | 6,6 Ω | 35,7 Hz | 0,34 | 17,9 L | 3,15 mm | 86,1 dB | 50 W | [T][R41] |
| **SB Acoustics SB26STCN-C000-4** | Tweeter High-end | 4 Ω | 3,2 Ω | 960 Hz | – | – | – | 92,5 dB | 120 W maks. | [T][R44] (crossover rekomendasi ≥2,6 kHz/12 dB) |
| **Dayton DC28FS-8** | Tweeter Menengah | 8 Ω | – | 813 Hz | – | – | – | 89 dB (1 W/1 m) | 50 W RMS | [T][R42] (crossover ≥1,8 kHz) |

**Kecocokan impedansi dengan amp:**
- **Satelit 8 Ω + TPA3255 BTL.** Di 48 V menghasilkan ±125 W per kanal [E], cukup untuk woofer 50–60 W RMS plus headroom transien. Dengan 8 Ω arus lebih kecil, amp lebih dingin, dan batas 53,5 V (R_L ≥6 Ω) berlaku [T][R2].
- **Sub 4 Ω + TPA3255 PBTL.** ±254 W [E]. Untuk RSS210HO-4 (300 W) aman tanpa limiter thermal; untuk DCS205-4 (150 W) **wajib limiter** (lihat 11.4). Sub DVC 2×4 Ω (mis. RSS265HO-44) bisa diparalel menjadi 2 Ω untuk ±436 W di 48 V, tetapi arus dan panas naik.
- **JAB5:** minimal 6 Ω per kanal [T][R15], jadi pakai woofer 8 Ω.

**Merek lokal (ACR, Black Spider, Audax lokal):** banyak driver lokal dirancang untuk *sound system*/PA dan mobil: sensitivitas tinggi, Qts tinggi, Xmax kecil, dan data T/S sering tidak lengkap. Contoh data resmi **ACR 10" 25H100SUWPP Curve**: Fs 45 Hz, **Qts 1,24**, Vas 83,5 L, **Xmax 2,8 mm**, 90 dB, "300 W" maks. [T][R45]. Qts setinggi itu cocok untuk open-baffle/box sangat besar, bukan sub box kecil yang di-EQ. Jadi untuk sub portabel, pilih driver dengan **Qts 0,3–0,45 dan Xmax ≥8 mm**. Driver lokal masih bisa dipakai untuk satelit PA, asalkan T/S-nya diukur sendiri (REW + jig impedansi atau DATS) [V].

### 7.2 Sealed vs ported

| Aspek | Sealed (tertutup) | Ported (bass reflex) | Passive radiator |
|---|---|---|---|
| Ukuran untuk F3 yang sama | Lebih besar bila tanpa EQ, **kecil bila di-EQ** | Lebih kecil/efisien di sekitar Fb | Kecil |
| Efisiensi di sekitar Fb | Rendah | +3–6 dB di sekitar Fb | Mirip port |
| Respons transien / group delay | Terbaik | Lebih lambat di sekitar Fb | Mirip port |
| Proteksi di bawah Fb | Driver tetap "terkontrol" | Driver bebas bergerak, **wajib HPF subsonik** | Wajib HPF |
| Noise port (chuffing) | Tidak ada | Ada bila port kecil | Tidak ada |
| Toleransi salah hitung | Tinggi | Rendah (harus pas di WinISD) | Sedang |
| Cocok dengan amp 250 W + DSP | **Sangat cocok** (Linkwitz transform) | Cocok bila box cukup besar | Cocok, biaya tambah |

**Rekomendasi:** satelit **sealed** karena HPF 90 Hz ada di DSP. Sub **sealed + EQ** untuk kabinet kompak, atau **ported** bila ruang box ≥25–30 L dan port bisa panjang (verifikasi di WinISD).

### 7.3 Menghitung volume box sealed

Rumus (Thiele/Small, box tertutup):

$$V_b = \frac{V_{as}}{(Q_{tc}/Q_{ts})^2 - 1} \qquad f_c = F_s \cdot \frac{Q_{tc}}{Q_{ts}} \qquad Q_{tc} = Q_{ts}\sqrt{\frac{V_{as}}{V_b}+1}$$

| Driver | Vb untuk Qtc 0,707 | fc | Vb untuk Qtc 0,6 | fc | Usulan praktis [E] |
|---|---|---|---|---|---|
| RSS265HO-4 | 9,5 L | 54 Hz | 15,2 L | 46 Hz | **15 L bersih** → Qtc 0,60, fc 46 Hz; + Linkwitz transform ke ±30 Hz |
| RSS210HO-4 | 8,8 L | 52 Hz | 15,0 L | 44 Hz | **12–15 L** |
| DCS205-4 | 10,2 L | 62 Hz | 16,6 L | 52 Hz | 12 L → Qtc 0,67, fc 58 Hz |
| SB17NRX2C35-8 | 14,7 L | 61 Hz | 25,9 L | 52 Hz | **10 L** → Qtc 0,81, fc 70 Hz (aman karena HPF 90 Hz) |
| DC160-8 | 5,4 L | 74 Hz | 8,5 L | 63 Hz | **6 L** → Qtc 0,68, fc 71 Hz |
| RS180-8 | 5,8 L | 81 Hz | 8,9 L | 69 Hz | 6 L → Qtc 0,70, fc 80 Hz |

"Vb bersih" = volume dalam dikurangi volume driver, bracing, dan port. Tambahkan ±10–15% bila box diisi damping (damping membuat box "terasa" lebih besar).

### 7.4 Menghitung port (bila ported)

$$L_v\,[cm] = \frac{23562{,}5 \cdot D_v^2 \cdot N_p}{F_b^2 \cdot V_b} - k \cdot D_v$$

dengan Dv = diameter port (cm), Vb (liter), Fb (Hz), Np = jumlah port, k = 0,732 (satu ujung flanged), 0,85 (dua ujung flanged), 0,614 (dua ujung bebas) [T][R46].

Contoh [E]: RSS265HO-4, Vb 30 L, Fb 32 Hz, port Ø7,5 cm, 1 buah → **Lv ≈ 37,7 cm**. Untuk 250 W di 32 Hz, port Ø7,5 cm kemungkinan besar terlalu kecil (kecepatan udara tinggi, terdengar "chuffing"). Cek grafik *Air velocity* di WinISD dengan target ≤17 m/s. Port yang lebih besar membuat port sangat panjang, jadi pertimbangkan **slot port di sudut** atau **passive radiator**. Alasan ini juga yang membuat sealed + EQ menarik untuk boombox.

**Software:**
- **WinISD** (gratis) [R47]: masukkan T/S driver, pilih sealed/vented, lalu lihat *Transfer function*, *Cone excursion* (harus < Xmax pada daya maksimum), *Air velocity*, dan *Group delay*. Tambahkan filter di tab *Filters* (HPF subsonik, Linkwitz transform) supaya simulasi mengikuti DSP.
- **VituixCAD** (gratis) [R48]: simulasi crossover pasif satelit (butuh file FRD/ZMA dari pabrikan atau hasil ukur), *Enclosure tool* untuk box, dan *Diffraction tool* untuk baffle step.

### 7.5 Material, bracing, damping

| Item | Rekomendasi |
|---|---|
| Material | **Multiplek (plywood) 15–18 mm** lebih ringan dan tahan benturan/kelembapan, cocok untuk portabel. **MDF 18 mm** lebih "mati" secara akustik tetapi berat dan menyerap air. Kombinasi yang bagus: baffle MDF 18 mm + badan multiplek 15 mm |
| Sambungan | Lem kayu PVAc + sekrup/dowel. Semua sambungan box sub **wajib kedap udara** (silikon di sisi dalam) |
| Bracing | Window brace/dowel Ø20–25 mm setiap ±20–25 cm panel bebas. Brace dari baffle ke panel belakang di box sub |
| Sekat | Ruang elektronik **terpisah** dari ruang sub (sealed), dan ruang satelit terpisah dari ruang sub (tekanan sub memodulasi cone woofer satelit) |
| Damping | Satelit sealed: isi 50–100% volume dengan dakron/polyfill longgar. Sub sealed: 50–100% polyfill. Sub ported: lapisi dinding saja (foam/felt 2–3 cm), jangan tutup mulut port |
| Gasket | Gasket foam di flange driver dan terminal |
| Elektronik | Panel belakang aluminium 3 mm sebagai "plate amp": heatsink amp menempel di panel dengan sirip di luar; SMPS, inlet AC, dan kipas di ruang elektronik yang punya ventilasi. Panel logam wajib diarde (8.2) |
| Grill & handle | Grill besi berlubang; handle recessed; roda + handle koper bila berat >15 kg |

### 7.6 Crossover pasif satelit: nilai awal [E]

Linkwitz-Riley orde-2 (LR2) memakai rumus L = R/(π·f) dan C = 1/(4π·f·R). Polaritas tweeter **dibalik** pada LR2.

| Varian | Woofer (seri L / paralel C) | Tweeter (seri C / paralel L) | L-pad tweeter | Zobel woofer |
|---|---|---|---|---|
| Menengah: DC160-8 + DC28FS-8 @2,5 kHz | 1,0 mH / 4,0 µF | 4,0 µF / 1,0 mH | −3 dB pada 8 Ω: Rs 2,3 Ω, Rp 19 Ω | Le DC160 2,26 mH besar: Rz 8,2 Ω + Cz 33 µF (Rz = 1,25·Re, Cz = Le/Rz²) |
| High-end: SB17NRX2C35-8 + SB26STCN-C000-4 @2,8 kHz | 0,91 mH / 3,6 µF | 7,1 µF / 0,45 mH (Z tweeter 4 Ω) | −5,5 dB pada 4 Ω: Rs 1,9 Ω, Rp 4,5 Ω | Le SB17 0,15 mH kecil, biasanya tidak perlu |

**Peringatan:** nilai di atas menganggap driver sebagai resistor murni. Impedansi nyata naik dengan frekuensi dan di sekitar Fs tweeter, dan respons akustik dipengaruhi baffle step serta offset akustik. Anggap ini **titik awal**, lalu optimasi di VituixCAD dengan file FRD/ZMA dan verifikasi dengan pengukuran REW (bagian 11). Koreksi *baffle step* sebaiknya dilakukan di DSP (low-shelf pada kanal satelit), bukan di crossover pasif.

---

## 8. Catu Daya AC/DC & Proteksi

### 8.1 Pemilihan SMPS

| Opsi | Kelebihan | Kekurangan | Status |
|---|---|---|---|
| **SMPS bermerek 48 V (Mean Well LRS/HRP)** | Tegangan teregulasi 48,0 V, ringan, efisiensi 92% [T][R61], proteksi hubung singkat/beban lebih/tegangan lebih/suhu [T][R61] | Kipas bisa berbunyi saat beban tinggi | **Rekomendasi** |
| Trafo toroid + penyearah + kapasitor (linear) | Tidak ada derau switching | Berat (±5–7 kg untuk 500 W), tegangan **tidak teregulasi**: naik saat beban kecil dan saat PLN tinggi, bisa melewati batas 50–51 V board TPA3255 [E] | Tidak disarankan untuk TPA3255 |
| SMPS "jaring"/generik tanpa merek 48 V | Murah | Daya sering tidak sesuai klaim, ripple dan proteksi tidak jelas, risiko panas **[V]** | Hindari |

**Setelan wajib:**
1. **LRS-600-48:** saklar pilih input di posisi **230 V** sebelum dicolok pertama kali [T][R61]. Salah posisi (115 V) di listrik PLN bisa langsung merusak SMPS.
2. Tanpa beban, setel trimpot **V.ADJ** sampai **48,0 V** di multimeter. Rentang LRS-600-48 45,6–52,8 V [T][R61], jadi batas atas trimpot **melebihi** batas board amp.
3. Beli dari distributor resmi Mean Well; di marketplace banyak unit tiruan **[V]**.

### 8.2 Sisi AC: inlet, fuse, saklar, arde

- **Inlet IEC C14 3-in-1** (soket + saklar + dudukan fuse), rating 10 A 250 V, di panel belakang.
- **Fuse inlet T6,3 A slow-blow 250 V** [E][V].
- **Arde (PE) wajib:** pin arde inlet → baut chassis/panel logam (ring terminal + ring bergerigi, cat dikerok) → terminal FG (⏚) kedua SMPS. Karena ada 230 V di dalam kabinet, chassis logam yang tidak diarde bisa bertegangan bila kabel AC lepas.
- **Kabel AC internal:** 0,75–1 mm² 300/500 V, sepatu kabel berinsulasi, terminal AC SMPS ditutup (cover bawaan atau heat-shrink), kabel dijepit ke panel, dan jalurnya dipisah dari kabel sinyal/RCA.
- **Stop kontak rumah berarde.** ELCB/RCD 30 mA di panel listrik rumah sangat disarankan.

### 8.3 Fuse DC dan ukuran kabel

**Ampacity kabel tembaga (PowerStream)** [T][R57]:

| AWG | Ø (mm) | Ω/km | Maks. A *chassis wiring* | Dipakai untuk |
|---|---|---|---|---|
| 12 | 2,05 | 5,21 | 41 | Opsional SMPS → busbar (margin besar) |
| **14** | 1,63 | 8,28 | 32 | SMPS → busbar, bus → amp, kabel sub |
| 16 | 1,29 | 13,17 | 22 | Kabel satelit |
| 18 | 1,02 | 20,94 | 16 | Tweeter |
| 20 | 0,81 | 33,29 | 11 | 12 V DSP/BT, kipas |

**Aturan fuse:** fuse melindungi **kabel**. Nilainya ≥1,25× arus kontinu maksimum dan ≤ ampacity kabel. Semua fuse DC harus **berating DC ≥ tegangan maksimum sistem** (bus 48 V → seri 58 V [T][R58]).

### 8.4 Soft-start dan anti-pop

| Masalah | Penyebab | Solusi |
|---|---|---|
| Lonjakan arus saat saklar dinyalakan | Inrush ke kapasitor input SMPS | Normal; dibatasi rangkaian inrush SMPS. Pakai fuse inlet **slow-blow** |
| "Pop" saat nyala | DSP/BT boot lebih lambat dari amp; DAC mengeluarkan transien | Nyalakan DSP/BT **±2–3 detik sebelum** amp (relay delay-on 12 V yang menyambung VIN amp, atau pin mute/RESET board bila tersedia [V]). TPA3255 sendiri *click-and-pop free* [T][R2] |
| "Pop" saat mati | Rail 12 V dan 48 V turun dengan kecepatan berbeda | Matikan amp dulu (saklar 2 tahap) atau relay delay-off |
| Dengung saat laptop tersambung USB (tuning) | Ground loop lewat charger laptop dan arde speaker | Tuning dengan laptop memakai baterai, atau pakai isolator USB |

Datasheet TPA3255 menyatakan urutan catu tidak kritis berkat power-on-reset internal, tetapi menyarankan **RESET dilepas setelah catu stabil** agar artefak nyala minimal [T][R2].

### 8.5 Proteksi speaker dan DC

- **TPA3255** punya proteksi *undervoltage*, *overtemperature*, *clipping*, *short circuit* dengan pelaporan error (FAULT, CLIP_OTW) [T][R2]. **TPA3221** punya proteksi DC speaker bawaan [T][R5].
- **Modul proteksi speaker relay klasik** (mis. berbasis µPC1237) dirancang untuk amp *single-ended* yang output-nya berreferensi ground. **Output BTL/PBTL keduanya "hidup" (bias ±PVDD/2)**, jadi modul semacam itu umumnya **tidak cocok** tanpa modifikasi [E/V]. Andalkan proteksi internal chip, **fuse speaker**/polyswitch untuk tweeter (opsional), dan terutama **limiter DSP**.
- **HPF subsonik** (±25 Hz, BW2) di kanal sub melindungi driver dari ekskursi berlebih, wajib untuk box ported.
- **Kapasitor seri tweeter** di crossover pasif sudah melindungi tweeter dari DC dan bass.

### 8.6 Grounding bintang dan pengendalian noise

1. **Satu titik 0 V (star)**: busbar di terminal −V SMPS 48 V. −V SMPS 12 V juga ke titik ini.
2. **Kabel GND terpisah** dari setiap modul ke star. Jangan meng-*daisy-chain* GND amp → DSP → BT.
3. **Arus besar tidak lewat ground sinyal.** Ground RCA (DSP ↔ amp) hanya membawa referensi sinyal. Kalau muncul dengung, coba putus shield di satu sisi (*ground lift*) atau pakai input balanced (3e board punya XLR) [T][R12].
4. **Catu BT/DSP** dari SMPS 12 V terpisah + filter LC (10–22 µH + 470–1000 µF low-ESR) di dekat modul [T][R33][R34].
5. **Pisahkan fisik**: modul BT + antena jauh dari SMPS dan induktor output amp (≥10–15 cm). Antena keluar dari kotak logam.
6. **Twist** pasangan kabel +/− daya dan speaker untuk mengurangi loop area/EMI.
7. **Chassis (sudah diarde) ke star di satu titik saja.** Bila muncul dengung saat speaker disambung ke perangkat lain yang juga berarde (TV, PC), sambungan chassis–star boleh lewat resistor 10 Ω 1 W paralel kapasitor 100 nF (*ground-lift*) [E]. **Kabel PE ke chassis tidak boleh diputus.**

### 8.7 Manajemen panas [E]

$$P_{loss} \approx P_{out}\left(\frac{1}{\eta}-1\right) + P_{idle}$$

- Sinus penuh: sub 254 W @η 0,88 → **±35 W** panas; satelit 2×125 W → ±34 W; SMPS (η 0,92 [T][R61]) → ±50 W. Uji sinus penuh bisa memicu OTP; Archimago mencatat proteksi suhu/arus TPA3255 aktif saat uji intensif, pulih setelah power cycle [T][R8].
- Musik keras (1/8 daya): ±4–6 W per board + idle ±2,5 W per chip [T][R2], SMPS ±7 W. Heatsink bawaan cukup **asal ada aliran udara**.
- Target: heatsink ≤60–65 °C di ruang 35 °C. Pasang **kipas 12 V + termostat** (nyala ≥45 °C), lubang intake bawah dan exhaust atas. SMPS diletakkan di ruang elektronik dekat exhaust, lubang kipasnya jangan tertutup; jangan taruh amp atau SMPS di ruang sub yang tertutup rapat.

---

## 9. BOM: Dua Varian

Harga **[E]**, per September 2026, rentang dari penjual lokal/impor. **Tanpa baterai, BMS, charger, atau boost.** Belum termasuk alat (solder, multimeter) dan ongkir besar. Harga Tokopedia berubah cepat, jadi cek ulang sebelum membeli.

### 9.1 Varian Menengah (SMPS LRS-600-48, ADAU1701, 2× ZK-3002)

| # | Item | Qty | Harga (Rp ribu) | Sumber harga |
|---|---|---|---|---|
| 1 | Modul BT ZK-QCC (QCC3034/QCC5125) + PCM5102A, 8–32 V | 1 | 400–700 | [E] AliExpress/Tokopedia |
| 2 | Wondom APM2 AA-AP23122 (ADAU1701) | 1 | 400–600 | [E] |
| 3 | Wondom ICP5 programmer | 1 | 400–600 | [E] |
| 4 | Amp ZK-3002 TPA3255 | 2 | 1.200–1.600 | Tokopedia ±Rp602 rb/pcs [R14] |
| 5 | **SMPS Mean Well LRS-600-48** (48 V 12,5 A) | 1 | 1.100–1.300 | US$59,90 [R61] |
| 6 | SMPS Mean Well LRS-35-12 (12 V 3 A) | 1 | 150–250 | [E][V] |
| 7 | Buck 12→5 V 3 A + filter LC (untuk APM2) | 1 | 50–100 | [E] |
| 8 | Inlet IEC C14 (saklar + fuse T6,3 A), kabel power berarde, cover terminal AC | 1 set | 100–200 | [E] |
| 9 | Fuse DC 58 V (MINI 15 A ×2, kecil ×3) + holder | 1 set | 100–200 | [E] [R58] |
| 10 | Kabel 14/16/18/20 AWG, kabel AC 0,75–1 mm², terminal, RCA | 1 set | 150–300 | [E] |
| 11 | Relay delay-on 12 V, LED power, knob volume (opsional pot ke APM2) | 1 set | 80–180 | [E] |
| 12 | Kipas 12 V + termostat, pasta termal | 1 set | 50–150 | [E] |
| 13 | Woofer Dayton DC160-8 | 2 | 1.000–1.300 | [E] impor |
| 14 | Tweeter Dayton DC28FS-8 | 2 | 700–950 | [E] impor |
| 15 | Subwoofer Dayton RSS210HO-4 | 1 | 2.000–2.600 | [E] impor |
| 16 | Komponen crossover pasif (induktor air-core, kapasitor MKP, resistor) | 2 set | 300–600 | [E] |
| 17 | Kabinet MDF/multiplek 18 mm (potong CNC/jasa), lem, cat/tolex | 1 | 700–1.200 | [E] |
| 18 | Damping, gasket, terminal, grill, handle | 1 set | 300–500 | [E] |
| | **TOTAL Varian Menengah** | | **≈ Rp9,2 – 13,3 jt** (tipikal ±Rp11 jt) | [E] |
| | *Opsi hemat:* sub DCS205-4 (−Rp0,9–1,1 jt), SMPS LRS-350-48 + limiter ketat (−Rp0,4–0,6 jt), JAB5 + SMPS 36 V menggantikan item 1–4 (−Rp1,5 jt, daya turun) | | *≈ Rp6,4–10 jt* | |

### 9.2 Varian High-end (SMPS HRP-600-48, miniDSP 2x4 HD, 3e PFFB + ZK-3002)

| # | Item | Qty | Harga (Rp ribu) | Sumber harga |
|---|---|---|---|---|
| 1 | Modul BT QCC5125 (LDAC/aptX HD) + DAC (ES9023/PCM5102A) atau board optik FYF | 1 | 450–900 | €32,90 [R30] / US$39–50 [R32] |
| 2 | **miniDSP 2x4 HD** | 1 | 4.000–5.500 | [E] (±US$225–250) |
| 3 | **3e Audio 260-2-29A** (2× TPA3255 PFFB) | 1 | 2.800–3.300 | €149 [R12] |
| 4 | ZK-3002 (PBTL untuk sub) | 1 | 600–800 | [R14] |
| 5 | **SMPS Mean Well HRP-600-48** (48 V 13 A, PFC aktif) | 1 | 2.600–3.000 | US$138,30 [R62] |
| 6 | SMPS Mean Well LRS-35-12 (12 V 3 A) | 1 | 150–250 | [E][V] |
| 7 | Inlet IEC C14 (saklar + fuse T6,3 A), kabel power berarde, cover terminal AC | 1 set | 150–300 | [E] |
| 8 | Fuse DC 58 V (MINI 15 A ×2, 1 A, 0,5 A) + holder | 1 set | 150–300 | [E] [R58] |
| 9 | Kabel 14/16/18/20 AWG, kabel AC 0,75–1 mm², RCA berpelindung, terminal | 1 set | 200–400 | [E] |
| 10 | Relay delay-on 12 V, LED power, saklar | 1 set | 100–200 | [E] |
| 11 | Heatsink tambahan + kipas PWM + termostat | 1 set | 150–300 | [E] |
| 12 | Woofer **SB Acoustics SB17NRX2C35-8** | 2 | 2.000–2.600 | [E] impor |
| 13 | Tweeter **SB Acoustics SB26STCN-C000-4** | 2 | 1.400–1.900 | [E] impor |
| 14 | Subwoofer **Dayton RSS265HO-4** | 1 | 3.000–3.800 | [E] impor |
| 15 | Crossover pasif audio-grade (air-core, MKP) | 2 set | 600–1.200 | [E] |
| 16 | Kabinet multiplek birch 18 mm + bracing + finishing | 1 | 1.500–2.500 | [E] |
| 17 | Damping, gasket, terminal, grill logam, handle | 1 set | 400–800 | [E] |
| | **TOTAL Varian High-end** | | **≈ Rp20,3 – 28,1 jt** (tipikal ±Rp24 jt) | [E] |
| | *Alat ukur (tidak dihitung):* miniDSP **UMIK-1** | 1 | ±1.950 | Rp1,95 jt [R51] |

### 9.3 Memangkas biaya tanpa mengorbankan inti

- **Pertahankan:** chip TPA3255, SMPS bermerek dengan arde yang benar, fuse DC-rated, sub dengan Xmax besar.
- **Bisa diganti:** miniDSP menjadi APM2 (−Rp3,5–4,5 jt); 3e board menjadi ZK-3002 (−Rp2 jt); HRP-600-48 menjadi LRS-600-48 (−Rp1,5 jt, kehilangan PFC aktif); SB Acoustics menjadi Dayton Classic; multiplek birch menjadi multiplek biasa.
- **Jangan dihemat:** SMPS generik tanpa merek, inlet tanpa fuse/arde, fuse DC yang tidak berating DC, kabel yang lebih kecil dari tabel 8.3.

---

## 10. Perakitan

**Tahap 0: Persiapan**
1. Unduh semua datasheet/manual (TPA3255, ZK-3002/3e, APM2/miniDSP, ZK-QCC, SMPS Mean Well). Konfirmasi setiap tanda **[V]** di dokumen ini (pinout, jumper PBTL, polaritas jack DC).
2. Simulasikan box di WinISD dan crossover di VituixCAD. Kunci ukuran kabinet.

**Tahap 1: Panel daya AC (semua pekerjaan dengan steker DICABUT)**
1. **LRS-600-48:** pastikan saklar pilih input di posisi **230 V** [T][R61].
2. Pasang inlet IEC di panel belakang. Sambungkan L dan N ke terminal AC kedua SMPS. Sambungkan PE ke baut chassis dan terminal FG (⏚) kedua SMPS. Tutup semua terminal AC.
3. Uji dengan multimeter (steker masih dicabut): pin arde steker ↔ chassis **< 0,5 Ω** [E]; pin L dan N ↔ chassis harus **tidak tersambung** (open).
4. Colok pertama kali lewat **lampu seri** (bohlam pijar 60–100 W seri di kabel L) bila tersedia [E]. Lampu menyala terang terus berarti ada hubung singkat: cabut dan periksa.
5. Tanpa beban, setel V.ADJ SMPS 48 V ke **48,0 V** dan cek SMPS 12 V = 12,0 V.

**Tahap 2: Distribusi DC**
1. Pasang busbar BUS+ dan star ground di panel elektronik.
2. Pasang fuse cabang dan (Menengah) buck 12→5 V. **Setel output buck 5 V sebelum beban disambung.**

**Tahap 3: Uji daya bertahap (tanpa speaker)**
1. Hubungkan satu modul per satu. Untuk sambungan pertama tiap amp, boleh lewat power supply lab (limit arus 1 A) atau **resistor 10 Ω 10 W** seri sebagai pembatas arus.
2. Ukur arus idle tiap modul (TPA3255 idle ±2,5 W per chip [T][R2], jadi ±50 mA per chip di 48 V). Arus jauh lebih besar berarti ada salah wiring.

**Tahap 4: Jalur sinyal**
1. Sambungkan BT → DSP → amp dengan RCA pendek.
2. **Menengah:** program APM2 di SigmaStudio (template Wondom sebagai awal), tulis ke EEPROM, lepas ICP5.
3. **High-end:** konfigurasi miniDSP 2x4 HD (plugin 2x4 HD), simpan ke preset.
4. Setel gain amp **rendah dulu** (ZK-3002 ke 26 dB).

**Tahap 5: Speaker & kabinet**
1. Rakit crossover di papan MDF/PCB perfboard. Induktor saling tegak lurus dan berjarak ≥5 cm. Ikat dengan cable tie + lem panas.
2. Pasang driver dengan gasket. Kencangkan sekrup menyilang dan jangan terlalu kencang.
3. Uji kebocoran box sub: tekan cone perlahan; cone harus kembali pelan (sealed) dan tidak ada desis.
4. Pasang elektronik di ruang terpisah yang berventilasi.

**Tahap 6: Tuning** (bagian 11).

---

## 11. Tuning & Pengujian

### 11.1 Cek dengan multimeter (sebelum musik)

| Titik | Nilai yang diharapkan | Tindakan bila menyimpang |
|---|---|---|
| Kontinuitas arde: pin arde steker ↔ chassis (steker dicabut) | < 0,5 Ω [E] | Periksa baut/ring terminal PE |
| Tegangan bus SMPS 48 V | 48,0 ±0,3 V | Setel V.ADJ; **jangan >50 V** |
| Output SMPS 12 V / buck 5 V | 12,0 ±0,3 V / 5,1 ±0,1 V | Setel trimpot |
| **DC offset di terminal speaker** (tanpa sinyal, amp ON) | < ±50 mV (TPA3255: |Vos| khas 15 mV, maks. 60 mV [T][R2]) | >100 mV: jangan sambung speaker, cek board |
| Resistansi DC speaker (dari terminal crossover) | Satelit ±5,5–7 Ω; sub ±3,5 Ω [T][R39][R43] | 0 Ω = short; ∞ = putus |
| Daya idle dari PLN (colokan watt-meter) | ±15–20 W [E] | Jauh lebih besar = ada masalah |

### 11.2 Setelan DSP awal

| Kanal | Filter | PEQ/lainnya | Limiter |
|---|---|---|---|
| L/R satelit | HPF **LR4 90 Hz** | Low-shelf +3–4 dB di bawah ±400–600 Hz untuk baffle step (sesuaikan hasil ukur); PEQ ±3 band untuk puncak | Threshold dihitung di 11.4 |
| Sub | LPF **LR4 90 Hz**; HPF subsonik **BW2 22–25 Hz** | Sealed: **Linkwitz transform** (f0 = fc box, Q0 = Qtc) ke f 30 Hz, Q 0,6–0,7. Atau low-shelf +6 dB @40 Hz | Threshold dari Xmax/RMS driver |
| Semua | Input: mono sum (L+R)/2 untuk sub | Delay sub 0–3 ms, polaritas 0/180°: pilih yang paling rata di crossover | Master volume ≤0 dB |

**Bass boost dengan hati-hati:** setiap +3 dB bass = **2× daya** dan ±1,4× ekskursi; +6 dB = 4× daya. Cek grafik *Cone excursion* di WinISD dengan filter terpasang pada daya amp penuh. Excursion harus ≤ Xmax (RSS265HO-4 12,3 mm [T][R39]).

### 11.3 Pengukuran dengan REW + UMIK-1

1. Pasang **REW** (gratis) [R49]. Colok **UMIK-1** (USB) dan muat file kalibrasi sesuai nomor seri (*Preferences → Mic/Meter*). Pakai file on-axis (tanpa "_90deg") bila mic diarahkan ke speaker [T][R50].
2. Kirim sinyal uji: High-end lewat **USB audio miniDSP 2x4 HD** [T][R23]; Menengah lewat AUX/BT dari laptop (matikan efek audio OS).
3. Level uji ±75–80 dB SPL di mic [T][R50]. Sweep log (default 256k OK) [R50].
4. **Ukur tiap driver terpisah** (mute kanal lain di DSP): woofer dan tweeter pada jarak ±50 cm on-axis tweeter dengan **gating** ±4–6 ms untuk respons "anechoic semu" di atas ±300 Hz. Sub diukur **nearfield** (mic ±1 cm dari cone).
5. Gabungkan (*merge*) nearfield + gated farfield, ekspor FRD, impor ke VituixCAD, lalu optimasi crossover pasif.
6. Ukur respons total di posisi dengar. Rata-ratakan 5–9 titik (grid ±15–20 cm) untuk membedakan mode ruang dari masalah speaker [T][R50].
7. Cek sambungan sub–satelit: sweep L+Sub, lalu ubah delay/polaritas sampai tidak ada lubang di 70–120 Hz.
8. Terapkan PEQ: **potong puncak, jangan mengisi lembah sempit** (lembah biasanya dari ruang/pembatalan).

### 11.4 Menyetel gain dan limiter (paling penting untuk keandalan) [E]

**Gain amp** agar output DSP penuh menghasilkan daya maksimum amp:
- Target di satelit (8 Ω, 48 V): ±125 W → **31,6 Vrms**. Bila output DSP 0 dBFS = 0,9 Vrms, gain amp = 20·log(31,6/0,9) ≈ **31 dB**. Bila 2 Vrms (miniDSP), ≈ **24 dB**.
- 3e 260-2-29A jenuh di **1,4 Vrms** input RCA [T][R12], jadi batasi output miniDSP ≤1,4 Vrms (±−3 dB dari 2 Vrms).
- ZK-3002: gain 26–36 dB bisa disetel [T][R13].

**Limiter per kanal** dari rating thermal driver:
- Woofer SB17NRX2C35-8 50 W/8 Ω → V_limit = √(50×8) = **20 Vrms**. Threshold DSP = 20·log(20/31,6) ≈ **−4,0 dB** di bawah level clipping amp. Dengan tweeter di kanal yang sama, gunakan threshold ini untuk sinyal lebar pita (aman dan konservatif).
- Sub DCS205-4 150 W/4 Ω → **24,5 Vrms** (amp PBTL 48 V ±31,9 Vrms) → threshold ±**−2,3 dB**. RSS265HO-4 600 W, jadi limiter cukup mencegah clipping amp (−0,5 dB).

**Cara verifikasi di lapangan:**
1. Putar sinus 100 Hz (satelit) / 50 Hz (sub) dari DSP/REW.
2. Ukur Vrms di terminal speaker dengan **multimeter true-RMS** (frekuensi rendah agar di dalam bandwidth multimeter). Mulai dari volume kecil.
3. Naikkan sampai limiter bekerja. Nilai harus sesuai target di atas.
4. **Uji ini tidak boleh lama** (maks. beberapa detik di daya penuh) karena sinus kontinu jauh lebih berat dari musik.

### 11.5 Uji akhir

- Burn-in 1–2 jam musik keras. Pantau suhu heatsink (target <65 °C) dan suhu casing SMPS.
- Uji noise: telinga dekat tweeter tanpa sinyal, BT tersambung, lalu BT memutar hening. Hiss/dengung berarti kembali ke 8.6.
- Uji jangkauan BT dan dropout (antena keluar dari kotak logam).
- Ukur konsumsi listrik dengan colokan watt-meter (kWh meter plug-in) dan bandingkan dengan tabel 4.5.

### 11.6 Kesalahan umum

| Kesalahan | Akibat | Pencegahan |
|---|---|---|
| Trimpot V.ADJ SMPS 48 V diputar ke maksimum (52,8 V) | Melebihi batas ZK-3002 (50 V), 3e (51 V), TPA3255 4 Ω (51 V); chip rusak | Setel 48,0 V dengan multimeter sebelum amp disambung |
| LRS-600-48 dicolok ke PLN dengan saklar input di 115 V | SMPS rusak | Cek saklar di 230 V sebelum colok pertama |
| Chassis logam tidak diarde | Risiko tersetrum bila kabel AC lepas menyentuh chassis | PE ke chassis & FG SMPS, uji kontinuitas |
| Menyambung speaker "−" ke ground/chassis atau menyatukan "−" dua kanal | Short output BTL → proteksi/kerusakan | Output BTL/PBTL tetap floating |
| Salah wiring PBTL | Short antar half-bridge | Ikuti manual board; uji dengan fuse kecil |
| Fuse blade 32 V di sistem 48 V | Busur api saat fuse putus | Fuse berating DC 58 V [R58] |
| SMPS generik tanpa merek atau terlalu kecil | Suara putus saat bass panjang (OCP), panas, ripple | Mean Well 600 W asli (4.3) |
| Bass boost besar tanpa HPF subsonik | Driver menabrak (bottoming), amp clipping | HPF 22–25 Hz + limiter |
| Ground berantai, BT dekat amp/SMPS | Dengung, cuit BT | Star ground, catu BT terfilter/terisolasi |
| Menilai "300 W" dari listing | Ekspektasi salah (10% THD / 2 Ω) | Pakai rumus P = V²/2R dan datasheet 1% |
| Ruang elektronik di dalam box sub tertutup | Panas & kebocoran udara | Sekat terpisah + ventilasi |
| Laptop tuning dicolok ke charger | Ground loop saat pengukuran | Laptop pakai baterai |

---

## 12. Keselamatan

**Listrik PLN 220–230 V AC (risiko terbesar di proyek ini)**
- Tegangan PLN bisa mematikan. Kerjakan semua wiring dengan **steker dicabut**. Kapasitor input SMPS bisa menyimpan tegangan beberapa saat setelah dicabut; tunggu ≥1 menit sebelum menyentuh terminal AC [E]. **Jangan membuka casing SMPS.**
- **Chassis logam wajib diarde (PE)** dan diuji kontinuitasnya (bagian 10). Pakai stop kontak berarde; ELCB/RCD 30 mA di instalasi rumah sangat disarankan.
- Semua terminal AC tertutup, kabel AC dijepit (*strain relief*) di inlet, dilindungi grommet saat menembus panel, dan dipisah dari kabel DC/sinyal.
- Kabinet speaker bergetar kuat: kencangkan SMPS dengan baut + ring pegas dan periksa berkala.
- Jangan dioperasikan di tempat basah/hujan tanpa pelindung. Jangan tutup ventilasi SMPS.
- Bila belum yakin dengan wiring 230 V, minta teknisi listrik memeriksa sebelum dinyalakan pertama kali.

**Arus DC 48 V**
- 48 V masih di bawah batas SELV umum (60 V DC), tetapi arus hubung singkat SMPS 600 W cukup untuk memanaskan kabel dan memercikkan busur api. Karena itu fuse DC **harus berating DC** untuk tegangan sistem.
- Semua sambungan crimp dengan tang crimp yang benar, lalu uji tarik. Solder saja tidak cukup untuk sambungan arus tinggi yang bergetar.

**Pendengaran**
- 110+ dB SPL dalam jarak dekat dapat merusak pendengaran dalam hitungan menit. Batasi master volume dan jangan menaruh telinga dekat tweeter saat uji daya.

---

## 13. Sumber/Referensi

**Chip amplifier (datasheet/produsen)**
- [R1] Texas Instruments, TPA3255 product page: https://www.ti.com/product/TPA3255
- [R2] Texas Instruments, *TPA3255 315-W Stereo, 600-W Mono PurePath™ Ultra-HD Analog-Input Class-D Amplifier*, SLASEA8A (Rev. Okt 2016): https://www.ti.com/lit/ds/symlink/tpa3255.pdf
- [R3] Texas Instruments, TPA3251 (product & datasheet SLASE40D): https://www.ti.com/product/TPA3251 · https://www.ti.com/lit/ds/symlink/tpa3251.pdf
- [R4] Texas Instruments, TPA3116D2 (product & datasheet SLOS708G): https://www.ti.com/product/TPA3116D2 · https://www.ti.com/lit/ds/symlink/tpa3116d2.pdf
- [R5] Texas Instruments, TPA3221 datasheet (SLASEE9C, rev. Mei 2025): https://www.ti.com/lit/ds/symlink/tpa3221.pdf
- [R6] Texas Instruments, TAS5630B (product & datasheet SLES217D): https://www.ti.com/product/TAS5630B · https://www.ti.com/lit/ds/symlink/tas5630b.pdf
- [R7] Infineon, MA12070: https://www.infineon.com/part/MA12070 · datasheet: https://www.radiolocman.com/datasheet/pdf.html?di=165851

**Review/pengukuran independen**
- [R8] Archimago, *Part II: Fosi Audio V3 Mono Amp; Class D + PFFB, TI TPA3255* (2024): http://archimago.blogspot.com/2024/08/part-ii-fosi-audio-v3-mono-amp-class-d.html
- [R9] Audio Science Review, *Fosi Audio V3 Amplifier Review*: https://www.audiosciencereview.com/forum/index.php?threads/fosi-audio-v3-amplifier-review.45757/ (ringkasan: https://www.audiophonics.fr/en/blog-diy-audio/67-fosi-audio-v3-review-by-audiosciencereview.html)
- [R10] Archimago, *Part I: 3e Audio A5 Stereo and A7 Mono (TPA3251/3255, PFFB)* (2024): http://archimago.blogspot.com/2024/11/part-i-3e-audio-a5-stereo-and-a7-mono.html

**Board amplifier**
- [R11] 3e Audio, TPA3255-2CH-260W: https://www.3e-audio.com/amplifier-kits/tpa3255-2ch-260w/
- [R12] Audiophonics, 3E Audio 260-2-29A PFFB TPA3255: https://www.audiophonics.fr/en/amplifier-boards/3e-audio-pffb-balanced-class-d-amplifier-module-tpa3255-btl-2x260w-p-17252.html
- [R13] ZK-3002 TPA3255 (listing & spesifikasi): https://www.amazon.com/Single-Digital-Amplifier-Module-8%E2%80%9150VDC/dp/B0CKPLQL1Z · https://weenable.tech/sound-audio-modules/485-zk-3002-tpa3255-pure-rear-level-digital-power-amplifier-board-stereo-300wx-2-bridged-mono-600w.html · manual: https://manuals.plus/ae/1005005921176348
- [R14] Tokopedia, pencarian "TPA3255" (harga BDM8, ZK-3002, dll.): https://www.tokopedia.com/find/tpa3255

**Board all-in-one & DSP**
- [R15] Audiophonics, Wondom JAB5 AA-JA33286: https://www.audiophonics.fr/en/amplifier-boards/wondom-jab5-aa-ja33286-amplifier-module-class-d-bluetooth-50-dsp-adau1701-4x100w-6-ohm-p-15064.html
- [R16] SoundImports, Sure Electronics AA-JA33286: https://www.soundimports.eu/en/sure-electronics-aa-ja33286.html · Wondom store: https://store.sure-electronics.com/product/AA-JA33286
- [R17] Audiophonics, Wondom JAB4 AA-JA33285 (TPA3118): https://www.audiophonics.fr/en/amplifier-boards/wondom-jab4-aa-ja33285-amplifier-board-4-ways-tpa3118-bluetooth-50-dsp-adau1701-4x30w-8-ohm-p-15454.html
- [R18] Audiophonics, Wondom JAB3+ AA-JA32173: https://www.audiophonics.fr/en/amplifier-boards/wondom-jab3-aa-ja32173-amplifier-module-class-d-bluetooth-50-dsp-adau1701-2x50w-4-ohm-p-15063.html
- [R19] Wondom, *ADAU1701 DSP Kernel Board APM2 (AA-AP23122) Datasheet*: https://store.sure-electronics.com/upload/download/2/AA-AP23122%20ADAU1701Digital%20Signal%20Processor%20Kernel%20Board%20APM2%20Datasheet.pdf
- [R20] Analog Devices, ADAU1701 datasheet: https://www.analog.com/media/en/technical-documentation/data-sheets/ADAU1701.pdf
- [R21] electro-dan, *ADAU1701/ADAU1401 DSP Information and Expansions*: https://electro-dan.co.uk/electronics/ADAU1701_ADAU1401_dsp_info.aspx
- [R22] ADI EngineerZone, *ADAU1701 I2S input help*: https://ez.analog.com/audio/f/q-a/3417/adau1701-i2s-input-help
- [R23] miniDSP 2x4 HD: https://www.minidsp.com/products/minidsp-in-a-box/minidsp-2x4-hd · manual: https://docs.minidsp.com/product-manuals/2x4-hd/index.html
- [R24] Parts Express, Dayton Audio DSP-408: https://www.parts-express.com/Dayton-Audio-DSP-408-4x8-DSP-Digital-Signal-Processor-for-Home-and-Car-Audio-230-500
- [R25] Arylic Up2Stream Amp 2.1: https://www.audiophonics.fr/en/amplifier-boards/arylic-up2stream-amp-21-amplifier-module-21-wifi-bluetooth-50-tone-control-2x50w-100w-p-14710.html · ACPWorkbench: https://www.arylic.com/blogs/news/acpworkbench
- [R26] Arylic BP50: https://www.arylic.com/products/bp50-bluetooth-preamplifier · Audioholics, Arylic B50 (QCC3040): https://www.audioholics.com/gadget-reviews/arylic-b50

**Bluetooth**
- [R27] Qualcomm, QCC5125: https://www.qualcomm.com/audio/products/qcc51xx-series/qcc5125
- [R28] Qualcomm, QCC3034: https://www.qualcomm.com/audio/products/qcc30xx-series/qcc3034
- [R29] Audiophonics, Bluetooth 5.0 Receiver Board QCC5125 to I2S: https://www.audiophonics.fr/en/bluetooth-modules-wireless-reception/bluetooth-50-receiver-board-qcc5125-ldac-aptx-hd-aptx-adaptive-to-i2s-p-15375.html
- [R30] Audiophonics, Bluetooth 5.1 Receiver QCC5125 + ES9023: https://www.audiophonics.fr/en/bluetooth-modules-wireless-reception/bluetooth-51-receiver-board-qcc5125-aptx-hd-ldac-dac-es9023-p-16840.html
- [R31] ZK-QCC QCC5125/QCC3034 Decoding Board, manual: https://manuals.plus/ae/1005008053826282
- [R32] FYF Audio, QCC5125 digital output board (optik/koaksial/I2S): https://fyfaudio.com/products/qcc5125-bluetooth-51-digital-audio-output-board-i2s-to-coaxial-optical-spdif-aes-hdmi-usb-interface

**Noise/grounding (forum)**
- [R33] diyAudio, *Class D wireless speaker problem with common ground*: https://www.diyaudio.com/community/threads/class-d-wireless-speaker-problem-with-common-ground.298795/
- [R34] diyAudio, *Bluetooth module high frequency and buzzing noise*: https://www.diyaudio.com/community/threads/bluetooth-module-high-frequency-and-buzzing-noise.341922/
- [R35] diyAudio, *Class-D Amp: Battery Powered: Head-Breaking Ground Loop*: https://www.diyaudio.com/community/threads/class-d-amp-battery-powered-head-breaking-ground-loop.273347/

**Power (SMPS)**
- [R61] Mean Well, *LRS-600 series specification*: http://www.meanwelljapan.com/upload/pdf/LRS-600/LRS-600-spec.pdf · harga/spesifikasi distributor: https://www.bravoelectro.com/lrs-600-48.html · https://www.omc-stepperonline.com/lrs-600-48-mean-well-600w-48vdc-12-5a-115-230vac-enclosed-switching-power-supply-lrs-600-48
- [R62] Mean Well, *HRP-600 series specification*: https://www.meanwell.com/Upload/PDF/HRP-600/HRP-600-SPEC.PDF · harga/spesifikasi distributor: https://www.bravoelectro.com/hrp-600-48.html · https://www.trcelectronics.com/products/mean-well-hrp-600-48

**Driver speaker**
- [R37] Dayton Audio RS180-8 spec sheet: https://www.parts-express.com/pedocs/specs/295-355--dayton-audio-rs180-8-reference-woofer-8-ohm-specifications.pdf
- [R38] Dayton Audio RSS210HO-4 spec sheet: https://www.daytonaudio.com/images/resources/295-458-dayton-audio-rss210ho-4-specifications.pdf
- [R39] Dayton Audio RSS265HO-4 spec sheet: https://www.parts-express.com/pedocs/specs/295-462-dayton-audio-rss265ho-4-specifications-46173.pdf
- [R40] Dayton Audio DCS205-4 spec sheet: https://www.daytonaudio.com/images/resources/295-200-dayton-audio-dcs205-4-specifications-46584.pdf
- [R41] Dayton Audio DC160-8 spec sheet: https://www.parts-express.com/pedocs/specs/295-305-dayton-audio-dc160-8-specifications-46146.pdf
- [R42] Dayton Audio DC28FS-8: https://www.daytonaudio.com/product/31/dc28fs-8-1-1-8-silk-dome-shielded-tweeter-8-ohm
- [R43] SB Acoustics SB17NRX2C35-8 datasheet: https://sbacoustics.com/wp-content/uploads/2020/02/6in-SB17NRX2C35-8.pdf
- [R44] Madisound, SB Acoustics SB26STCN-C000-4: https://www.madisoundspeakerstore.com/soft-dome-tweeters-sb-acoustics/sb-acoustics-sb26stcn-c000-4-tweeter-4-ohm/
- [R45] ACR Speaker, 10" 25H100SUWPP Curve: https://acrspeaker.com/product/10-25h100suwpp-curve/

**Enclosure & pengukuran**
- [R46] AJ Design, vent/port length equation: https://www.ajdesigner.com/phpvent/subwoofer_vent_port_equation_length_l.php
- [R47] WinISD (LinearTeam): http://www.linearteam.org/
- [R48] VituixCAD (Kimmo Saunisto): https://kimmosaunisto.net/
- [R49] REW – Room EQ Wizard: https://www.roomeqwizard.com/
- [R50] miniDSP, *UMIK-1/2 setup with REW*: https://www.minidsp.com/applications/acoustic-measurements/umik-1-setup-with-rew · produk: https://www.minidsp.com/products/acoustic-measurement/umik-1
- [R51] Harga UMIK-1 di Indonesia (Rp1.950.000): https://www.car-audio-spesialist.com/produk/563/Harga-UMIK-1-Alat-Setting-Audio-Mini-Dsp--PO/12

**Kabel & fuse**
- [R57] PowerStream, *American Wire Gauge table and AWG current limits*: https://www.powerstream.com/Wire_Size.htm
- [R58] Littelfuse, *MAXI Series Blade Fuses Rated 58V*: https://www.littelfuse.com/assetdocs/littelfuse-datasheet-999-maxi58v?assetguid=10bca524-97c7-4ac8-a68a-1e80e144964e · *MINI Series Rated 58V*: https://www.littelfuse.com/assetdocs/littelfuse-datasheet-997-mini58v?assetguid=838cc4ad-f429-4185-a8e8-ccc70cd2b713

*Nomor R36 dan R52–R56, R59–R60 (boost converter, baterai, BMS, charger, konektor anti-spark, keselamatan Li-ion) dihapus pada revisi AC/DC.*

---

*Dokumen ini adalah hasil riset untuk tujuan edukasi hobi. Angka berlabel [E] adalah estimasi teknik yang wajar, bukan jaminan. Selalu utamakan datasheet terbaru dan pengukuran sendiri. Proyek ini memakai listrik PLN 220–230 V; kerjakan dengan prosedur keselamatan di bagian 12.*
