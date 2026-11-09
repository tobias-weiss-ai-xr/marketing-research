---
title: Customer Segmentation Using K-Means Clustering Algorithm for Digital Marketing Strategy
url: https://doi.org/10.36520/jai.v10i1.320
category: digital-marketing
subcategory: framework
date: 2026-06
venue: JURNAL ARMADA INFORMATIKA
authors:
- Penda Sudarto Hasugian
- Agustina Simangunsong
- Meriana Manik
source: openalex-oa
pdf_url: https://jurnal.stmikmethodistbinjai.ac.id/jai/article/download/320/166
pages: 12
chars: 36817
fetched_at: '2026-11-08T17:56:36+00:00'
kb_version: 1
---

# Customer Segmentation Using K-Means Clustering Algorithm for Digital Marketing Strategy

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 251
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
Segmentasi Pelanggan Menggunakan Algoritma K-Means Clustering
Strategi Digital Marketing

Customer Segmentation Using K-Means Clustering Algorithm for Digital
Marketing Strategy
Penda Sudarto Hasugian1*, Agustina Simangunsong2, Meriana Manik3, Hotnitaria Tarihoran4

1,3,4 Bisnis Digital, STMIK Pelita Nusantara, Medan, Indonesia
2 Teknik Informatika, STMIK Pelita Nusantara, Medan, Indonesia
Email: 1*penda.hasugian@gmail.com, 2Agustinasimangunsong93@gmail.com, 3meirianna@gmail.com,
4Hotni78@gmail.com
Email Penulis Korespondensi: penda.hasugian@gmail.com

Abstrak− Perkembangan teknologi informasi dan meningkatnya persaingan bisnis mendorong perusahaan untuk
memanfaatkan data transaksi pelanggan sebagai dasar dalam pengambilan keputusan. Namun, banyak pelaku usaha yang belum
mengoptimalkan pemanfaatan data tersebut untuk memahami perilaku pelanggan dan menyusun strategi pemasaran yang lebih
efektif. Penelitian ini bertujuan untuk menerapkan algoritma K-Means Clustering dalam melakukan segmentasi pelanggan pada
RM Serdang menggunakan pendekatan Recency, Frequency, dan Monetary (RFM) guna mendukung penyusunan strategi
digital marketing berbasis data. Penelitian diawali dengan pengolahan data transaksi pelanggan melalui perhitungan nilai
Recency, Frequency, dan Monetary (RFM),  yang selanjutnya dinormalisasi menggunakan metode Min -Max Normalization.
Penentuan jumlah cluster dilakukan menggunakan Elbow Method dan menghasilkan empat cluster sebagai jumlah cluster yang
optimal. Implementasi algoritma K-Means Clustering  dilakukan melalui perhitungan Euclidean Distance  dan pembaruan
centroid secara iteratif hingga mencapai kondisi konvergen pada Iterasi ke -5. Berdasarkan hasil penelitian, sebanyak 20 data
pelanggan yang digunakan sebagai sampel perhitungan manual berhasil dikelompokkan ke dalam empat cluster, yaitu Cluster
1 (Pelanggan Aktif) yang terdiri atas 7 pelanggan, Cluster 2 (Pelanggan Bernilai Tinggi) yang terdiri atas 4 pelanggan, Cluster
3 (Pelanggan Potensial) yang terdiri atas 5 pelanggan, dan Cluster 4 (Pelanggan Kurang Aktif) yang terdiri atas 4 pelanggan.
Hasil segmentasi menunjukkan bahwa setiap cluster memiliki karakteristik perilaku transaksi yang berbeda berdasarkan atribut
RFM. Temuan ini menunjukkan bahwa kombinasi metode RFM dan algoritma K -Means Clustering mampu menghasilkan
segmentasi pelanggan yang representatif dan da pat dimanfaatkan sebagai dasar dalam penyusunan strategi digital marketing
yang lebih tepat sasaran, seperti program loyalitas, promosi yang dipersonalisasi, dan strategi retensi pelanggan. Dengan
demikian, penelitian ini membuktikan bahwa penerapan algori tma K-Means Clustering  berbasis RFM dapat memberikan
kontribusi dalam mendukung pengambilan keputusan berbasis data ( data-driven decision making ) serta meningkatkan
efektivitas strategi pemasaran pada RM Serdang.
Kata Kunci: Segmentasi Pelanggan, K-Means Clustering, RFM, Data Mining, Digital Marketing
Abstract− The rapid advancement of information technology and increasing business competition have encouraged
organizations to utilize customer transaction data as a basis for decision -making. However, many businesses have not yet
optimized the use of such data to u nderstand customer behavior and develop more effective marketing strategies. This study
aims to implement the K-Means Clustering algorithm for customer segmentation at RM Serdang using the Recency, Frequency,
and Monetary (RFM) approach to support data-driven digital marketing strategies. The study began with processing customer
transaction data by calculating Recency, Frequency, and Monetary values, which were subsequently normalized using the Min-
Max Normalization method. The optimal number of clusters was determined using the Elbow Method, resulting in four clusters.
The K-Means algorithm was then implemented through Euclidean Distance calculations and iterative centroid updates until
convergence was achieved at the fifth iteration.  The results indicate that 20 customer records used as manual calculation
samples were successfully grouped into four clusters: Cluster 1 (Active Customers) consisting of 7 customers, Cluster 2 (High-
Value Customers) consisting of 4 customers, Cluster 3 (Po tential Customers) consisting of 5 customers, and Cluster 4 (Less
Active Customers) consisting of 4 customers. The segmentation results demonstrate that each cluster exhibits distinct
transactional behavior characteristics based on the RFM attributes. Thes e findings indicate that the combination of the RFM
method and the K-Means Clustering algorithm is capable of producing representative customer segmentation and can serve as
a foundation for developing more targeted digital marketing strategies, such as loyalty programs, personalized promotions, and
customer retention initiatives.  In conclusion, this study demonstrates that the implementation of RFM -based K -Means
Clustering contributes to supporting data -driven decision -making and enhancing the effectiveness of digital marketing
strategies at RM Serdang.

Keywords: Customer Segmentation, K-Means Clustering, RFM, Data Mining, Digital Marketing.
1. PENDAHULUAN
Perkembangan teknologi informasi telah mendorong transformasi signifikan dalam dunia bisnis, khususnya
pada sektor bisnis digital. Perusahaan dituntut untuk mampu beradaptasi dengan perubahan perilaku konsumen
yang semakin dinamis serta memanfaatkan data s ebagai dasar dalam pengambilan keputusan strategis. Dalam

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 252
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
konteks ini, pemanfaatan data pelanggan menjadi sangat penting untuk meningkatkan efektivitas strategi
pemasaran dan daya saing perusahaan. Namun demikian, masih banyak pelaku usaha yang belum mampu
mengoptimalkan pemanfaatan data pelanggan, khususnya data  transaksi. Data yang tersedia umumnya hanya
digunakan sebagai arsip operasional tanpa dilakukan analisis lebih lanjut untuk menghasilkan informasi yang
bernilai. Padahal, data tersebut dapat digunakan untuk memahami pola perilaku pelanggan dan mendukung
pengambilan keputusan pemasaran yang lebih tepat sasaran[1][2].[3] Salah satu pendekatan yang dapat digunakan
untuk mengatasi permasalahan tersebut adalah segmentasi pelanggan. Segmentasi pelanggan memungkinkan
perusahaan untuk mengelompokkan konsumen berdasarkan karakteristik tertentu sehingga dapat memahami
kebutuhan dan preferensi masing-masing kelompok secara lebih mendalam. Dengan demikian, perusahaan dapat
merancang strategi pemasaran yang lebih efektif, seperti promosi tertarget, program loyalitas, dan peningkatan
hubungan dengan pelanggan. [4] Dalam perkembangannya, teknik data mining telah banyak digunakan untuk
mendukung proses segmentasi pelanggan secara otomatis dan akurat. Data mining merupakan proses penggalian
informasi atau pola tersembunyi dari data dalam jumlah besar yang dapat diguna kan sebagai dasar pengambilan
keputusan. Dalam konteks pemasaran, penerapan data mining pada segmentasi pelanggan terbukti mampu
membantu perusahaan dalam menentukan target pasar dan strategi pemasaran yang lebih efektif[5].[6] Salah satu
metode yang umum digunakan dalam segmentasi pelanggan adalah algoritma K-Means Clustering. Algoritma ini
termasuk dalam teknik unsupervised learning yang mampu mengelompokkan data berdasarkan tingkat kemiripan
antar objek. K -Means banyak diguna kan karena memiliki keunggulan dalam hal kesederhanaan, efisiensi, dan
kemampuannya dalam mengolah data dalam jumlah besar. Selain itu, metode ini juga sering dikombinasikan
dengan model RFM ( Recency, Frequency, Monetary ) untuk menghasilkan segmentasi pelanggan yang lebih
representatif.[7][8]. Model RFM merupakan salah satu pendekatan yang paling banyak digunakan dalam analisis
perilaku pelanggan. Model ini mengukur nilai pelanggan berdasarkan tiga dimensi utama, yaitu waktu transaksi
terakhir (recency), frekuensi pembelian (frequency), dan nilai transaksi (monetary). Dengan menggunakan model
ini, perusahaan dapat mengidentifikasi pelanggan yang bernilai tinggi, pelanggan potensial, serta pelanggan yang
perlu mendapatkan perhatian khusus melalui strategi pemasaran tertentu. [9]. Penelitian-penelitian sebelumnya
menunjukkan bahwa kombinasi antara model RFM dan teknik clustering, seperti K-Means, mampu menghasilkan
segmentasi pelanggan yang efektif serta memberikan insight yang berguna dalam penyusunan strategi pemasaran
berbasis data. Selain itu, hasil segmentasi tersebut juga dapat digunakan untuk meningkatkan loyalitas pelanggan,
mengoptimalkan penjualan, serta meningkatkan efisiensi kampanye pemasaran.[10] Berdasarkan uraian tersebut,
dapat disimpulkan bahwa pemanfaatan teknik data mining melalui algoritma K-Means Clustering  dengan
pendekatan RFM memiliki potensi yang besar dalam mendukung strategi digital marketing yang lebih efektif dan
tepat sasaran[11], [12], [13]. Oleh karena itu, penelitian ini dilakukan untuk mengembangkan model segmentasi
pelanggan berbasis data transaksi guna menghasilkan rekomendasi strategi digital marketing yang berbasis data
(data-driven marketing), sehingga dapat meningkatkan daya saing b isnis, khususnya pada sektor ritel dan bisnis
digital[14], [15].
2. METODOLOGI PENELITIAN
2.1 Metodolongi Penelitian
Metodologi penelitian ini menggunakan pendekatan data mining dengan teknik clustering untuk melakukan
segmentasi pelanggan berdasarkan data transaksi. Secara umum, tahapan penelitian mengacu pada alur Knowledge
Discovery in Database (KDD) yang disusun sesuai kebutuhan penelitian seperti pada gambar 1 berikut:

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 253
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026

Gambar 1. Tahapan Penelitian
2.2 Tahapan pada Penelitian
Adapun tahapan penelitian yang dilakukan yaitu sebagai berikut:
1. Pengumpulan Data
Tahap pertama adalah pengumpulan data, yaitu proses mengambil data transaksi pelanggan dari objek penelitian,
seperti toko atau bisnis ritel. Data yang dikumpulkan biasanya berupa informasi pelanggan, tanggal transaksi,
jumlah pembelian, dan nilai transaksi. Data ini menjadi fondasi utama dalam penelitian.
2. Analisa Data
Proses Analisa data bertujuan untuk memahami karakteristik data secara awal. Pada tahap ini dilakukan
eksplorasi data untuk mengetahui struktur data, distribusi nilai, serta mendeteksi adanya data yang tidak lengkap
atau tidak konsisten. Analisis awal ini penting untuk menentukan langkah pengolahan data berikutnya.
3. Pra-pemrosesan Data (Data Preprocessing)
Pada tahap pra -pemrosesan data (data preprocessing). Pada tahap ini dilakukan pembersihan data ( data
cleaning), seperti menghapus data duplikat, menangani data yang hilang ( missing value), serta menyaring data
yang tidak relevan. Proses ini bertujuan untuk meningkatkan kualitas data agar siap digunakan dalam analisis
lebih lanjut.
4. Transformasi dan Pemodelan Data
Tahap transformasi dan pemodelan data, di mana data yang telah dibersihkan diubah ke dalam bentuk yang
sesuai untuk analisis. Dalam penelitian ini, data ditransformasikan menggunakan model RFM (Recency,
Frequency, Monetary) untuk merepresentasikan perilaku pelanggan. Selain itu, dilakukan normalisasi data agar
setiap variabel memiliki skala yang seimbang sebelum masuk ke proses clustering.
5. Proses Clustering (K-Means)
Tahap inti proses clustering menggunakan algoritma K-Means. Pada tahap ini, data pelanggan dikelompokkan
ke dalam beberapa cluster berdasarkan tingkat kemiripan karakteristiknya. Proses ini melibatkan penentuan
jumlah cluster (k), perhitungan jarak antar data, serta iterasi hingga terbentuk kelompok yang optimal.
6. Interpretasi Hasil (Knowledge Interpretation)
Tahap terakhir adalah interpretasi hasil (knowledge interpretation). Hasil clustering yang diperoleh dianalisis
untuk memahami karakteristik masing -masing kelompok pelanggan. Setiap cluster kemudian diberikan label,
seperti pelanggan loyal, pelanggan poten sial, atau pelanggan tidak aktif. Hasil interpretasi ini selanjutnya
digunakan sebagai dasar dalam menyusun strategi digital marketing yang tepat sasaran.
.
3. HASIL DAN PEMBAHASAN
3.1 Hasil Penelitian
Dataset yang digunakan dalam penelitian ini merupakan data pelanggan dan data transaksi yang berasal dari
Rumah Makan (RM) Serdang selama periode Oktober 2025 hingga Desember 2025. Pemilihan periode tersebut
didasarkan pada pertimbangan bahwa data transaksi pada rentang waktu tersebut mampu merepresentasikan

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 254
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
aktivitas pembelian pelanggan terkini sehingga lebih relevan untuk digunakan dalam proses segmentasi pelanggan.
Selain itu, penggunaan data transaksi yang relatif baru memungkinkan hasil segmentasi yang diperoleh dapat
digunakan sebagai dasar dalam penyusu nan strategi digital marketing yang lebih sesuai dengan kondisi dan
perilaku pelanggan saat ini. Data yang digunakan dalam penelitian terdiri atas dua kelompok utama, yaitu data
pelanggan dan data transaksi. Data pelanggan berfungsi sebagai identitas pelan ggan yang digunakan untuk
menghubungkan setiap transaksi dengan pelanggan yang bersangkutan, sedangkan data transaksi digunakan
sebagai sumber utama dalam proses analisis perilaku pelanggan. Melalui data transaksi tersebut, peneliti dapat
mengidentifikasi pola pembelian pelanggan berdasarkan frekuensi transaksi, waktu transaksi terakhir, serta nilai
pembelian yang dilakukan selama periode pengamatan. Dataset pelanggan terdiri dari 100 pelanggan aktif yang
terdaftar dalam sistem RM Serdang dengan kode unik mulai dari PL001 hingga PL100. Setiap pelanggan memiliki
atribut yang meliputi ID Pelanggan, Nama Pelanggan, Usia, Kanal Pemesanan, dan Metode Pembayaran. Atribut-
atribut tersebut tidak digunakan secara langsung dalam proses clustering , namun berfungsi sebagai data
pendukung untuk membantu menginterpretasikan karakteristik masing -masing kelompok pelanggan yang
terbentuk setelah proses segmentasi dilakukan. Dengan adanya informasi profil pelanggan, hasil segmentasi yang
diperoleh dapat dianalisis secara lebih komprehensif sehingga memudahkan pihak manajemen dalam menentukan
strategi pemasaran yang tepat untuk setiap kelompok pelanggan. Data pelanggan merupakan data identitas yang
digunakan untuk membedakan setiap pelanggan pada proses analisis. Untuk menjaga p rivasi, nama pelanggan
dianonimkan menggunakan format PL001 dan Seterusnya. Data transaksi yang digunakan dalam proses k-means
clustering diambil sebanyak 20 data transaksi sebagai sample perhintungan. Seperti tabel 1.

Tabel 1. Data Transasi Pelanggan

3.1.1 Preprosesing Data
Preprocessing data merupakan tahapan penting dalam penelitian data mining yang bertujuan untuk
meningkatkan kualitas data sebelum dilakukan proses analisis menggunakan algoritma K-Means Clustering.
Tahap ini dilakukan untuk memastikan bahwa data yang digunakan telah memenuhi kriteria kelengkapan,
konsistensi, dan validitas sehingga mampu menghasilkan model segmentasi pelanggan yang akurat dan dapat
dipertanggungjawabkan. Proses preprocessing meliputi empat tahapan utama, yaitu validasi data (data validation),
pembersihan data (data cleaning), integrasi data (data integration), dan transformasi data (data transformation).
1. Validasi Data (Data Validation)
Tahap validasi data bertujuan untuk memastikan bahwa seluruh data yang digunakan dalam penelitian
telah memenuhi persyaratan analisis. Validasi dilakukan dengan memeriksa keberadaan atribut utama,
konsistensi relasi antar tabel, serta memastikan tidak terdapat data yang hilang atau tidak sesuai.
Berdasarkan hasil validasi, seluruh data dinyatakan valid dan dapat digunakan pada tahap selanjutnya.
2. Pembersihan Data (Data Cleaning)

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 255
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
Tahap pembersihan data dilakukan untuk mengidentifikasi dan menghilangkan data yang berpotensi
menurunkan kualitas analisis, seperti: Missing value, Data duplikat. Kesalahan format tanggal, Kesalahan
perhitungan nilai transaksi.
3. Integrasi Data (Data Integration)
Setelah melalui tahap validasi dan pembersihan, langkah berikutnya adalah mengintegrasikan data
pelanggan dan data transaksi. Integrasi dilakukan menggunakan atribut ID Pelanggan sebagai primary
key. Proses integrasi bertujuan untuk menghasilkan dataset ya ng terstruktur dan memudahkan proses
analisis perilaku pelanggan
4. Transformasi Data (Data Transformation)
Tahap transformasi data dilakukan untuk mengubah data transaksi mentah menjadi variabel yang dapat
digunakan pada algoritma K -Means. Proses transformasi dilakukan terhadap seluruh data transaksi
pelanggan RM Serdang yang berjumlah 500 transaksi selama peri ode 1 Oktober 2025 hingga 31
Desember 2025. Setiap transaksi dikelompokkan berdasarkan ID Pelanggan sehingga diperoleh tiga
variabel utama, yaitu:
1. Recency (R) yaitu jumlah hari sejak pelanggan melakukan transaksi terakhir hingga tanggal referensi
2. Frequency (F) yaitu jumlah transaksi yang dilakukan pelanggan selama periode penelitian. Dengan
3. Monetary (M) yaitu total nilai transaksi yang dilakukan pelanggan selama periode penelitian.
5. Perhitungan Recency, Frequency, dan Monetary (RFM)
Metode RFM ( Recency, Frequency, Monetary) merupakan teknik analisis pelanggan yang digunakan
untuk mengukur tingkat aktivitas dan nilai pelanggan berdasarkan riwayat transaksi. Pada penelitian ini,
metode RFM digunakan untuk mentransformasikan data transaksi pelanggan RM Serdang menjadi tiga
variabel numerik yang selanjutnya digunakan sebagai input pada algoritma K-Means Clustering.
Perhitungan dilakun dengan terhadap data transaksi yang berjumlah 500 transaksi selama periode 1
Oktober 2025 hingga 31 Desember 2025 dengan Tanggal referensi 1 Januari 2026.
A. Perhitungan Recency (R)
Perhitungan dilakukan untuk masing masing data transaksi pelanggan, berikut ini perhitungan untuk
data PL001.
Diketahui:
Treferensi  = 1 Januari 2026
T transaksi terakhir  = 26 Desember 2025
Sehingga diperoleh nilai Recency (R) untuk data PL001 sebagai berikut:
R = 1 Januari 2026 − 26 Desember 2025
R = 6 hari
B. Frequency (F)
Frequency digunakan untuk mengukur seberapa sering pelanggan melakukan transaksi selama
periode penelitian, dari data transaksi diperoleh PL001 memiliki 8 transaksi yaitu pada transaksi
yaitu id transaksi TR028, TR0390, TR0390, TR0425, TR0427, TR0145, TR0324, TR0001, dan
TR0235. Sehingga dilakukan peritungan Frequency sebagai berikut:
F1=1+1+1+1+1+1+1+1
F1=8
C. Monetary (M)
Monetary merupakan total nilai transaksi yang dilakukan pelanggan selama periode penelitian.
Berdasarkan data transaksi PL001:
1. TR0288 = Rp54.000
2. TR0390 = Rp21.000
3. TR0425 = Rp50.000
4. TR0427 = Rp285.000
5. TR0145 = Rp10.000
6. TR0324 = Rp36.000
7. TR0001 = Rp95.000

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 256
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
8. TR0235 = Rp36.000
Maka dilakukan perhitungan untuk nilai Monetary PL001:
M1 = 54.000+21.000+50.000+285.000+10.000+36.000+95.000+36.000
M1 = 587.000
Berdasarkan hasil perhitunga menggunakan metode Recency, Frequency, dan Monetary (RFM) ,
diperoleh nilai Recency sebesar 6 hari, Frequency sebanyak 8 transaksi, dan Monetary sebesar
Rp587.000 untuk pelanggan PL001.
Tabel 2. Hasil perhitungan RFM
ID_Pelanggan Recency Frequency Monetary
PL001 6 8 587000
PL002 1 11 640000
PL003 6 7 401000
PL004 12 7 189000
PL005 8 14 1091000
………………… ………… …………….. ……………..
PL100 9 3 150000
Berikutnya dilakukan normalisasi data, hasil normalisasi seperti pada tabel 3. Berikut
Tabel 3. Hasil Normalisasi RFM
ID_Pelanggan Recency_N Frequency_N Monetary_N
PL001 0,067568 0,538462 0,456113
PL002 0 0,769231 0,497649
PL003 0,067568 0,461538 0,310345
PL004 0,148649 0,461538 0,144201
PL005 0,094595 1 0,851097
……………… ……………… ……………… ………………
PL100 0,108108 0,153846 0,113636
3.1.2 Implementasi Algoritma K-Means Clustering
Implementasi Algoritma K-Means dilakukan terhadap 100 data pelanggan RM Serdang. Namun, untuk
mempermudah penyajian dan penjelasan proses perhitungan, ditampilkan perhitungan manual menggunakan 20
data pelanggan yaitu Pelanggan 1 sampai Pelanggan ke 20 (PL001 –PL020). Jumlah cluster yang dibentuk
berdasarkan Elbow Method diperoleh jumlah cluster optimal K=4 seperti pada tabel 4.
Tabel 4. Jumlah cluster yang dibentuk
Cluster Nama Cluster
C1 Pelanggan Aktif
C2 Pelanggan Bernilai Tinggi
C3 Pelanggan Potensial
C4 Pelanggan Kurang Aktif
Selanjutkan  Centroid awal yang digunakan Adalah diambil secara acar dari data PL001, PL007,
PL0013, PL0020 seperti tabel 5 berikut
Tabel 5 Data Centroid Awal

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 257
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
Cluster ID Pelanggan R F M
C1 PL001 0,067568 0,538462 0,456113
C2 PL007 0,054054 0,769231 0,408307
C3 PL013 0,081081 0,615385 0,420846
C4 PL020 0,081081 0,692308 0,266458

3.1.3 Menghitung Euclidean Distance
Untuk menghitung Euclidean Distance atau jarak antara data ke-𝑖 dengan pusat cluster (centroid) ke-𝑘
digunakan rumus Algoritma K-Means menggunakan rumus utama yaitu:
𝒅(𝒙𝒊, 𝑪𝒌) = √∑ (𝒙𝒊𝒋−𝑪𝒌𝒋 𝒎 𝒋=𝟏 )2
Dengan keterangan:
• 𝑑(𝑥𝑖, 𝐶𝑘)= jarak antara data 𝑥𝑖dengan centroid 𝐶𝑘
• 𝑥𝑖𝑗= nilai atribut ke-𝑗 pada data ke-𝑖
• 𝐶𝑘𝑗= nilai atribut ke-𝑗 pada centroid cluster ke-𝑘
• 𝑚= jumlah atribut atau variabel
• 𝑖= indeks data pelanggan
• 𝑘= indeks cluster
Sehingga dapat dilakukan perhitungan pada iterasi pertama:
1. Menghitung Jarak PL001 terhadap Cluster 1 (C1)
Karena C1 merupakan centroid awal yang berasal dari PL001, maka:
 d(PL001,C1)
= √(RPL001 − RC1)² +  (FPL001 − FC1)² +  (MPL001 − MC1)²
= √(0,067568 − 0,067568)² +  (0,538462 − 0,538462)² +  (0,456113 − 0,456113)²
= √(0,000000)² +  (0,000000)² +  (0,000000)²
= √0, 000000 +  0, 000000 +  0, 000000
= √0, 000000
= 0,000000
2. Menghitung Jarak PL001 terhadap Cluster 2 (C2)
d(PL001,C2)
= √(RPL001 − RC2)² + (FPL001 − FC2)² + (MPL001 − MC2)²
=√(0,067568 − 0,054054)² + (0,538462 − 0,769231)² + (0,456113 − 0,408307)²
= √(0,013514)² +  (−0,230769)² + (0,047806)²
= √(0,000183) +  (0,053255) +  (0,002285)
= √(0,055723)
= 0,236056
3. Menghitung Jarak PL001 terhadap Cluster 3 (C3)
d(PL001,C3)
= √(RPL001 − RC3)² + (FPL001 − FC3)² + (MPL001 − MC3)²

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 258
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
= √(0,067568 − 0,081081)² + (0,538462 − 0,615385)² + (0,456113 − 0,420846)²
= √(−0,013513)² +  (−0,076923)² +  (0,035267)²

=  √(0,000183) +  (0,005917) +  (0,001244)
= √(0,007344)
= 0,085694
4. Menghitung Jarak PL001 terhadap Cluster 4 (C4)
d(PL001,C4)
= √(RPL001 − RC4)² + (FPL001 − FC4)² + (MPL001 − MC4)²
= √(0,067568 − 0,081081)² + (0,538462 − 0,692308)² +  (0,456113 − 0,266458)²
=  √(−0,013513)² +  (−0,153846)² +  (0,189655)²
= √(0,000183) +  (0,023668) +  (0,035969)
= √(0,059820)
= 0,244582
Hasil Penentuan Cluster Iterasi ke-1
ID C1 C2 C3 C4 Cluster
PL001 0 0,236056 0,085694 0,244582 C1
Adapun Anggota Cluster Iterasi ke-1yaitu:
Tabel 6 Anggota Cluster Iterasi ke-1
Cluster Anggota cluster
C1 PL001, PL003, PL008, PL010, PL011, PL014, PL018
C2 PL002, PL005, PL006, PL007, PL017, PL019
C3 PL009, PL012, PL013
C4 PL004, PL015, PL016, PL020
3.1.4 Perhitungan Centroid Baru
Untuk menghitung centroid baru digunakan rumus berikut:
𝑪𝒌 = 𝟏 𝒏𝒌 ∑ 𝒙𝒊
𝒏𝒌
𝒊=𝟏

Keterangan:
• 𝐶𝑘= centroid baru cluster ke-𝑘
• 𝑛𝑘= jumlah data yang berada pada cluster ke-𝑘
• 𝑥𝑖= nilai data anggota cluster
Berdasarkan hasil iterasi 1, maka dilakukan perhitungan centroid baru yaitu: Menentukan nilai Centroid Baru
C1, C2, C3 dan C4. Berikut perhitungan centroid baru untuk C1:
Nilai Recency (R)
R(C1)  = (RPL001+RPL003+RPL008+RPL010+RPL011+RPL014+RPL018)/7
= (0,067568+0,027027+0,054054+0,040541+0,054054+0,121622+0,121622)/7
= 0,486488/7
= 0,069498
Nilai Frequency (F)

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 259
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
F(C1) = (0,538462+0,384615+0,615385+0,307692+0,384615+0,692308+0,307692)/7
= 3,230769/7
= 0,461538
Nilai Monetary (M)
M(C1) = (0,456113+0,357842+0,401257+0,223517+0,425168+0,535278+0,394145)/7
= 2,793320/7
= 0,399046
Perhitungan dilakuan sampai dengan C4 sehingga diperoleh centroid baru untuk iterasi 2 seperti pada tabel 7
Tabel 7 Centroid baru Iterasi ke-1
Cluster Recency Frequency Monetary
C1' 0,069498 0,461538 0,399046
C2' 0,058559 0,782051 0,671119
C3' 0,067568 0,564103 0,389095
C4' 0,091216 0,557693 0,246426
Berdasarkan hasil pembaharuan centroid pada Iterasi 1,2 dan ke-3, dilakukan kembali proses perhitungan
Euclidean Distance terhadap seluruh data pelanggan. Hasil perhitungan menunjukkan bahwa sebagian besar
anggota cluster telah menunjukkan pola yang stabil dan tidak mengalami perpindahan cluster yang signifikan.
Tabel 8 Hasil Centroid Iterasi ke-4
Cluster Recency Frequency Monetary
C1 0,047297 0,461538 0,29663
C2 0,081081 0,794872 0,932079
C3 0,085586 0,666667 0,432776
C4 0,094595 0,461538 0,179859
Anggota untuk setiap cluster pada iterasi 4.
Tabel 9 Anggota cluster Iterasi ke-4
Cluster Anggota Cluster Jumlah
Cluster 1 PL003, PL008, PL009, PL010, PL011, PL014, PL018 7
Cluster 2 PL002, PL005, PL017, PL019 4
Cluster 3 PL001, PL006, PL007, PL012, PL013 5
Cluster 4 PL004, PL015, PL016, PL020 4
Iterasi ke -5 dilakukan menggunakan centroid hasil Iterasi ke -4. Tujuan dari iterasi ini adalah untuk
memastikan apakah masih terdapat perpindahan anggota cluster atau tidak. Apabila tidak ditemukan perubahan,
maka algoritma dinyatakan telah mencapai kondisi konvergen.
Tabel 10 Hasil Centroid Iterasi ke-5

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 260
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
Cluster Recency Frequency Monetary
C1 0,056757 0,476923 0,29279
C2 0,081081 0,794872 0,932079
C3 0,085586 0,666667 0,432776
C4 0,094595 0,435897 0,147335
Anggota untuk setiap cluster pada iterasi 5.
Tabel 11 Anggota Cluster pada Iterasi ke-5
Cluster Anggota Cluster Jumlah
Cluster 1 PL003, PL008, PL009, PL010, PL011, PL014, PL018 7
Cluster 2 PL002, PL005, PL017, PL019 4
Cluster 3 PL001, PL006, PL007, PL012, PL013 5
Cluster 4 PL004, PL015, PL016, PL020 4
Berdasarkan hasil Iterasi ke-5, diketahui bahwa tidak terdapat perpindahan anggota pada seluruh cluster
dibandingkan dengan Iterasi ke -4. Kondisi ini mengindikasikan bahwa algoritma K -Means telah mencapai
keadaan konvergen ( convergence), yaitu kondisi ketika proses pembaruan centroid tidak lagi menghasilkan
perubahan terhadap keanggotaan data. Dengan demikian, hasil pengelompokan pada Iterasi  ke-5 ditetapkan
sebagai hasil akhir penelitian.
Hasil akhir pengelompokan ini selanjutnya digunakan sebagai dasar dalam melakukan analisis
karakteristik masing -masing cluster serta penyusunan strategi digital marketing yang sesuai dengan profil
pelanggan pada setiap kelompok.
Tabel 12 Hasil Akhir Segmentasi Pelanggan RM Serdang
Cluster Nama Cluster Anggota Jumlah
C1 Pelanggan Aktif PL003, PL008, PL009, PL010, PL011, PL014, PL018 7
C2 Pelanggan Bernilai Tinggi PL002, PL005, PL017, PL019 4
C3 Pelanggan Potensial PL001, PL006, PL007, PL012, PL013 5
C4 Pelanggan Kurang Aktif PL004, PL015, PL016, PL020 4

Tabel 13 Visualisasi Hasil Segmentasi Pelanggan RM Serdang
Cluster Nama Cluster Representasi
C1 Pelanggan Aktif ███████
C2 Pelanggan Bernilai Tinggi ████
C3 Pelanggan Potensial █████

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 261
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
C4 Pelanggan Kurang Aktif ████

Berdasarkan hasil implementasi algoritma K -Means, diperoleh empat kelompok pelanggan yang
memiliki karakteristik berbeda. Cluster yang terbentuk merupakan hasil akhir dari proses iterasi yang mencapai
kondisi konvergen pada Iterasi ke-5. Cluster 1 yang diberi nama Pelanggan Aktif merupakan cluster dengan jumlah
anggota terbanyak, yaitu sebanyak tujuh pelanggan atau  35% dari total sampel. Pelanggan pada cluster ini
menunjukkan tingkat aktivitas transaksi yang relatif baik dan memiliki potensi untuk dipertahankan melalui
program loyalitas. Cluster 2, yang diberi nama Pelanggan Bernilai Tinggi, terdiri atas empat pelan ggan dengan
kontribusi nilai transaksi yang paling besar. Kelompok ini menjadi segmen yang paling penting bagi perusahaan
karena berkontribusi langsung terhadap pendapatan. Sementara itu, Cluster 3 (Pelanggan Potensial) beranggotakan
lima pelanggan yang me miliki peluang untuk dikembangkan melalui strategi pemasaran yang lebih terarah.
Adapun Cluster 4 (Pelanggan Kurang Aktif) terdiri atas empat pelanggan yang menunjukkan tingkat aktivitas
transaksi yang relatif rendah. Kelompok ini memerlukan perhatian khusus melalui program retensi, promosi, dan
reaktivasi pelanggan. Dengan demikian, h asil segmentasi yang diperoleh mampu memberikan informasi yang
lebih spesifik mengenai perilaku pelanggan dan dapat dijadikan sebagai dasar dalam penyusunan strategi digital
marketing yang lebih efektif
4. KESIMPULAN
Berdasarkan hasil penelitian yang telah dilakukan mengenai penerapan algoritma K-Means Clustering
untuk segmentasi pelanggan pada RM Serdang menggunakan pendekatan Recency, Frequency, dan Monetary
(RFM), dapat disimpulkan bahwa: Penelitian ini berhasil mengimplementasikan pendekatan RFM untuk
merepresentasikan perilaku pelanggan berdasarkan tiga dimensi utama, yaitu waktu terakhir pelanggan melakukan
transaksi (Recency), frekuensi transaksi ( Frequency), dan nilai total transaksi ( Monetary).  Penerapan algoritma
K-Means Clustering  dilakukan secara bertahap melalui proses perhitungan Euclidean Distance , pembaruan
centroid, dan iterasi berulang hingga mencapai kondisi konvergen. Berdasarkan hasil perhitungan manual terhadap
20 data pelanggan, algoritma mencapai kondisi stabil pada Iterasi ke -5 yang ditandai dengan tidak adanya
perubahan anggota cluster pada dua iterasi terakhir. Kondisi ini menunjukkan bahwa algoritma K-Means mampu
mengelompokkan pelanggan secara konsisten berdasarkan tingkat kemiripan atribut RFM yang dimiliki.
Penerapan algoritma K-Means Clustering  mengelompokkan data menjadi empat kelompok utama dengan
karakteristik yang berbeda. Cluster 1 (Pelanggan Aktif) terdiri atas tu juh pelanggan yang menunjukkan tingkat
aktivitas transaksi yang relatif baik dan memiliki potensi untuk dipertahankan melalui program loyalitas. Cluster
2 (Pelanggan Bernilai Tinggi) terdiri atas empat pelanggan yang memiliki kontribusi terbesar terhadap pendapatan
perusahaan karena didominasi oleh nilai Frequency dan Monetary yang tinggi. Cluster 3 (Pelanggan Potensial)
terdiri atas lima pelanggan yang memiliki peluang untuk dikembangkan menjadi pelanggan bernilai tinggi melalui
strategi pemasaran yang leb ih terarah. Sementara itu, Cluster 4 (Pelanggan Kurang Aktif) terdiri atas empat
pelanggan yang menunjukkan tingkat aktivitas transaksi yang relatif rendah dan memerlukan pendekatan
reaktivasi pelanggan. Setiap kelompok (cluster) pelanggan memiliki karakteristik perilaku yang berbeda sehingga
tidak dapat diperlakukan dengan strategi pemasaran yang sama. Oleh karena itu, hasil segmentasi yang dihasilkan
melalui algoritma K-Means dapat menjadi dasar dalam penerapan strategi digital marketing yang lebih tepat
sasaran, seperti program loyalitas, promosi yang dipersonalisasi, pemberian penghargaan kepada pelanggan
prioritas, serta program retensi pelanggan.
REFERENCES
[1] E. Manurung and P. S. Hasugian, “Data Mining Tingkat Pesanan Inventaris Kantor Menggunakan Algoritma Apriori pada Kepolisian
Daerah Sumatera Utara,” Journal Of Informatic Pelita Nusantara, vol. 4, no. 2, 2019.
[2] T. S. Alasi, “Ilmu komputer,” 2024, Media Publikasi Idpress .
[3] N. Kadek, A. Nirwana, N. Putu, W. Dewi, I. M. Dwi, and P. Asana, “Master Stockist Customer Segmentation Using RFM Model and
Self-Organizing Maps Algorithm,” vol. 8, no. October, pp. 2447 –2457, 2024.
[4] A. Sciences, “CUSTOMER SEGMENTATION BY USING RFM MODEL AND CLUSTERING METHODS : A CASE,” pp. 1 –19, 2018.
[5] A. S. Sembiring, T. S. Alasi, and others, “Penerapan Data Mining Menggunakan Algoritma Apriori Pada Peminjaman Buku di
Perpustakaan Pada Pesantren Babul Ulum,” Jurnal Armada Informatika, vol. 7, no. 2, pp. 323–327, 2023.

Jurnal Armada Informatika
Volume 10, Nomor 1, Juni 2026, Page 251-262
ISSN  2615-689X (Online), 2598-0416 (Print)
Available Online at https://jurnal.stmikmethodistbinjai.ac.id/jai
Doi https://doi.org/10.36520/jai.v10i1.320
Penda Sudarto Hasugian, Copyright © 2026, JAI, Page 262
Submitted: 04/04/2026; Accepted: 11/05/2026; Published: 27/06/2026
[6] C. Series, “A review of data mining methods in RFM -based customer segmentation,” 2021, doi: 10.1088/1742 -
6596/1869/1/012085.
[7] D. Methods, R. Wati, B. Sembiring, F. A. Mohammed, and K. Chairuang, “Customer Segmentation Based on RFM Model Using,”
vol. 11, no. 1, pp. 32–43, 2020.
[8] A. T. Al Afkari, T. S. Alasi, and Y. Darmayunata, “Clustering of Stunting, Wasting, and Underweight Case Volumes Using K -Means:
An Exploratory Study of Monthly Data in Southeast Aceh Regency,” Jurnal Armada Informatika, vol. 10, no. 1, pp. 262–269, 2026.
[9] G. B. Sulistyo, N. Hasan, S. Kiswati, F. Natalia, and E. Muningsih, “Segmentasi Pelanggan dan Optimalisasi Penjualan pada Dat a
Retail Online Berbasis Model RFM,” vol. 5, no. 1, 2025.
[10] R. Martiansah, S. Monalisa, M. Fronita, and F. Muttakin, “Customer Segmentation Analysis Through RFM - D Model and K-Means
Algorithm,” vol. 08, no. 01, pp. 1 –11, 2025.
[11] S. Y. Prayogi, T. S. Alasi, and R. F. Rahmat, “Pengantar Machine Learning,” 2025, Media Publikasi Idpress.
[12] M. Iqbal, T. S. Alasi, and E. M. Padilla, Pemograman untuk data analitik: dari data berantakan menjadi cerita yang mudah
dipahami. IdPress, 2026.
[13] A. Y. Nasution, T. S. Alasi, P. D. Manalu, D. Irawan, and R. Rosnelly, “Keamanan Data Dengan Analisis Log Berbasis Kecerdasan
Buatan,” 2026, Media Publikasi Idpress.
[14] F. A. Sianturi, A. Simangunsong, R. M. Simanjorang, and P. I. Sijabat, “Implementasi Algoritma Modified Nearest Neighbourt (M -
KNN) Untuk Klasifikasi Buku,” Jurnal Media Informatika [Jumin], vol. 1, no. 2, 2020.
[15] A. Simangunsong and M. Informatika, “Sistem Informasi Pengarsipan Dokumen Berbasis Web,” Jurnal Mantik Penusa, vol. 2, no.
1, 2018.
