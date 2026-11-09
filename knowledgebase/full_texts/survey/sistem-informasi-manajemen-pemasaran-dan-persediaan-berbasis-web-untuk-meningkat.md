---
title: Sistem Informasi Manajemen Pemasaran dan Persediaan Berbasis Web untuk Meningkatkan Efisiensi Operasional
  CV. Sarepah Meutuah
url: https://doi.org/10.61306/jnastek.v6i4.571
category: survey
subcategory: case-study
date: 2026-10
venue: Jurnal Nasional Teknologi Komputer
authors:
- Aryudha Julian Efendi
- Abdul Khaliq
- Hanna Willa Dhany
source: openalex-oa
pdf_url: https://publikasi.hawari.id/index.php/jnastek/article/download/571/503
pages: 9
chars: 23192
fetched_at: '2026-11-08T19:55:55+00:00'
kb_version: 1
---

# Sistem Informasi Manajemen Pemasaran dan Persediaan Berbasis Web untuk Meningkatkan Efisiensi Operasional CV. Sarepah Meutuah

Jurnal Nasional Teknologi Komputer
Vol.6; No: 4; Oktober 2026
                                                                                                       Website: publikasi.hawari.id/index.php/jnastek
                                                                                             E-ISSN: 2808-4845; P-ISSN: 2808-7801

 Lisensi
 Lisensi Internasional Creative Commons Attribution-ShareAlike 4.0.

2205
Makalah Penelitian

Sistem Informasi Manajemen Pemasaran dan Persediaan Berbasis Web
untuk Meningkatkan Efisiensi Operasional CV. Sarepah Meutuah

Aryudha Julian Efendi1, Abdul Khaliq2, Hanna Willa Dhany3

1,2,3Universitas Pembangunan Panca Budi Medan
1aryudajulianefendi@gmail.com

Corresponding Author: Abdul Khaliq

ABSTRACT

Advancements in information technology encourage companies to utilize information systems to support the management of
marketing, sales, and inventory activities in a more structured manner. CV. Sarepah Meutuah requires an integrated system
for managing da ta on products, categories, customers, orders, and inventory, as well as sales reports, to enhance the
effectiveness of administrative and operational processes. This research aims to develop a web-based marketing and inventory
management information system to support data and transaction management at CV. Sarepah Meutuah. The study employs a
case study approach comprising requirements analysis, design, implementation, and functional testing phases. The system
features administrator authentication, a dashbo ard, and management capabilities for products, product categories, customer
data, orders, order reports, and users. Implementation results demonstrate that key data management functions have been
consolidated into a single administrative interface. The product module enables administrators to manage categories, ports of
origin, product names, prices, stock levels, images, and management actions. The customer and order modules facilitate the
management of customer information and order statuses, while the re porting module presents transaction data in a structured
format. The resulting system establishes a foundation for digitizing marketing and inventory administration processes at CV.
Sarepah Meutuah. However, quantitative measurements regarding efficiency improvements—such as processing times before
and after implementation—were not available in the source documentation and should be addressed in future research.
Keywords: information system, marketing management, inventory, sales, web-based.

ABSTRAK

Perkembangan teknologi informasi mendorong perusahaan untuk memanfaatkan sistem informasi dalam mendukung
pengelolaan aktivitas pemasaran, penjualan, dan persediaan secara lebih terstruktur. CV. Sarepah Meutuah membutuhkan
pengelolaan data barang, kategori , pelanggan, pemesanan, persediaan, serta laporan penjualan yang terintegrasi agar proses
administrasi dan operasional dapat dilakukan secara lebih efektif. Penelitian ini bertujuan mengembangkan sistem informasi
manajemen pemasaran dan persediaan berbasis web yang dapat mendukung pengelolaan data dan transaksi pada CV. Sarepah
Meutuah. Metode penelitian menggunakan pendekatan studi kasus dengan tahapan analisis kebutuhan, perancangan,
implementasi, dan pengujian fungsional. Sistem menyediakan autentikasi a dministrator, dashboard, pengelolaan barang,
kategori barang, data pelanggan, pemesanan, laporan pemesanan barang, dan manajemen pengguna. Hasil implementasi
menunjukkan bahwa fungsi utama pengelolaan data telah diakomodasi dalam satu antarmuka administras i. Modul barang
memungkinkan administrator mengelola kategori, pelabuhan, nama barang, harga, stok, gambar, dan tindakan pengelolaan.
Modul pelanggan dan pemesanan mendukung pengelolaan informasi pelanggan serta status pesanan, sedangkan modul laporan
menyajikan transaksi dalam bentuk informasi yang lebih terstruktur. Sistem yang dihasilkan memberikan dasar digitalisasi
proses administrasi pemasaran dan persediaan pada CV. Sarepah Meutuah. Namun, pengukuran kuantitatif peningkatan
efisiensi seperti waktu proses sebelum dan sesudah implementasi belum tersedia dalam dokumen sumber dan perlu dilakukan
pada penelitian lanjutan..

Kata Kunci: sistem informasi, manajemen pemasaran, persediaan, penjualan, berbasis web.

1. Pendahuluan

Pemanfaatan sistem informasi berbasis web merupakan salah satu pendekatan yang banyak
digunakan untuk mendukung digitalisasi proses bisnis. Dalam kegiatan penjualan dan
persediaan, sistem informasi dapat membantu perusahaan memusatkan data produk,
pelanggan, transaksi, dan laporan sehingga informasi dapat diakses dan dikelola secara lebih

Aryudha Julian Efendi1, Abdul Khaliq2, Hanna Willa Dhany3
Jurnal Nasional Teknologi Komputer (JNASTEK) Vol. 6 No. 4 (2026)

 Lisensi
 Lisensi Internasional Creative Commons Attribution-ShareAlike 4.0.

2206
terstruktur. Penelitian mengenai sistem informasi penjualan berbasis web juga menunjukkan
bahwa digitalisasi dapat digunakan untuk mendukung pemantauan transaksi dan penyusunan
laporan penjualan secara lebih cepat dan terorganisasi.
Pada pengelolaan persediaan, keberadaan informasi barang dan stok merupakan bagian
penting karena data tersebut berkaitan langsung dengan proses penjualan dan ketersediaan
produk. Penelitian tentang sistem informasi persediaan berbasis web menempatkan
pengelolaan data barang, stok, transaksi, dan pelaporan sebagai fungsi utama sistem.
Penggunaan model Waterfall juga banyak diterapkan dalam pengembangan sistem persediaan
dan penjualan karena menyediakan tahapan pengembangan yang terstruktur, mulai dari analisis
kebutuhan sampai pengujian.
CV. Sarepah Meutuah memiliki sistem administrasi yang mendukung pengelolaan
aktivitas penjualan barang. Berdasarkan dokumentasi sistem yang menjadi sumber penelitian,
administrator melakukan autentikasi melalui halaman login sebelum mengakses sistem.
Setelah berhasil login, administrator diarahkan ke dashboard yang menyediakan menu Barang,
Cabang, Kategori Barang, Data Pelanggan, Pemesanan, Laporan Pemesanan Barang, dan
Manajemen User. Struktur tersebut menunjukkan bahwa sistem telah mengintegrasikan
beberapa fungsi administrasi dalam satu lingkungan aplikasi.
Pada sisi pengelolaan produk, sistem menyediakan menu Barang yang digunakan untuk
menambahkan, melihat, mengubah, dan menghapus data barang. Data yang ditampilkan
meliputi kategori, pelabuhan, nama barang, harga, stok, gambar, dan tindakan pengelolaan.
Selain itu, tersedia menu Kategori Barang untuk mengelompokkan produk, menu Data
Pelanggan untuk mengelola informasi pelanggan, serta menu Pemesanan untuk mengelola
transaksi pemesanan dan statusnya.
Permasalahan penelitian ini difokuskan pada bagaimana mengembangkan sistem
informasi berbasis web yang mampu mengintegrasikan fungsi manajemen pemasaran dan
persediaan pada CV. Sarepah Meutuah. Tujuan penelitian adalah menghasilkan sistem yang
mendukung pe ngelolaan data produk, pelanggan, pemesanan, persediaan, laporan, dan
pengguna secara terpusat. Kontribusi penelitian terletak pada dokumentasi dan pengembangan
sistem administrasi berbasis web yang menggabungkan fungsi pemasaran dan persediaan
dalam satu aplikasi.
Penelitian sejenis menunjukkan relevansi pendekatan tersebut. Sistem informasi
manajemen penjualan berbasis website telah digunakan untuk mendukung pencatatan
transaksi, pengelolaan stok, dan pembuatan laporan. Studi lain mengenai sistem persediaan
berbasis web juga menunjukkan bahwa sistem terkomputerisasi dapat membantu pengelolaan
data barang dan penyajian laporan secara lebih cepat. Oleh karena itu, pengembangan sistem
pada CV. Sarepah Meutuah ditempatkan pada konteks digitalisasi administrasi penjualan  dan
persediaan.

2. Metode Penelitian
2.1 Jenis dan Pendekatan Penelitian
Penelitian menggunakan pendekatan studi kasus pada CV. Sarepah Meutuah. Fokus penelitian
adalah proses administrasi yang berkaitan dengan pengelolaan barang, kategori, pelanggan,
pemesanan, laporan penjualan, dan pengguna. Pendekatan studi kasus dipilih ag ar analisis
sistem dapat diarahkan pada kebutuhan operasional objek penelitian secara spesifik.
2.2 Teknik Pengumpulan Data
Pengumpulan data dilakukan melalui observasi terhadap proses dan antarmuka sistem,
dokumentasi, serta studi pustaka. Dokumentasi sistem menjadi sumber utama untuk
mengidentifikasi fungsi yang telah tersedia. Studi pustaka digunakan untuk membandingkan
konsep dan pendekatan pengembangan dengan penelitian terdahulu mengenai sistem informasi
penjualan dan persediaan berbasis web.

Aryudha Julian Efendi1, Abdul Khaliq2, Hanna Willa Dhany3
Jurnal Nasional Teknologi Komputer (JNASTEK) Vol. 6 No. 4 (2026)

 Lisensi
 Lisensi Internasional Creative Commons Attribution-ShareAlike 4.0.

2207
2.3 Tahapan Pengembangan Sistem
Pengembangan sistem disusun secara bertahap yang meliputi analisis kebutuhan, perancangan,
implementasi, dan pengujian. Model pengembangan Waterfall digunakan sebagai kerangka
konseptual karena tahapannya sistematis dan banyak digunakan pada pengembangan s istem
informasi penjualan serta persediaan.
Tahap Aktivitas Output Keterangan
Analisis Identifikasi
kebutuhan
pengguna dan
fungsi sistem
Spesifikasi
kebutuhan
Menentukan fungsi
administrasi yang
diperlukan
Perancangan Perancangan
struktur menu dan
alur data
Rancangan sistem Menentukan hubungan
antarfitur
Implementasi Pembangunan
antarmuka dan
fungsi sistem
Aplikasi web Mengimplementasikan
modul administrasi
Pengujian Pengujian
fungsional
berdasarkan input
dan output
Hasil pengujian Memastikan fungsi
berjalan sesuai
kebutuhan

2.4 Analisis Kebutuhan Sistem
Kebutuhan fungsional sistem diidentifikasi berdasarkan menu yang tersedia pada dokumentasi
aplikasi. Administrator memerlukan fungsi autentikasi, pengelolaan barang, pengelolaan
cabang, pengelolaan kategori, pengelolaan pelanggan, pengelolaan pemesanan, pe nyajian
laporan, dan manajemen pengguna. Kebutuhan tersebut kemudian diterjemahkan ke dalam
struktur dashboard dan menu administrasi.
No. Kebutuhan Fungsi
1 Autentikasi Login dan pembatasan akses
administrator
2 Barang Tambah, lihat, ubah, dan
hapus data barang
3 Kategori Mengelola pengelompokan
barang
4 Pelanggan Melihat dan mengelola data
pelanggan
5 Pemesanan Melihat pesanan dan
mengelola status pemesanan
6 Laporan Menyajikan informasi
transaksi pemesanan
7 Manajemen User Mengelola akun dan akses
pengguna

3. Hasil Dan Pembahasan
3.1 Halaman Login Administrator
Halaman login merupakan pintu masuk administrator ke dalam sistem. Administrator harus
memasukkan username dan password yang telah terdaftar. Tombol Login digunakan untuk

Aryudha Julian Efendi1, Abdul Khaliq2, Hanna Willa Dhany3
Jurnal Nasional Teknologi Komputer (JNASTEK) Vol. 6 No. 4 (2026)

 Lisensi
 Lisensi Internasional Creative Commons Attribution-ShareAlike 4.0.

2208
memproses autentikasi, sedangkan tombol Reset digunakan untuk mengosongkan kembali
isian. Mekanisme ini membatasi akses ke halaman administrator sehingga pengelolaan data
dapat dilakukan oleh pengguna yang memiliki hak akses.

Gambar 1. Halaman Login Administrator
3.2 Dashboard Administrator
Setelah proses login berhasil, administrator diarahkan ke dashboard. Dashboard berfungsi
sebagai pusat navigasi menuju fitur pengelolaan sistem. Menu yang terlihat meliputi Barang,
Cabang, Kategori Barang, Data Pelanggan, Pemesanan Pemesanan, Laporan Pemes anan
Barang, dan Manajemen User. Dashboard menjadi titik penghubung antara fungsi pengelolaan
produk, pelanggan, transaksi, laporan, dan pengguna.

Gambar 2. Dashboard Administrator
3.3 Pengelolaan Data Barang
Menu Barang digunakan sebagai pusat pengelolaan produk. Administrator dapat
menambahkan data baru, melihat daftar barang, mengubah informasi, dan menghapus data
yang tidak diperlukan. Informasi yang tersedia meliputi kategori, pelabuhan, nomor/nama
barang, harga, stok, gambar, dan tindakan pengelolaan. Struktur ini mendukung kebutuhan
dasar manajemen persediaan karena informasi stok berada pada satu modul dengan informasi
produk.

Aryudha Julian Efendi1, Abdul Khaliq2, Hanna Willa Dhany3
Jurnal Nasional Teknologi Komputer (JNASTEK) Vol. 6 No. 4 (2026)

 Lisensi
 Lisensi Internasional Creative Commons Attribution-ShareAlike 4.0.

2209

Gambar 3. Menu Data Barang
3.4 Pengelolaan Kategori Barang
Menu Kategori Barang digunakan untuk mengelompokkan produk berdasarkan jenis tertentu.
Administrator dapat menambahkan, melihat, mengubah, dan menghapus kategori.
Pengelompokan ini membantu menjaga struktur data produk sehingga pencarian dan
pengelolaan barang dapat dilakukan berdasarkan kelompok yang sesuai.

Gambar 4. Menu Kategori Barang dan Data Pelanggan

3.5 Pengelolaan Data Pelanggan
Data pelanggan digunakan untuk menyimpan informasi pelanggan yang melakukan transaksi.
Data ini mendukung proses pencatatan dan pengelolaan transaksi penjualan. Administrator
dapat melihat data pelanggan yang telah terdaftar, sehingga hubungan antara pelan ggan dan
transaksi dapat dikelola secara lebih terstruktur.

3.6 Pengelolaan Pemesanan
Menu Pemesanan digunakan untuk mengelola data pemesanan barang yang dilakukan
pelanggan. Administrator dapat melihat informasi pesanan dan mengelola status pemesanan.
Pada tampilan sistem, data pemesanan memperlihatkan informasi pelanggan, nomor telepon,
tanggal pesanan, detail pesanan, status delivery, dan status transaksi. Fungsi ini

Aryudha Julian Efendi1, Abdul Khaliq2, Hanna Willa Dhany3
Jurnal Nasional Teknologi Komputer (JNASTEK) Vol. 6 No. 4 (2026)

 Lisensi
 Lisensi Internasional Creative Commons Attribution-ShareAlike 4.0.

2210
menghubungkan data pelanggan dengan produk yang dipesan dan menjadi bagian penting
dalam administrasi penjualan.

Gambar 5. Menu Pemesanan Barang
3.7 Laporan Pemesanan Barang
Menu Laporan Pemesanan Barang digunakan untuk menampilkan informasi transaksi
pemesanan. Laporan menyajikan data transaksi secara lebih terstruktur dan dapat digunakan
sebagai bahan monitoring serta evaluasi aktivitas penjualan. Keberadaan laporan terinteg rasi
mengurangi kebutuhan untuk menyusun ulang informasi transaksi dari sumber data yang
berbeda.

Gambar 6. Laporan Penjualan Barang
3.8 Manajemen User
Menu Manajemen User digunakan untuk mengelola akun yang memiliki akses terhadap sistem
administrator. Fungsi yang tersedia meliputi penambahan akun, perubahan informasi
pengguna, dan penghapusan akun yang tidak diperlukan. Pengelolaan akun mendukung
pembatasan akses sehingga penggunaan sistem dapat dilakukan oleh pihak yang memiliki
kewenangan.

Aryudha Julian Efendi1, Abdul Khaliq2, Hanna Willa Dhany3
Jurnal Nasional Teknologi Komputer (JNASTEK) Vol. 6 No. 4 (2026)

 Lisensi
 Lisensi Internasional Creative Commons Attribution-ShareAlike 4.0.

2211

Gambar 7. Manajemen User
3.9 Pengujian Fungsional
Pengujian fungsional dirancang menggunakan pendekatan black -box, yaitu memeriksa
hubungan antara masukan dan keluaran fungsi tanpa menilai struktur kode internal. Pendekatan
ini umum digunakan pada penelitian sistem informasi penjualan dan persediaan untuk
memastikan fungsi sesuai dengan kebutuhan pengguna.
No. Fungsi Skenario Kriteria Keberhasilan
1 Login Username dan
password valid
dimasukkan
Administrator diarahkan ke
dashboard
2 Barang Tambah/ubah/hapus
data barang
Data
tersimpan/berubah/terhapus
sesuai aksi
3 Kategori Tambah/ubah/hapus
kategori
Data kategori berubah
sesuai aksi
4 Pelanggan Membuka daftar
pelanggan
Data pelanggan tampil
5 Pemesanan Membuka data
pesanan dan status
Informasi pesanan dan
status tampil
6 Laporan Membuka laporan
pemesanan
Laporan transaksi tampil
terstruktur
7 Manajemen User Tambah/ubah/hapus
pengguna
Data pengguna dapat
dikelola
Tabel pengujian di atas merupakan rancangan skenario pengujian yang perlu dijalankan pada
instalasi sistem dan dicatat hasil aktualnya sebelum naskah dikirim ke jurnal. Dokumen sumber
yang dianalisis menyediakan bukti visual keberadaan dan struktur setiap modul, tetapi tidak
memuat log pengujian, jumlah skenario yang benar -benar dieksekusi, waktu respons, atau
persentase keberhasilan. Oleh karena itu, penelitian ini tidak menetapkan angka keberhasilan
pengujian yang tidak didukung oleh data sumber.

3.10 Pembahasan
Hasil implementasi menunjukkan bahwa sistem telah menggabungkan beberapa fungsi yang
saling berkaitan dalam proses operasional penjualan. Modul Barang berperan sebagai pusat
informasi produk dan stok, sedangkan Kategori Barang membantu pengelompokan produk .

Aryudha Julian Efendi1, Abdul Khaliq2, Hanna Willa Dhany3
Jurnal Nasional Teknologi Komputer (JNASTEK) Vol. 6 No. 4 (2026)

 Lisensi
 Lisensi Internasional Creative Commons Attribution-ShareAlike 4.0.

2212
Data Pelanggan dan Pemesanan menghubungkan informasi konsumen dengan transaksi,
sementara Laporan menyediakan bentuk informasi yang dapat digunakan untuk monitoring.
Manajemen User menambahkan fungsi pengendalian akses.
Dari perspektif operasional, integrasi tersebut berpotensi mengurangi fragmentasi data karena
informasi administrasi dikelola melalui satu lingkungan sistem. Temuan ini sejalan dengan
penelitian terdahulu yang mengembangkan sistem penjualan dan persediaan berbasis web
untuk memusatkan data transaksi, stok, dan laporan. Namun, istilah 'meningkatkan efisiensi'
dalam penelitian ini dipahami sebagai manfaat fungsional dari digitalisasi dan integrasi proses,
bukan sebagai peningkatan yang telah dibuktikan melalui pengukuran waktu atau biaya.
Dibandingkan dengan penelitian yang secara eksplisit melaporkan hasil black -box dan
usability testing, penelitian pada CV. Sarepah Meutuah masih memerlukan data pengujian
aktual agar klaim kinerja dapat dikuantifikasi. Penelitian lanjutan dapat menambahkan
pengukuran waktu pencatatan transaksi, waktu penyusunan laporan, tingkat kesalahan input,
dan penilaian usability pengguna. Penambahan metrik tersebut akan memperkuat bukti empiris
mengenai dampak sistem terhadap efisiensi operasional.

4. Kesimpulan
Penelitian ini menghasilkan rancangan dan implementasi Sistem Informasi Manajemen
Pemasaran dan Persediaan Berbasis Web untuk CV. Sarepah Meutuah. Sistem menyediakan
fungsi autentikasi administrator, dashboard, pengelolaan barang, kategori barang, data
pelanggan, pemesanan, laporan pemesanan barang, dan manajemen user. Integrasi fungsi
tersebut menyediakan sarana pengelolaan data pemasaran dan persediaan secara terpusat serta
mendukung proses administrasi penjualan yang lebih terstruktur.
Berdasarkan dokumentasi sistem, modul -modul utama telah direpresentasikan dalam
antarmuka aplikasi dan mendukung kebutuhan pengelolaan data. Meskipun demikian,
dokumen sumber belum menyediakan hasil pengujian kuantitatif sehingga peningkatan
efisiensi belum dapat dinyatakan dalam bentuk persentase atau nilai waktu tertentu. Untuk
pengembangan penelitian selanjutnya, disarankan dilakukan black -box testing secara
terdokumentasi, usability testing, serta pengukuran sebelum dan sesudah implementasi
terhadap waktu proses, kesalahan pencatatan, dan penyusunan laporan.

DAFTAR PUSTAKA
Alamna Digitech University, A. R., Abdullah, F., & Anggraini, N. (2025). Sistem Informasi
Persediaan dan Mutasi Barang Berbasis Web (Studi Kasus: PT Chitose Cengineering
Indonesia). OKTAL: Jurnal Ilmu Komputer dan Sains.
Arvanullah, & Kurniawati, R. (2024). Perancangan Sistem Informasi Persediaan Barang
Berbasis Web dengan Framework Laravel (Studi Kasus pada Direktorat Sarana Prasarana
Universitas Kristen Maranatha). INFOKOM (Informatika & Komputer), 12(1), 17 –27.
https://doi.org/10.56689/infokom.v12i1.1141
Cakrawati, C., Rochim, A. F., & Windasari, I. P. (2023). Rancang Bangun dan Implementasi
Sistem Informasi Manajemen Penjualan Berbasis Website Menggunakan Kerangka Kerja
CodeIgniter pada Kafe Dangau Kopi. Jurnal Teknik Komputer, 2(1), 31 –38.
https://doi.org/10.14710/jtk.v2i1.38083
Fatmawati, F., & Munajat, J. (2018). Implementasi Model Waterfall pada Sistem Informasi
Persediaan Barang Berbasis Web (Studi Kasus: PT. Pamindo Tiga T). JURNAL MEDIA
INFORMATIKA BUDIDARMA, 2(2). https://doi.org/10.30865/mib.v2i2.559
Fathoni, M. N. K., & Kustiyono. (2025). Pengembangan Sistem Informasi Persediaan Barang
Menggunakan Model Waterfall untuk Meningkatkan Efisiensi Pengelolaan Stok. Jurnal
Algoritma, 22(2). https://doi.org/10.33364/algoritma/v.22-2.2533

Aryudha Julian Efendi1, Abdul Khaliq2, Hanna Willa Dhany3
Jurnal Nasional Teknologi Komputer (JNASTEK) Vol. 6 No. 4 (2026)

 Lisensi
 Lisensi Internasional Creative Commons Attribution-ShareAlike 4.0.

2213
Hasanudin, H., & Wati, R. (2024). Implementasi Sistem Informasi Persediaan Barang Berbasis
Web Menggunakan Metode Waterfall pada PT ABCDE Indonesia. JATI (Jurnal
Mahasiswa Teknik Informatika), 8(6). https://doi.org/10.36040/jati.v8i6.11980
Jibran, S. M., Jannah, N., & Rahmani, D. I. P. (2025). Pengembangan Sistem Informasi
Manajemen Penjualan Berbasis Website untuk Meningkatkan Efisiensi Operasional pada
Toko Win Glowing dengan Metode Waterfall. Journal of Human and Education, 5(1), 576–
588. https://doi.org/10.31004/jh.v5i1.2225
Meilano, R., Damanik, F., & Tanto. (2020). Pengembangan Sistem Informasi Persediaan
Barang dengan Metode Waterfall. Jurnal Elektronika Listrik dan Teknologi Informasi
Terapan, 2(2). https://doi.org/10.37338/elti.v2i2.188
Nawangnugraeni, D. A. (2023). Pengembangan Sistem Informasi Manajemen Penjualan untuk
Meningkatkan Pelayanan Pelanggan Berbasis Web. JTIK (Jurnal Teknik Informatika
Kaputama), 7(2), 249–259. https://doi.org/10.59697/jtik.v7i2.18
Raharjo, B. P., Muslim, M. A., & Arini, F. Y. (2014). Sistem Informasi Penjualan Berbasis
Web pada Stockist Centre PT K -Link Indonesia Cabang Pekalongan. Unnes Journal of
Mathematics, 3(2). https://doi.org/10.15294/ujm.v3i2.4300
Rahmah, M., & Prima, W. (2019). Sistem Informasi Persediaan Barang Berbasis Web pada PT
BPR Sungai Rumbai. Simtika, 2(3), 10–20.
Rosalina, A., Rassi, A. A. G. R., Hadi, G. Y., Ubaidillah, R., & Desyani, T. (2020). Pengujian
Black Box pada Sistem Informasi Penjualan HI Shoe Store Menggunakan Teknik
Equivalence Partitions. Jurnal Informatika Universitas Pamulang, 5(1).
https://doi.org/10.32493/informatika.v5i1.3964
Sari, J., Nurhidayati, Saputri Nasution, I. W., & Furqan, M. (2025). Sistem Pengelolaan
Pencatatan Barang di Gudang Bapendasu Berbasis Web dengan Metode Waterfall. Syntax:
Journal of Software Engineering, Computer Science and Information Technology.
Solehudin, A. -A., Fariz, N., Wahyu, N., Permana, R. F., & Saifudin, A. (2023). Rancang
Bangun Digitalisasi Persediaan Barang Berbasis Web Menggunakan Metode Waterfall.
LOGIC: Jurnal Ilmu Komputer dan Pendidikan, 1(4), 1000–1005.
Tarmino, R. N., Hasan, N. F., & Musfiroh. (2026). Sistem Informasi Manajemen Penjualan
pada Toko Rizky Berbasis Website. Journal of Informatics, Intelligent Technology,
Cybersecurity, and Software, 1(1). https://doi.org/10.67618/pw57cb05
Wau, K. (2022). Pengembangan Sistem Informasi Persediaan Gudang Berbasis Website
dengan Metode Waterfall. Jurnal Teknik, Komputer, Agroteknologi dan Sains, 1(1).
https://doi.org/10.56248/marostek.v1i1.8
Wijaya, I. G. K. (2026). Implementasi Sistem Informasi Penjualan Berbasis Web
Menggunakan Arsitektur MVC dan Metode Waterfall. Jurnal Minfo Polgan, 15(2), 942 –
947. https://doi.org/10.33395/jmp.v15i2.16206

******
