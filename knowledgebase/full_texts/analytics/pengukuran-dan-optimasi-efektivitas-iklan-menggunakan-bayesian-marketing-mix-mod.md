---
title: Pengukuran dan Optimasi Efektivitas Iklan Menggunakan Bayesian Marketing Mix Modeling dan Bayesian
  Optimization
url: https://doi.org/10.36080/idealis.v9i2.3753
category: analytics
subcategory: measurement
date: 2026-06
venue: 'IDEALIS : InDonEsiA journaL Information System'
authors:
- Fajar Legianto Asmin
- Alz Danny Wowor
source: openalex-oa
pdf_url: https://jom.fti.budiluhur.ac.id/IDEALIS/article/download/3753/1479
pages: 10
chars: 43761
fetched_at: '2026-11-08T17:57:08+00:00'
kb_version: 1
---

# Pengukuran dan Optimasi Efektivitas Iklan Menggunakan Bayesian Marketing Mix Modeling dan Bayesian Optimization

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 204
Measurement and Optimization of TikTok Ads Effectiveness Using
Bayesian Marketing Mix Modeling and Optimization
Fajar Legianto Asmin1*, Alz Danny Wowor2
1,2 Teknik Informatika, Fakultas Teknologi Informasi, Universitas Kristen Satya Wacana, Salatiga, Indonesia
 Email: 1*672021088@student.uksw.edu, 2alzdanny.wowor@uksw.edu
(*: corresponding author)

Abstract - The rapid growth of digital advertising has intensified the need for accurate measurement of advertising
effectiveness and efficient budget allocation. However, many businesses still struggle to quantitatively link marketing efforts to
sales outcomes due to data uncertainty, channel interactions, and dynamic consumer behavior. This study proposes an
integrated framework that combines Bayesian Marketing Mix Modeling (BMMM) with Bayesian Optimization (BO) to
simultaneously measure advertising contribution and optimize budget allocation under uncertainty. The proposed framework
was applied to a dataset of 456 daily TikTok advertising records collected from January 2024 to March 2025. Bayesian Ridge
Regression was employed for model estimation and evaluated using 5-Fold Cross-Validation, yielding strong predictive
performance with an R² of 0.8649 and MAPE of 0.55%. Optimization results indicate that Visual Shopping Ads (VSA) and Live
Shopping Ads (LSA) deliver the highest marginal returns on sales, while Product Showcase Ads (PSA), Awareness, and GMV
Max exhibit relatively lower contributions. Unlike previous studies that typically address marketing mix modeling or budget
optimization separately, this research introduces integrated probabilistic framework that simultaneously measures advertising
effectiveness and optimizes budget allocation by fully utilizing posterior distributions. This approach offers a more robust
alternative to traditional Marketing Mix Modeling and manual allocation methods, particularly in fast-changing digital
advertising environments such as TikTok Ads. The findings provide practical guidance for retailers in making data-driven
marketing decisions and demonstrate the significant potential of Bayesian approaches in digital marketing analytics, especially
for emerging markets like Indonesia.
Keywords: Advertising Effectiveness, Bayesian Marketing Mix Modeling, Bayesian Optimization, Budget Allocation, Digital
Marketing

Abstrak - Perkembangan pesat periklanan digital telah meningkatkan kebutuhan akan pengukuran efektivitas iklan yang akurat
dan alokasi anggaran yang efisien. Namun, banyak bisnis masih kesulitan menghubungkan aktivitas pemasaran dengan hasil
penjualan secara kuantitatif akibat ketidakpastian data, interaksi antar kanal, dan perilaku konsumen yang dinamis. Penelitian
ini mengusulkan kerangka terintegrasi yang menggabungkan Bayesian Marketing Mix Modeling  (BMMM) dan Bayesian
Optimization (BO) untuk mengukur kontribusi iklan sekaligus mengoptimalkan alokasi anggaran di tengah ketidakpastian.
Kerangka ini diterapkan pada dataset yang terdiri dari 456 catatan harian aktivitas periklanan TikTok periode Januari 2024
hingga Maret 2025. Estimasi model dilakukan menggunakan Bayesian Ridge Regression dan dievaluasi melalui 5-Fold Cross-
Validation, menghasilkan performa prediksi yang kuat dengan nilai R² sebesar 0,8649 dan MAPE sebesar 0,55%. Hasil
optimasi menunjukkan bahwa Visual Shopping Ads (VSA) dan Live Shopping Ads (LSA) memberikan marginal return tertinggi
terhadap penjualan, sementara Product Showcase Ads (PSA), Awareness, dan GMV Max menunjukkan kontribusi yang lebih
rendah. Berbeda dengan studi sebelumnya yang umumnya membahas modeling atau optimasi secara terpisah, penelitian ini
menghadirkan kerangka probabilistik terintegrasi yang secara simultan mengukur efektivitas iklan dan mengoptimalkan alokasi
anggaran dengan memanfaatkan distribusi posterior secara penuh. Kerangka ini menawarkan alternatif yang lebih robust
dibandingkan Marketing Mix Modeling tradisional dan alokasi manual, khususnya dalam lingkungan periklanan digital yang
cepat berubah seperti TikTok Ads. Temuan penelitian ini memberikan panduan praktis bagi pelaku ritel di Indonesia dalam
pengambilan keputusan pemasaran berbasis data serta menunjukkan potensi besar pendekatan Bayesian dalam analitik
pemasaran digital.
Kata Kunci:  Alokasi Anggaran, Bayesian Marketing Mix Modeling , Bayesian Optimization , Efektivitas Periklanan,
Pemasaran Digital.
1. PENDAHULUAN
Perkembangan pesat teknologi digital telah mengubah lanskap pemasaran secara fundamental. Saat ini, lebih
dari 5,66 miliar orang atau sekitar 69,9% populasi global aktif menggunakan media sosial [1]. Pengeluaran iklan
global diproyeksikan mencapai US$1,04 triliun pada tahun 2026, meningkat 5,1% dibandingkan tahun sebelumnya
dan merupakan pertama kalinya angka ini melampaui satu triliun dolar AS. Pertumbuhan ini didorong oleh
algorithm-driven advertising  yang diprediksi akan mencapai 71,6% dari total pengeluaran iklan pada 2026 [2].
Platform seperti Google Ads, Meta Ads, dan TikTok Ads tidak hanya menawarkan jangkauan luas dan
personalisasi, tetapi juga mendorong pendekatan data-driven marketing. Sebagai gambaran, Alphabet (Google)
meraup lebih dari US$264,5 miliar dari iklan pada 2024 [3]. Bersama Meta dan Amazon, ketiga perusahaan ini
diproyeksikan menguasai hampir 56% pangsa pasar iklan global di luar China pada tahun 2025 [4].
Meskipun investasi iklan digital terus meningkat, pengukuran efektivitasnya masih menghadapi tantangan
signifikan. Analisis 15 eksperimen lapangan besar di Facebook menunjukkan bahwa metode observasional yang
umum digunakan di industri sering kali gagal mereproduksi hasil Randomized Controlled Trials  (RCT) [5].

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 205
Tantangan ini diperparah oleh kompleksitas multi-touch attribution, sehingga pengukuran efektivitas iklan harus
menjadi bagian integral sepanjang siklus perencanaan dan evaluasi kampanye  [6]. Marketing Mix Modeling
(MMM) konvensional berbasis regresi OLS merupakan pendekatan yang umum digunakan, namun memiliki
keterbatasan dalam menangani efek non-linear, interaksi antar kanal, dan ketidakpastian data [7].
Kemajuan signifikan dicapai melalui penerapan pendekatan Bayesian pada MMM. Bayesian Media Mix
Model dengan functional forms fleksibel memungkinkan pemodelan efek adstock dan saturasi secara lebih akurat
[7],  sementara model hierarkis dengan sign constraints menghasilkan estimasi yang lebih sesuai logika bisnis [8].
Hierarchical Bayesian Market Mix Models  (HBMMM) mampu meningkatkan akurasi prediksi hingga 30,4%
melalui integrasi data individual dan agregat [9]. Bayesian Deep Learning dengan self-attention mechanism juga
berhasil meningkatkan akurasi forecasting ROAS yang risk-aware pada platform e-commerce [10]. Lebih jauh,
kerangka Lightweight Bayesian untuk data pemasaran berdimensi tinggi terbukti efisien secara komputasi tanpa
mengorbankan akurasi [11], dan pendekatan CausalMMM telah menunjukkan kemampuan yang baik dalam causal
structure learning pada data heterogen antar toko  [12].
Di sisi optimasi, berbagai pendekatan telah dieksplorasi: multi-armed bandits [13], reinforcement learning
multimodal [14], [15], [16] , ROI-constrained bidding  berbasis Bayesian reinforcement learning  [17], serta
Bayesian Optimization dengan Gaussian Process untuk mengoptimalkan strategi iklan secara periodik [18]  dan
menangani budget constraint [19]. Studi multi-objective Bayesian Optimization menekankan pentingnya integrasi
antara model pengukuran dan proses optimasi ketika menangani beberapa metrik iklan secara simultan [20].
Namun, sebagian besar studi yang ada masih memisahkan kedua tahap tersebut, sehingga distribusi posterior dari
model pengukuran belum dimanfaatkan secara penuh.
Pada konteks Indonesia, pendekatan yang ada masih didominasi sistem deterministik: implementasi e-
commerce [21], sistem pendukung keputusan berbasis TOPSIS [22] dan Fuzzy AHP [23], serta prediksi penjualan
ritel berbasis machine learning  seperti Random Forest  [24]. Pendekatan-pendekatan tersebut belum mampu
menangani karakteristik time-series yang dinamis dan stokastik, termasuk efek carryover, saturasi, dan interaksi
antar kanal pada periklanan digital. Kesenjangan ini memotivasi penelitian yang mengintegrasikan BMMM dan
BO dalam satu pipeline probabilistik yang koheren untuk konteks TikTok Ads di Indonesia.
Berdasarkan kesenjangan yang telah diidentifikasi, penelitian ini dirumuskan untuk menjawab dua
pertanyaan utama (RQ): RQ1: Seberapa akurat kerangka BMMM dapat mengukur kontribusi masing-masing kanal
iklan TikTok terhadap penjualan di tengah ketidakpastian data?, dan RQ2: Bagaimana integrasi BMMM dengan
Bayesian Optimization  dapat menghasilkan rekomendasi alokasi anggaran yang lebih optimal dibandingkan
pendekatan konvensional?
Secara operasional, tujuan penelitian ini adalah: (1) mengembangkan dan memvalidasi model BMMM
berbasis Bayesian Ridge Regression  pada data TikTok Ads harian; (2) mengintegrasikan hasil model tersebut
sebagai objective function dalam Bayesian Optimization; dan (3) memberikan rekomendasi alokasi anggaran yang
actionable bagi perusahaan ritel dalam pengambilan keputusan pemasaran berbasis data. Penelitian ini
memberikan tiga jenis kontribusi yang saling melengkapi, pertama kontribusi metodologis dengan mengusulkan
kerangka terintegrasi yang menggabungkan Bayesian Marketing Mix Modeling  dengan Bayesian Optimization
dalam satu model probabilistik. Integrasi ini memungkinkan pengukuran ketidakpastian yang eksplisit sekaligus
optimasi anggaran yang adaptif, sesuatu yang belum dilakukan pada studi sebelumnya. Kedua kontribusi empiris,
dengan menyediakan bukti kuantitatif tentang efektivitas relatif lima kanal TikTok Ads (VSA, LSA, PSA,
Awareness, GMV Max) pada data nyata dari perusahaan ritel Indonesia selama 15 bulan, termasuk pemodelan
efek carryover, saturasi, dan interaksi musiman.
Terakhir memberikan kontribusi praktis, yaitu mmberikan rekomendasi alokasi anggaran yang actionable
dan berbasis data bagi praktisi pemasaran digital Indonesia, khususnya retailer yang menggunakan TikTok Ads
sebagai kanal utama menggantikan pendekatan intuitif yang masih umum digunakan. Penelitian ini dilakukan pada
sebuah perusahaan ritel yang masih menghadapi kesenjangan antara biaya iklan dan hasil penjualan akibat belum
adanya sistem pengukuran dan optimasi yang terstruktur. Oleh karena itu, penelitian ini bertujuan untuk
mengembangkan kerangka analitis berbasis Bayesian yang mampu mengukur efektivitas iklan digital sekaligus
menentukan strategi alokasi anggaran yang optimal dan berbasis data.
2. METODE PENELITIAN
Penelitian ini menggabungkan Bayesian Marketing Mix Modeling (BMMM) dengan Bayesian Optimization
(BO). Pendekatan Bayesian dipilih karena mampu mengakomodasi ketidakpastian data dan menghasilkan
distribusi posterior untuk setiap parameter, sehingga estimasi kontribusi masing-masing kanal iklan menjadi lebih
robust dibandingkan metode regresi klasik. Keunggulan BMMM dalam memodelkan efek carryover dan
saturation telah ditunjukkan melalui functional forms yang fleksibel [7]. Pendekatan tersebut juga telah diperkaya
dengan hierarchical structure  dan s ign constraints  [8]. Untuk aspek optimasi alokasi anggaran, penelitian ini
terinspirasi dari penerapan BO dengan Gaussian Process Regression  yang digunakan untuk mengoptimalkan

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 206
strategi iklan secara periodik di lingkungan e-commerce [18]. Pendekatan ini telah terbukti efektif dalam
meningkatkan efisiensi pengeluaran iklan, terutama ketika mempertimbangkan karakteristik waktu dan dinamika
pasar.
Bayesian Optimization (BO) juga telah terbukti efektif dalam mengoptimalkan alokasi sumber daya di bawah
budget constraint  dan ketidakpastian, seperti pada multi-step budgeted BO [19]. Namun, penerapannya pada
alokasi budget iklan digital masih relatif terbatas. Berbeda dengan studi sebelumnya yang umumnya membahas
BMMM atau BO secara terpisah, penelitian ini mengintegrasikan kedua metode tersebut dalam satu kerangka
terpadu. Integrasi ini memungkinkan pengukuran kontribusi iklan yang probabilistik sekaligus rekomendasi
alokasi anggaran yang dinamis dan adaptif terhadap lingkungan periklanan TikTok Ads yang cepat berubah.
Pendekatan ini diharapkan dapat mengisi gap yang ada dengan menyediakan solusi yang lebih komprehensif dan
data-driven.
2.1. Tahapan dan Alur Penelitian
Gambar 1 menunjukkan kerangka metodologis yang digunakan dalam penelitian ini. Proses penelitian
dimulai dengan pengumpulan data aktivitas pemasaran dan data penjualan, yang kemudian dilanjutkan dengan
tahap feature engineering untuk mempersiapkan dataset sebelum dilakukan pemodelan.

Gambar 1. Kerangka Pemodelan dan Optimasi Marketing Mix Bayesian
Tahap berikutnya adalah proses estimasi model Bayesian Marketing Mix Modeling  (BMMM), yang
digunakan untuk mengukur kontribusi masing-masing kanal pemasaran terhadap kinerja penjualan. Selanjutnya,
hasil estimasi model digunakan sebagai masukan pada tahap optimasi. Pada tahap ini, alokasi anggaran iklan
ditentukan menggunakan pendekatan Bayesian Optimization (BO) untuk memperoleh kombinasi distribusi anggaran
yang menghasilkan performa pemasaran yang paling optimal.
2.2. Pengumpulan dan Pembersihan Data
Data penelitian diperoleh dari aktivitas pemasaran digital dan penjualan harian pada platform TikTok, yang
dikumpulkan oleh tim pengiklan pada sebuah perusahaan ritel Indonesia. Periode observasi mencakup data harian
dari Januari 2024 hingga Maret 2025, dengan total 456 titik observasi. Data sudah terorganisir dengan baik
sehingga pembersihan yang diperlukan bersifat minimal, terutama penanganan missing values pada beberapa fitur
yang memiliki nilai kosong ( null). Proses ini memastikan konsistensi, kelengkapan, dan kualitas data sebelum
dilanjutkan ke tahap transformasi dan pemodelan.
2.3. Feature Engineering
Tahap ini bertujuan menyiapkan data agar stabil, representatif, dan siap dipakai dalam pemodelan. Proses
dilakukan melalui tiga langkah utama: transformasi variabel, konstruksi fitur baru, dan encoding variabel
kategorikal.
a. Transformasi Variabel
Variabel target (Sales) ditransformasikan menggunakan logaritma natural ( log1p) untuk menstabilkan varians
data. Seluruh prediktor distandarisasi dengan Standard Scaler untuk memastikan bahwa setiap variabel berada
pada skala yang sebanding sekaligus mengurangi potensi multikolinearitas. Variabel pengeluaran iklan yang
dilibatkan dalam tahap ini mencakup Visual Shopping Ads  (VSA), Live Shopping Ads  (LSA), Product

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 207
Showcase Ads (PSA), dan GMV Max, serta metrik Awareness. Setiap kanal periklanan TikTok yang digunakan
dalam penelitian ini memiliki karakteristik yang berbeda, yaitu sebagai berikut:
1. Visual Shopping Ads (VSA): iklan yang menampilkan visual produk secara menarik dan berfokus pada produk,
biasanya ditampilkan pada in-feed atau halaman explore untuk menarik perhatian pengguna.
2. Live Shopping Ads  (LSA): iklan yang terintegrasi dengan sesi live streaming , memungkinkan pengguna
melakukan pembelian secara langsung selama siaran berlangsung.
3. Product Showcase Ads  (PSA): iklan interaktif berbentuk katalog yang memungkinkan pengguna menjelajahi
beberapa produk dalam satu unit iklan.
4. Awareness: jenis kampanye iklan yang berfokus pada peningkatan visibilitas dan kesadaran merek, bukan pada
konversi penjualan secara langsung.
5. GMV Max: sistem otomatis berbasis algoritma yang dirancang untuk mengoptimalkan Gross Merchandise
Value (GMV) dengan menggabungkan lalu lintas berbayar ( paid traffic ) dan organik ( organic traffic ).
Algoritma ini secara dinamis menyesuaikan aset kreatif, pemilihan produk, serta strategi penawaran (bidding
strategy) untuk meningkatkan efisiensi konversi.
b. Kontruksi Fitur Baru
Fitur tambahan dibangun untuk menangkap pola musiman, interaksi, dan dinamika historis:
1. Musiman : cyclic encoding waktu (Month_Sin, Month_Cos, Week_Sin, Week_Cos).
2. Interaksi : gabungan variabel (misalnya AdSpend × Discount, AdSpend × Holiday).
3. Lag features : penjualan sebelumnya (Sales_Lag_1, Sales_Lag_7, Sales_Lag_30).
c. Encoding Variabel Kategorikal
Variabel biner seperti Holiday_Flag dan Payday_Flag dikonversi menjadi numerik (0/1) agar dapat digunakan
dalam pemodelan, karena keduanya berpengaruh pada pola penjualan.
2.4. Asumsi Utama Model Bayesian
Sebelum memaparkan spesifikasi teknis, penting untuk memahami asumsi mendasar yang melandasi
pendekatan Bayesian dalam penelitian ini:
a. Asumsi linearitas dalam skala log: hubungan antara pengeluaran iklan dan penjualan diasumsikan linear
setelah transformasi logaritmik, yang berarti setiap peningkatan relatif pengeluaran iklan berdampak
proporsional pada penjualan.
b. Asumsi independensi residual: kesalahan prediksi diasumsikan berdistribusi normal dengan rata-rata nol,
meskipun fitur lag dimasukkan untuk menangkap dependensi temporal.
c. Asumsi informatif prior: distribusi prior mencerminkan keyakinan awal bahwa koefisien iklan cenderung
kecil dan positif. Prior Gamma pada parameter regularisasi mencegah overfitting pada dataset dengan ukuran
sedang.
d. Asumsi stasioneritas relatif: hubungan antara variabel diasumsikan relatif stabil sepanjang periode observasi,
meskipun fitur musiman dan lag dimasukkan untuk menangkap variasi periodik.
2.5. Spesifikasi Bayesian Marketing Mix Modeling
a. Struktur Model
Estimasi model dilakukan menggunakan Bayesian Ridge Regression  yang diimplementasikan dengan
pustaka PyMC. Metode ini dipilih karena mampu mengakomodasi regularisasi secara probabilistik serta
menghasilkan distribusi posterior untuk setiap parameter, sehingga ketidakpastian estimasi dapat diukur secara
lebih transparan. Secara umum, hubungan antara variabel independen dan variabel dependen dalam model
dinyatakan pada persamaan (1).
𝑦 = 𝛼 + ෍ 𝛽௜𝑥௜ + 𝜀
௞
௜ୀଵ
, 𝜀 ∼  𝒩(0, 𝜎ଶ) (1)
Variabel target ditransformasikan menggunakan fungsi logaritmik untuk mengurangi skewness dan
meningkatkan stabilitas model sebagaimana ditunjukkan pada Persamaan (2).
𝑦 = log(1 + 𝑆𝑎𝑙𝑒𝑠) (2)
b. Distribusi Prior
Distribusi prior untuk setiap parameter ditentukan seperti yang ditunjukkan pada Tabel 1, beserta justifikasi
pemilihannya.

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 208
Tabel 1. Spesifikasi Distribusi Prior pada Model Bayesian Marketing Mix
Parameter Notasi Distribusi Prior Keterangan Justifikasi Pemilihan
Intercept 𝛼 Normal(0, 5) Rata-rata awal
penjualan
Prior lemah ( weakly informative ); memberi
kebebasan model mengestimasi baseline
Koefisien
fitur
𝛽௜ Normal(0, λିଵ) Regresi dengan
regularisasi
Regularisasi Bayesian mencegah overfitting;
varians dikontrol oleh 𝜆
Regularisasi 𝜆 Gamma(2, 0.5) Kontrol
kompleksitas model
Mendorong regularisasi sedang; sesuai untuk
dataset berukuruan menengah (456 hari)
Noise/residual 𝜎 HalfNormal(2) Error standar Memastikan 𝜎 > 0 secara definitif; skala 2 sesuai
rentang nilai log transformed
c. Fitur-fitur dalam model
Model mengikutsertakan berbagai fitur hasil transformasi dan konstruksi yang telah dijelaskan pada bagian
2.3. Variabel tersebut dikelompokkan sebagai berikut:
1. Fitur iklan  : VSA_Centered, LSA_Centered, PSA_Centered, Awareness_Centered, GMV_Centered
2. Fitur harga  : WAP
3. Diskon dan promosi : Discount_Rate
4. Interaksi  : AdSpend_Discount_Interaction_Centered, AdSpend_Season_Interaction ,
Discount_Season_Interaction, AdSpend_Holiday_Interaction, Discount_Holiday_Interaction
5. Musiman  : Month_Sin, Month_Cos, Week_Sin, Week_Cos, Seasonality_Index
6. Lag penjualan : Sales_Lag_1, Sales_Lag_7, Sales_Lag_30
7. Fitur dummy : Holiday_Flag, Payday_Flag
Seluruh prediktor numerik serta variabel target distandarisasi menggunakan metode Standard Scaler untuk
menjaga konsistensi skala di antara seluruh fitur. Proses ini memastikan bahwa tidak ada variabel yang
mendominasi proses estimasi akibat perbedaan magnitudo atau skala nilai antar variabel.
d. Inferensi dan Estimasi
Inferensi parameter dilakukan menggunakan metode sampling Markov Chain Monte Carlo  (MCMC) yang
diimplementasikan melalui fungsi pm.sample() pada perangkat lunak PyMC. Prosedur ini menggunakan 1.000
iterasi sampling dengan 500 langkah tuning untuk mencapai konvergensi yang stabil pada distribusi posterior.
Sampel posterior yang dihasilkan kemudian digunakan untuk menghasilkan estimasi prediktif serta mengevaluasi
kinerja model pada subset data validasi. Pendekatan ini memungkinkan setiap koefisien model diinterpretasikan
secara probabilistik, sehingga tidak hanya merepresentasikan besarnya pengaruh yang diestimasi, tetapi juga
tingkat ketidakpastian yang menyertainya. Hal ini merupakan salah satu keunggulan utama kerangka Bayesian
dibandingkan metode tradisional yang hanya menghasilkan estimasi titik ( point estimate).
2.6. Evaluasi Model
Evaluasi kinerja model dilakukan dengan strategi 5-Fold Cross-Validation  untuk menilai kemampuan
generalisasi terhadap data yang tidak digunakan selama pelatihan. Pendekatan ini dipilih agar model tidak hanya
menyesuaikan diri dengan data historis, tetapi juga mampu memberikan prediksi yang konsisten pada data baru.
Evaluasi dilakukan berdasarkan empat metrik utama, yaitu:
a. Mean Absolute Error (MAE)
b. Root Mean Squared Error (RMSE)
c. R-squared (R²)
d. Mean Absolute Percentage Error (MAPE)
Kombinasi metrik ini dipilih untuk memberikan gambaran menyeluruh mengenai akurasi prediksi, baik dari
sisi kesalahan absolut, kesalahan kuadrat, maupun proporsi variansi yang dijelaskan. Dengan demikian, hasil
evaluasi model tidak hanya mengukur ketepatan prediksi, tetapi juga menjadi dasar validasi sebelum model
digunakan dalam proses optimasi alokasi anggaran pada tahap berikutnya.
2.7. Optimasi Anggaran
Fungsi prediktif yang dihasilkan oleh model Bayesian Marketing Mix kemudian digunakan sebagai objective
function dalam Bayesian Optimization. Variabel yang dioptimasi mencakup biaya iklan VSA, biaya iklan LSA,
biaya iklan PSA, awareness (alokasi kampanye kesadaran merek), serta GMV (alokasi untuk mendorong Gross
Merchandise Value).
a. Batasan Alokasi
Untuk memastikan bahwa solusi yang dihasilkan tetap realistis dan sesuai dengan kondisi operasional di
dunia nyata, batas atas dan batas bawah untuk setiap variabel ditentukan berdasarkan nilai minimum dan

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 209
maksimum historis yang telah dibulatkan. Mekanisme pembatasan ini bertujuan untuk mencegah algoritma
optimasi merekomendasikan tingkat pengeluaran yang tidak realistis atau berada di luar kapasitas operasional
perusahaan.
b. Proses Optimasi
Proses optimasi dilakukan menggunakan pendekatan Bayesian Optimization  dengan Gaussian Process
sebagai surrogate model dan fungsi akuisisi Expected Improvement (EI). Proses optimasi diawali dengan lima titik
awal acak (init_points = 5) untuk mengeksplorasi ruang parameter. Selanjutnya, dilakukan sepuluh iterasi
eksploitasi (n_iter = 10) yang bertujuan untuk memperdalam pencarian pada wilayah parameter yang menunjukkan
potensi hasil terbaik. Tujuan optimasi ( optimization objective ) dalam penelitian ini dinyatakan pada Persamaan
(3), yaitu memaksimalkan hasil prediksi model terhadap nilai penjualan.
𝑚𝑎𝑥 𝑓(𝑥) = 𝑦ො = 𝑚𝑜𝑑𝑒𝑙(𝑥) (3)
Adapun himpunan variabel yang digunakan dalam proses optimasi ditunjukkan pada Persamaan (4).
𝑥 = {𝑎𝑑_𝑠𝑝𝑒𝑛𝑑_𝑉𝑆𝐴, 𝑎𝑑_𝑠𝑝𝑒𝑛𝑑_𝐿𝑆𝐴, 𝑎𝑑_𝑠𝑝𝑒𝑛𝑑_𝑃𝑆𝐴, 𝑎𝑤𝑎𝑟𝑒𝑛𝑒𝑠𝑠, 𝐺𝑀𝑉} (4)
Melalui pendekatan ini, diperoleh kombinasi alokasi anggaran yang memberikan estimasi penjualan tertinggi
dalam batasan yang telah ditetapkan.
2.8. Pseudocode Alur Penelitian
Pseudocode berikut merangkum langkah-langkah operasional penelitian secara rinci, mulai dari persiapan
data hingga proses optimasi alokasi anggaran:
Input : Data Tiktok Ads Harian (N=456, Jan 2024 – Mar 2025)
Output : Alokasi anggaran iklan optimal & prediksi penjualan maksimal
Fase 1 : Persiapan Data
1. Muat data mentah; tangani missing values (imputasi median)
2. Transformasi: y ← log1p (Sales); standarisasi prediktor numerik
3. Bangun fitur interaksi, cyclic encoding, lag features
Fase 2: Bayesian Marketing Mix Modeling (BMMM)
4. Definisikan prior: α ~ N(0,5); βᵢ ~ N(0,λ⁻¹); λ ~ Gamma (2,0.5); σ ~ HalfNormal (2)
5. Spesifikasi likelihood: y ~ N (α + Σβᵢxᵢ, σ²)
6. Jalankan MCMC (1000 iterasi, 500 tuning) → sampel posterior
7. Evaluasi: 5-Fold CV → hitung MAE, RMSE, R², MAPE
8. JIKA R² < 0.80 ATAU MAPE > 5%: kembali ke langkah 2 (revisi fitur)
Fase 3: Bayesian Optimization
9. Tetapkan batas [min_hist, max_hist] untuk setiap variabel iklan
10. Inisialisasi Gaussian Process sebagai surrogate model
11. Jalankan 5 titik awal acak (init_points=5)
12. Iterasi 10 kali eksploitasi menggunakan Expected Improvement (EI)
13. max f(x) = ŷ = model(x), di mana x = {VSA, LSA, PSA, Awareness, GMV}
14. Kembalikan: alokasi optimal x* dan prediksi penjualan ŷ*
3. HASIL DAN PEMBAHASAN
3.1. Ringkasan Hasil Estimasi Model
Model Bayesian Marketing Mix Modeling (BMMM) dievaluasi menggunakan strategi 5-Fold Cross-
Validation. Tabel 2 menyajikan metrik performa rata-rata pada data validasi.
Tabel 2. Rata-Rata Performa Validasi 5-Fold BMMM
Metrik Evaluasi Nilai Rata-rata
MAE 0.09
RMSE 0.14
R2 0.8649
MAPE (%) 0.55%

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 210
3.2. Visualisasi Hasil Prediksi vs Aktual (Fold ke-5)
Gambar 2 memperlihatkan perbandingan antara nilai penjualan aktual dan prediksi model pada fold ke-5.
Secara visual, garis prediksi (oranye) mengikuti tren penjualan aktual (biru) dengan sangat baik, termasuk mampu
menangkap lonjakan (spike) dan penurunan tajam.

Gambar 2. Perbandingan Nilai Aktual dan Prediksi Penjualan pada Fold ke-5
3.3. Interpretasi Hasil Model
Nilai R² sebesar 0.8649 menunjukkan bahwa model berhasil menjelaskan 86,49 % variasi penjualan (dalam
skala log transformed). Artinya, lebih dari 86 % fluktuasi penjualan harian dapat dijelaskan oleh variabel iklan,
harga, promosi, musim, dan interaksi antar faktor yang dimasukkan dalam model. MAPE yang sangat rendah (0,55
%) mengindikasikan bahwa rata-rata kesalahan prediksi penjualan hanya 0,55 % dari nilai aktual, jauh dibawah
5% yang lazim dianggap sebagai batas akurasi tinggi dalam literatur peramalan.
Penyimpangan kecil yang terlihat pada beberapa titik observasi mencerminkan variabilitas yang tidak
sepenuhnya dijelaskan oleh variabel input, seperti faktor eksternal (tren viral, perubahan algoritma TikTok).
Namun deviasi tersebut tidak berdampak signifikan terhadap performa keseluruhan, sebagaimana dibuktikan oleh
konsistensi metrik antar fold. Performa yang konsisten ini menegaskan kemampuan generalisasi model yang baik.
3.4. Perbandingan dengan Pendekatan Non-Bayesian
Untuk memberikan konteks metodologis yang lebih kuat, Tabel 3 menyajikan perbandingan konseptual dan
empiris antara pendekatan BMMM yang diusulkan dengan Ordinary Least Squares  (OLS) Regression, yang
hingga kini masih menjadi pendekatan MMM konvensional paling umum digunakan dalam industri. Perbedaan
mendasar antara kedua pendekatan ini terletak pada aspek kuantifikasi ketidakpastian prediktor, terutama saat
menghadapi data pemasaran bertipe time-series yang rentan terhadap multikolinearitas. OLS hanya mampu
menghasilkan estimasi titik tunggal ( point estimate), sehingga pengambil keputusan kesulitan mengukur tingkat
keandalan, variabilitas, dan sensitivitas dari parameter efektivitas iklan yang dihasilkan. Sebaliknya, BMMM
mampu menghasilkan distribusi posterior penuh atas setiap koefisien regresi melalui integrasi prior knowledge.
Karakteristik Bayesian ini sangat krusial bagi manajer pemasaran untuk menilai risiko serta ketidakpastian dalam
simulasi skenario alokasi anggaran iklan secara lebih eksplisit, adaptif, dan terukur.
Tabel 3. Perbandingan Karakteristik Teoretis Pendekatan OLS dan BMMM
Dimensi Perbandingan OLS Regression (Konvensional) BMMM (Penelitian Ini)
Estimasi parameter Point estimate tunggal Distribusi posterior (mean + interval)
Kuantifikasi ketidakpastian Tidak tersedia secara probalistik Eksplisit melalui distribusi posterior
Regularisasi Tidak ada (rentan overfitting) Prior informatif (Bayesian regularization)
Penanganan data kecil/menengah Tidak stabil pada n<1000 Stabil dengan prior knowledge
Integrasi dengan optimasi Membutuhkan tahap terpisah Terintegrasi dalam satu pipeline

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 211
3.5. Hasil Optimasi Anggaran
Berdasarkan model BMMM yang telah tervalidasi, Bayesian Optimization menghasilkan kombinasi alokasi
belanja iklan yang memaksimalkan prediksi penjualan dalam batasan historis. Hasil optimasi disajikan pada
Tabel 4.
Tabel 4. Hasil Optimasi Alokasi Anggaran Iklan
Variabel Alokasi Optimal
VSA Spend Rp5,984,057.36
LSA Spend Rp4,122,115.42
PSA Spend Rp1,125,175.52
Awareness Spend Rp183,808.46
GMV Rp938,375.83
Total Spend Rp12,353,532.59
Prediksi Penjualan Rp24,234,209.43
3.6. Interpretasi Bisnis per Kanal Iklan
Hasil optimasi memberikan implikasi manajerial yang berbeda untuk setiap kanal:
a. Visual Shopping Ads  (VSA). Prioritas Tinggi (48,4% anggaran): VSA memperoleh porsi terbesar karena
format visual produk yang kuat berkontribusi langsung pada konversi. Dari perspektif manajerial, VSA
sebaiknya menjadi kanal utama dengan kreasi konten visual yang terus diperbarui secara berkala. Investasi
dalam kualitas konten visual (foto produk profesional, video singkat) diproyeksikan memberikan imbal hasil
terbaik.
b. Live Shopping Ads (LSA). Prioritas Tinggi (33,4% anggaran): LSA menunjukkan marginal return tertinggi
kedua karena sesi live streaming  menciptakan urgensi pembelian yang tinggi. Retailer disarankan
meningkatkan frekuensi sesi live berkualitas, mengoptimalkan jam tayang ( prime time ), dan
mengintegrasikan promosi eksklusif khusus live untuk memaksimalkan konversi.
c. Product Showcase Ads (PSA). Prioritas Menengah (9,1% anggaran): PSA berguna sebagai pelengkap untuk
mendorong eksplorasi produk, namun menunjukkan diminishing return  yang lebih cepat. Alokasi sedang
disarankan, dengan fokus pada produk dengan margin tinggi atau produk baru yang perlu diperkenalkan.
d. GMV Max. Prioritas Menengah (7,6% anggaran): Meskipun sistem GMV Max bersifat otomatis,
kontribusinya terhadap peningkatan penjualan inkremental terbukti lebih rendah dibandingkan VSA dan
LSA. Retailer disarankan menggunakannya sebagai booster pelengkap, bukan sebagai kanal utama, sambil
terus memantau efisiensi konversinya.
e. Awareness. Prioritas Rendah (1,5% anggaran): Awareness mendapat alokasi terkecil karena secara inheren
tidak dirancang untuk konversi langsung. Namun peran jangka panjangnya dalam membangun ekuitas merek
tidak boleh diabaikan. Disarankan untuk mempertahankan investasi minimal yang konsisten guna menjaga
visibilitas merek, terutama di momentum musiman.
3.7. Analisis Sensitivitas dan Skenario Alokasi Alternatif
Untuk memberikan gambaran proyeksi yang lebih komprehensif kepada pengambil keputusan, Tabel 5
menyajikan simulasi alokasi anggaran pada setiap kanal iklan beserta proyeksi target penjualan yang dihasilkan
oleh model BMMM. Seluruh nominal angka di dalam tabel disajikan dalam satuan Rupiah utuh untuk menjaga
konsistensi interpretasi.
Tabel 5. Proyeksi Penjualan Berdasarkan Skenario Alokasi Anggaran Iklan
Skenario VSA (Rp) LSA (Rp) PSA (Rp) Awareness (Rp) GMV(Rp) Total Spend (Rp) Prediksi Penjualan (Rp)
S1 5.984.057 4.122.115 1.125.175 183.808 938.375 12.353.533 24.234.209
S2 4.488.000 3.092.000 844.000 138.000 703.000 9.265.000 18.200.000
S3 7.500.000 5.000.000 0 0 0 12.500.000 22.800.000
S4 2.471.000 2.471.000 2.471.000 2.471.000 2.469.000 12.353.000 19.100.000
Simulasi eksperimen pada Tabel 5 dibagi menjadi empat skenario strategis utama dengan karakteristik sebagai
berikut:
a. Skenario 1 (S1 - Optimal/Baseline): Alokasi optimal yang direkomendasikan langsung oleh model BMMM
berdasarkan efisiensi dan performa historis data.
b. Skenario 2 (S2 - Efisiensi Anggaran): Skenario penghematan dengan memotong total anggaran belanja iklan
sebesar 25% yang didistribusikan secara proporsional.

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 212
c. Skenario 3 (S3 - Fokus VSA dan LSA): Skenario agresif yang memusatkan seluruh modal anggaran hanya
pada dua kanal utama dan menonaktifkan kanal lainnya.
d. Skenario 4 (S4 - Distribusi Merata): Skenario konvensional non-biad di mana total anggaran dibagi secara
rata ke seluruh kanal periklanan TikTok yang tersedia.
Prediksi penjualan untuk skenario alternatif (S2 hingga S4) diestimasi menggunakan model BMMM yang
sama, dengan asumsi variabel eksternal di luar model berada pada nilai rata-rata historis ( ceteris paribus). Hasil
proyeksi menunjukkan bahwa Skenario S2 diperkirakan menghasilkan penjualan sebesar Rp18.200.000, Skenario
S3 sebesar Rp22.800.000, dan Skenario S4 sebesar Rp19.100.000. Ketiga skenario alternatif tersebut
menghasilkan performa penjualan yang lebih rendah jika dibandingkan dengan skenario optimal (S1) yang mampu
mencapai Rp24.234.209.
Berdasarkan analisis sensitivitas tersebut, penerapan alokasi anggaran secara merata (S4) terbukti
menghasilkan proyeksi penjualan yang tidak efisien. Temuan ini secara empiris mengonfirmasi adanya nilai
tambah (value add) yang signifikan dari penerapan pendekatan optimasi berbasis data ( data-driven). Di sisi lain,
skenario fokus anggaran pada saluran Visual Shopping Ads  (VSA) dan Live Shopping Ads  (LSA) (S3) mampu
memberikan hasil pencapaian yang mendekati optimal meskipun menonaktifkan tiga kanal lainnya. Hal ini
memperkuat rekomendasi strategis bagi manajemen untuk memprioritaskan alokasi anggaran pada kanal-kanal
pemasaran yang memiliki nilai pengembalian marjinal ( marginal return) tertinggi.
4. KESIMPULAN
Penelitian ini berhasil mengembangkan kerangka terintegrasi yang menggabungkan Bayesian Marketing Mix
Modeling (BMMM) dengan Bayesian Optimization  (BO) untuk mengukur efektivitas belanja iklan digital dan
mengoptimalkan alokasi anggaran secara simultan pada platform TikTok Ads. Model Bayesian Ridge Regression
yang divalidasi melalui 5-Fold Cross Validatio n mencapai R² = 0,8649 dan MAPE = 0,55%, membuktikan
kemampuannya memberikan estimasi kontribusi per kanal yang akurat dan probabilistik (RQ1). Integrasi dengan
BO menghasilkan rekomendasi alokasi anggaran total Rp12.353.533 dengan prediksi penjualan Rp24.234.209,
terbukti lebih optimal dibandingkan distribusi merata (RQ2).
Hasil optimasi mengungkap bahwa Visual Shopping Ads (VSA, 48,4%) dan Live Shopping Ads (LSA, 33,4%)
memberikan marginal return tertinggi, sementara PSA, Awareness, dan GMV Max menunjukkan kontribusi lebih
rendah dengan diminishing return  yang lebih cepat. Secara metodologis, pendekatan Bayesian terbukti
mengungguli MMM konvensional tidak hanya dalam akurasi prediksi, tetapi juga dalam transparansi
ketidakpastian estimasi, keunggulan kritis bagi pengambil keputusan pemasaran digital.
Bagi praktisi, tiga rekomendasi operasional yang dapat segera diterapkan adalah: (1) realokasi minimal 80%
anggaran iklan ke VSA dan LSA untuk memaksimalkan ROI; (2) optimasi sesi live streaming pada hari Jumat–
Minggu dan menjelang tanggal gajian, sesuai interaksi positif yang diidentifikasi model; serta (3) menjalankan
ulang optimasi setiap kuartal dengan data terbaru, mengingat dinamika algoritma TikTok yang cepat berubah.
Keterbatasan penelitian ini meliputi cakupan satu platform dan periode observasi 15 bulan. Agenda lanjutan
mencakup: (1) multi-platform extension  pada TikTok, Instagram Ads, dan Shopee Ads; (2) rolling optimization
berbasis data mingguan via API TikTok Ads; dan (3) validasi melalui A/B test minimum 8 minggu untuk mengukur
dampak ROI aktual. Secara keseluruhan, integrasi BMMM dan BO membuka arah baru dalam analitik pemasaran
digital berbasis probabilistik dan memberikan kontribusi bagi kemajuan teori serta praktik keputusan pemasaran
di Indonesia.
DAFTAR PUSTAKA
[1] S. Kemp, “Digital 2025: Global Overview Report,” Feb. 2025. [Online]. Available:
https://datareportal.com/reports/digital-2025-global-overview-report
[2] Dentsu, “Global Ad Spend Forecasts December 2025,” Dec. 2025. [Online]. Available: https://insight.dentsu.com/ad-
spend-dec-2025/
[3] Statista, “Advertising revenue of Google from 2001 to 2024,” Statista. [Online]. Available:
https://www.statista.com/statistics/266249/advertising-revenue-of-
google/?srsltid=AfmBOoohwTTQTfbuXXnGx2f_f4iBtaKQxpj4_znE-OOLyCg2WN_d3PbB
[4] eMarketer, “Worldwide Ad Spending Forecast 2025,” eMarketer. [Online]. Available:
https://www.emarketer.com/content/worldwide-ad-spending-forecast-2025#page-report
[5] B. R. Gordon, F. Zettelmeyer, N. Bhargava, and D. Chapsky, “A Comparison of Approaches to Advertising Measurement:
Evidence from Big Field Experiments at Facebook,” Marketing Science, vol. 38, no. 2, pp. 193–225, Mar. 2019, doi:
10.1287/mksc.2018.1135.
[6] J. T. Yun, C. M. Segijn, S. Pearson, E. C. Malthouse, J. A. Konstan, and V. Shankar, “Challenges and Future Directions
of Computational Advertising Measurement Systems,” J. Advert. , vol. 49, no. 4, pp. 446–458, 2020, doi:
10.1080/00913367.2020.1795757.

Idealis: Indonesia Journal Information System
Volume 9, Nomor 2, Juli 2026
ISSN 2684-7280 (online)
Halaman 204-213
available online at http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index

Fajar Legianto Asmin | http://jom.fti.budiluhur.ac.id/index.php/IDEALIS/index |  Page 213
[7] Y. Jin, Y. Wang, Y. Sun, D. Chan, and J. Koehler, “Bayesian Methods for Media Mix Modeling with Carryover and Shape
Effects,” Google Research, Apr. 2017.
[8] H. Chen, M. Zhang, L. Han, and A. Lim, “Hierarchical marketing mix models with sign constraints,” J. Appl. Stat., vol.
48, no. 13–15, pp. 2944–2960, 2021, doi: 10.1080/02664763.2021.1946020.
[9] X. Ni, Y. Zhang, Y. Pu, M. Wei, and Q. Lou, “A Personalized Causal Inference Framework for Media Effectiveness Using
Hierarchical Bayesian Market Mix Models,” Journal of Advanced Computing Systems (JACS) , vol. 3, no. 9, pp. 9–23,
2023.
[10] A. Jha, A. Bhatia, and K. Tiwari, “Bayesian Deep Learning Meets Self-Attention: A Risk-Aware Approach to
Advertisement Optimization,” IEEE Access, vol. 13, pp. 86413–86429, 2025, doi: 10.1109/ACCESS.2025.3570537.
[11] K. H. Brodersen, F. Gallusser, J. Koehler, N. Remy, and S. L. Scott, “Inferring causal impact using Bayesian structural
time-series models,” Ann. Appl. Stat., vol. 9, no. 1, 2015, doi: 10.1214/14-AOAS788.
[12] C. Gong et al., “CausalMMM: Learning Causal Structure for Marketing Mix Modeling,” in Proceedings of the 17th ACM
International Conference on Web Search and Data Mining , New York, NY, USA: ACM, 2024, pp. 238–246. doi:
10.1145/3616855.3635766.
[13] M. Gigli and F. Stella, “Multi-armed bandits for performance marketing,” Int. J. Data Sci. Anal., vol. 20, no. 1, pp. 151–
165, Jun. 2025, doi: 10.1007/s41060-023-00493-7.
[14] W. Gao, X. Meng, and Y. Zhang, “Multimodal Reinforcement Learning for Dynamic Cross-Media Advertising Budget
Allocation Via DDPG and PPO Combined with Meta-Learning and Adversarial Training,” Informatica, vol. 49, no. 30,
2025, doi: 10.31449/inf.v49i30.11440.
[15] M. Yang, Q. Cao, L. Tong, and J. Shi, “Reinforcement learning-based optimization strategy for online advertising budget
allocation,” in 2025 4th International Conference on Artificial Intelligence, Internet and Digital Economy (ICAID), IEEE,
Apr. 2025, pp. 115–118. doi: 10.1109/ICAID65275.2025.11034517.
[16] Z. Pan, “A Reinforcement Learning Approach for Adaptive Budget Allocation in Pharmaceutical Digital Marketing:
Maximizing ROI Across Patient Journey Touchpoints,” Journal of Sustainability, Policy, and Practice, vol. 1, no. 4, 2025.
[17] H. Wang et al., “ROI-Constrained Bidding via Curriculum-Guided Bayesian Reinforcement Learning,” in Proceedings of
the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining , New York, NY, USA: ACM, 2022, pp.
4021–4031. doi: 10.1145/3534678.3539211.
[18] Y. Wang, “Application of Bayesian Optimization in Periodic Delivery,” in Proceedings of the 2025 6th International
Conference on Computer Information and Big Data Applications , New York, NY, USA, 2025, pp. 556–561. doi:
10.1145/3746709.3746805.
[19] R. A. Astudillo, D. R. Jiang, M. Balandat, E. Bakshy, and P. I. Frazier, “Multi-Step Budgeted Bayesian Optimization with
Unknown Evaluation Costs,” in 35th Conference on Neural Information Processing Systems (NeurIPS 2021), Nov. 2021.
[20] S. Daulton, M. Balandat, and E. Bakshy, “Differentiable expected hypervolume improvement for parallel multi-objective
Bayesian optimization,” in NIPS’20: Proceedings of the 34th International Conference on Neural Information Processing
Systems, Vancouver: Curran Associates Inc., Dec. 2020, pp. 9851–9864.
[21] I. R. Arief and I. Novita, “Penerapan E-Commerce Untuk Mengoptimalkan Penjualan Pada Toko Gita Giza,” IDEALIS:
Indonesia Journal Information System, vol. 4, no. 1, pp. 127–136, 2021, doi: 10.36080/idealis.v4i1.2823.
[22] F. R. R. Santoso and E. I. H. Ujianto, “A decision support system for the determination of additional stock items using the
Topsis method based on Android,” IDEALIS: Indonesia Journal Information System, vol. 8, no. 1, pp. 42–52, 2025, doi:
10.36080/idealis.v8i2.3339.
[23] R. A. Zilasar, Y. A. Pranoto, and F. X. Ariwibisono, “Sistem Pendukung Keputusan Pemilihan Produk Kaca Dan Cermin
Menggunakan Metode Fuzzy AHP,” IDEALIS: Indonesia Journal Information System, vol. 9, no. 1, pp. 21–29, 2026, doi:
10.36080/idealis.v9i1.3617.
[24] S. N. Windrasari, H. Margono, and Y. A. N. S. Putra, “Predictive Sales Analysis in Coffee Shops Using the Random
Forest Algorithm,” MALCOM: Indonesian Journal of Machine Learning and Computer Science , vol. 5, no. 3, pp. 1000–
1011, 2025, doi: 10.57152/malcom.v5i3.2023.
