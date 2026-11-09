---
title: Pengembangan Sistem Informasi E-Ticketing pada Armada Bus PO Harapan Kasih
url: https://doi.org/10.67142/digita.v2i1.508
category: ai-marketing
subcategory: framework
date: 2026-08
venue: Digita Informatics Technology and Applications
authors:
- Emagusri Intan Arungbua
- Alfrina Mewengkang
- Arje Cerullo Djamen
source: openalex-oa
pdf_url: https://calamus.id/index.php/digita/article/download/508/464
pages: 13
chars: 26259
fetched_at: '2026-11-08T20:04:28+00:00'
kb_version: 1
---

# Pengembangan Sistem Informasi E-Ticketing pada Armada Bus PO Harapan Kasih

ISSN 3123-4224
Vol. 2 No. 1

81

Pengembangan Sistem Informasi E-Ticketing pada
Armada Bus PO Harapan Kasih

Emagusri Intan Arungbua1*, Alfrina Mewengkang2, Arje Cerullo Djamen3
1,2,3Jurusan Pendidikan Teknologi Informasi dan Komunikasi, Fakultas Teknik,
Universitas Negeri Manado
*Corresponding: emagusriintanarungbua@gmail.com

Abstrak

Proses pemesanan tiket yang masih dilakukan secara manual melalui agen,
telepon, maupun WhatsApp menimbulkan berbagai permasalahan pada PO. Harapan
Kasih, antara lain pemesanan ganda (3–5 kasus per minggu), keterlambatan respons
petugas, kesalahan pencatatan data penumpang, serta keterbatasan sopir dalam
mengakses manifest sebelum keberangka tan. Penelitian ini bertujuan
mengembangkan sistem informasi e -ticketing berbasis web guna meningkatkan
efisiensi operasional dan kemudahan akses layanan pemesanan tiket. Metode
pengembangan yang digunakan adalah Agile Scrum dengan tiga sprint iterasi. Sistem
dibangun menggunakan framework Laravel berbasis PHP dengan basis data MySQL,
serta dirancang untuk tiga peran pengguna: admin, penumpang, dan sopir. Fitur
utama meliputi pencarian jadwal, pemilihan kursi berbasis denah visual interaktif,
pembayaran digital (transfer bank dan QRIS), verifikasi pembayaran, unduhan e-tiket,
informasi kendala perjalanan real -time, serta laporan rekapitulasi penjualan.
Pengujian fungsional menggunakan Black Box Testing menunjukkan seluruh 24
skenario berjalan sesuai kebutuha n (100% Valid). Validasi ahli sistem menghasilkan
rata-rata 4,36 (Sangat Layak) dan ahli konten 4,1 (Sangat Layak). Uji usability
menggunakan USE Questionnaire terhadap 35 responden menghasilkan rata -rata
keseluruhan 4,39 (Sangat Baik) pada seluruh dimensi. Kontribusi utama penelitian ini
adalah integrasi fitur pembayaran digital dan informasi kendala perjalanan real-time
yang membedakan sistem ini dari sistem e -ticketing bus yang dikembangkan
sebelumnya.
Kata kunci: Agile Scrum, Bus, E-Ticketing, Laravel, Sistem Informasi.

Abstract

The ticket booking process, still carried out manually through agents,
telephone, or WhatsApp, has given rise to various problems at PO. Harapan Kasih,
including double bookings (3 –5 cases per week), slow staff response, errors in
passenger data recording, and limited driver access to the passenger manifest prior to
departure. This study aims to develop a web -based e-ticketing information system to
improve operational efficiency and ease of access to bus ticket booking services. The
development method employed is Agile Scrum with three sprint iterations. The system

ISSN 3123-4224
Vol. 2 No. 1

82

was built using the Laravel framework based on PHP with a MySQL database, and was
designed for three user roles: admin, passenger, and driver. The main features include
schedule search, interactive visual seat map selection, digital payment (bank transfer
and QRIS), payment verification, e -ticket download, real -time travel disruption
information, and sales recapitulation reports. Black Box Testing across 24 scenarios
confirmed that all system functions operate as required (100% Valid). System expert
validation yielded an average score of 4.36 (Very Feasible) and content expert
validation 4.1 (Very Feasible). Usability testing using the USE Questionnaire involving
35 respondents produced an overall average of 4.39 (Very Good) across all dimensions.
The primary contribution of this study is the integration of digital payment features
and real -time travel disruption information, which differentiates this system from
previously developed bus e-ticketing systems.
Keywords: Agile Scrum, Bus, E-Ticketing, Information System, Laravel.

PENDAHULUAN

Perkembangan teknologi informasi dan komunikasi yang pesat telah
mendorong transformasi digital di berbagai sektor, termasuk industri transportasi
darat. Masyarakat saat ini semakin terbiasa dengan layanan yang praktis dan efisien,
sehingga mengharapkan pr oses pemesanan tiket yang cepat, mudah, dan dapat
diakses kapan saja serta di mana saja. Namun, realitas di lapangan menunjukkan
bahwa masih banyak perusahaan transportasi yang belum sepenuhnya mengadopsi
sistem digital dalam operasionalnya. Salah satu con tohnya adalah PO. Harapan
Kasih, sebuah perusahaan otobus yang melayani rute antar provinsi di Sulawesi.
Berdasarkan hasil wawancara dengan pihak agen dan sopir pada Agustus 2025,
proses pemesanan tiket di perusahaan ini masih dilakukan secara manual, di m ana
calon penumpang harus datang langsung ke agen atau menghubungi petugas
melalui telepon atau WhatsApp. Kondisi ini menimbulkan berbagai permasalahan,
seperti lamanya waktu pemesanan, kesulitan akses informasi jadwal dan
ketersediaan kursi bagi penumpang , serta tingginya potensi kesalahan pencatatan
dan pemesanan ganda yang dapat mencapai 3 -5 kasus setiap minggunya. Dari sisi
operasional, sopir juga tidak mendapatkan manifest penumpang yang akurat
sebelum keberangkatan, sehingga menyulitkan verifikasi jum lah penumpang dan
rawan terjadi kelebihan muatan. Permasalahan-permasalahan ini secara signifikan
mengurangi efisiensi, akurasi, dan kenyamanan layanan.
Penelitian ini bertujuan untuk mengembangkan sebuah sistem informasi E -
Ticketing berbasis web pada armada bus PO. Harapan Kasih yang dapat menjadi
solusi atas permasalahan yang ada. Sistem ini dirancang untuk mengakomodasi tiga
peran pengguna utama, yaitu penumpang, administrator (agen), dan sopir, dengan
fitur-fitur yang disesuaikan dengan kebutuhan masing-masing. Beberapa penelitian
sebelumnya, seperti yang dilakukan oleh Vita Ariska et al., (2023)  pada PO.
Haryanto, telah berhasil mengembangkan sistem pemesanan tiket bus berbasis
website yang meningkatkan efisiensi layanan. Demikian pula, penelitian oleh

ISSN 3123-4224
Vol. 2 No. 1

83

(Ramdhani et al., 2020)  serta Prasojo et al., (2023) menghasilkan sistem serupa
dengan fokus pada kemudahan akses dan pemesanan online. Namun, penelitian -
penelitian tersebut masih memiliki keterbatasan, terutama pada proses
pembayaran yang masih dilakukan secara manual dan belum terintegrasi dengan
sistem. Posisi penelitian ini berbeda dan menawarkan kebaruan dengan
mengimplementasikan metode pengembangan Agile yang adaptif terhadap
perubahan kebutuhan pengguna, serta menyediakan fitur pembayaran digital yang
lebih lengkap melalui transfer bank dan QRIS.
Selain itu, sebagai pembeda yang signifikan dari studi sebelumnya, sistem E-
Ticketing pada PO. Harapan Kasih ini dilengkapi dengan fitur informasi kendala
perjalanan secara real -time. Fitur ini memungkinkan penumpang untuk melihat
informasi secara langsung  apabila terjadi gangguan, keterlambatan, atau kondisi
darurat selama perjalanan berlangsung, sehingga meningkatkan transparansi
layanan. Untuk mendukung pengembangan sistem ini, digunakan framework
Laravel dengan basis data MySQL dan metodologi Scrum yang  membagi proses ke
dalam tiga sprint. Setiap sprint menghasilkan perangkat lunak yang fungsional dan
diuji secara bertahap, mulai dari fondasi sistem (autentikasi, manajemen data)
hingga fitur operasional (pembayaran, verifikasi, laporan). Dengan hadirnya sistem
ini, diharapkan proses pemesanan tiket bus PO. Harapan Kasih menjadi lebih
terstruktur, transparan, dan efisien, sekaligus mengurangi potensi kesalahan yang
kerap terjadi pada sistem manual, serta memberikan kontribusi nyata dalam
digitalisasi layanan transportasi darat di Indonesia.

KAJIAN TEORI

Sistem Informasi
Sistem informasi merupakan suatu perangkat yang berperan dalam
menyediakan informasi guna mendukung proses pengambilan keputusan maupun
penetapan kebijakan, sekaligus menjalankan aktivitas operasional melalui integrasi
antara sumber daya manusia, teknologi , dan prosedur yang terorganisasi secara
sistematis (Hidayanti et al., 2025). Lebih lanjut, sistem informasi merupakan sebuah
sistem yang berfungsi menyediakan informasi bagi manajemen dalam proses
pengambilan keputusan sekaligus mendukung kegiatan operasi onal perusahaan
(Sari et al., 2025).

E-Ticketing
E-Ticketing merupakan metode yang digunakan untuk mencatat dan
mendokumentasikan transaksi penjualan perjalanan pelanggan tanpa perlu
menerbitkan tiket fisik. Seluruh data tiket elektronik tersimpan secara digital di
dalam sistem komputer perusahaan (Wiharko et al., 2020).

ISSN 3123-4224
Vol. 2 No. 1

84

Web
Web atau World Wide Web merupakan suatu sistem jaringan komputer yang
terdiri dari kumpulan situs internet yang menyediakan berbagai konten berupa
teks, grafik, suara, dan animasi, dan dapat diakses oleh pengguna melalui protokol
transfer hypertext (HTTP) menggunakan peramban web. Web menjadi fondasi
utama pengembangan sistem informasi berbasis internet yang memungkinkan
akses lintas perangkat dan lokasi secara real-time (Lelet et al., 2023).

PHP
PHP merupakan bahasa pemrograman yang menjadi fondasi pengembangan
berbagai aplikasi web populer, di antaranya WordPress, Joomla, dan Drupal. PHP
juga menyediakan berbagai fitur perlindungan guna mengantisipasi potensi
serangan terhadap aplikasi web (Korompot et al., 2025).

Laravel
Laravel adalah framework PHP yang mengadopsi pola arsitektur Model -
View-Controller (MVC). Arsitektur MVC membagi aplikasi menjadi tiga komponen
inti: Model, View, dan Controller, yang masing -masing menangani aspek spesifik
dalam pengembangan perangkat lunak (Rachman et al., 2024).

MySQL
MySQL merupakan sistem manajemen basis data (RDBMS) yang paling
banyak digunakan dalam pengembangan aplikasi web dinamis. MySQL mengelola
dan menyimpan data secara terstruktur berdasarkan hubungan antar tabel dalam
basis data relasional (Djamen et al., 2023).

Agile Scrum
Agile merupakan pendekatan pengembangan perangkat lunak yang
mengutamakan pengiriman produk secara bertahap dan adaptif terhadap
perubahan (Trisnawati et al., 2022). Scrum adalah kerangka kerja dalam Agile yang
menghasilkan nilai melalui solusi adaptif dal am menangani masalah kompleks
(Hardiansyah et al., 2023). Elemen fundamental Scrum adalah Sprint — siklus kerja
maksimal 30 hari yang terdiri dari sprint planning, daily scrum, sprint review, dan
sprint retrospective (Amarta et al., 2021).

Black Box Testing
Black Box Testing merupakan metode pengujian perangkat lunak yang
berfokus pada verifikasi fungsi sistem berdasarkan masukan dan keluaran tanpa
memperhatikan struktur internal kode program (Latifah et al., 2026). Pengujian ini
bertujuan memastikan bahwa seluruh fungsi sistem berjalan sesuai spesifikasi yang
telah ditetapkan dari perspektif pengguna akhir. Dalam setiap skenario Black Box
Testing, didefinisikan kondisi uji, data masukan, dan keluaran yang diharapka n
(expected result) untuk kemudian dibandingkan dengan keluaran aktual sistem.

ISSN 3123-4224
Vol. 2 No. 1

85

USE Questionnaire
USE Questionnaire (Usefulness, Satisfaction, and Ease of Use) merupakan
instrumen terstandar yang dikembangkan oleh Lund (2001) untuk mengukur
usabilitas sistem perangkat lunak dari perspektif pengguna. Instrumen ini
mengukur empat dimensi: (1) Usefulness — sejauh mana sistem membantu
pengguna menyelesaikan tugas; (2) Ease of Use — kemudahan penggunaan sistem;
(3) Ease of Learning — kemudahan mempelajari sistem bagi pengguna baru; dan
(4) Satisfaction — kepuasan pengguna secara keseluruhan. USE Questionnair e
umum digunakan dalam penelitian pengembangan sistem informasi karena
mencakup dimensi usabilitas yang komprehensif (Anggono et al., 2026).

METODE PENELITIAN

Tempat dan Waktu Penelitian
Penelitian ini akan dilaksanakan di  PO. Harapan Kasih, pada bulan Maret
2026 hingga Mei 2026.

Alat dan Bahan
Perangkat keras yang digunakan adalah laptop asus dengan RAM 4GB, SSD
4GB. Perangkat lunak yang digunakan meliputi sistem opersai Windows 10, editor
teks Visual Studio Code, laragon, framework laravel, dan browser google crome.

Teknik Pengumpulan Data
Teknik pengumpulan data yang dilakukan dalam penelitian ini adalah
sebagai berikut:
1. Wawancara: Pada tahap ini pengumpulan data dilakukan melalui tanya
jawab langsung atau konsultasi kepada Pemilik PO. Harapan Kasih, petugas
agen dan calon penumpang untuk mendapatkan informasi mengenai hal -
hal yang berhubungan dengan penyelesaian masalah penelitian.
2. Observasi: Dilakukan dengan pengamatan secara langsung pada PO.
Harapan Kasih, untuk mengetahui bagaimana proses pembelian tiket bus
yang di lakukan oleh calon penumpang setiap harinya.
3. Studi Pustaka: Metode ini dilakukan dengan membaca referensi -referensi
atau literature ilmiah berupa buku, karya tulis, ataupun dari hasil pencarian
melalui internet.
4. Kuesioner: Pengumpulan data melalui kuesioner dengan skala Likert
diberikan kepada ahli sistem dan ahli konten  serta kepada calon
penumpang untuk menilai kelayakan sistem.

Jalannya Penelitian
Penelitian ini menggunakan metode  Research and Development (R&D)
dengan pendekatan Agile Scrum. Prosedur pengembangan meliputi beberapa
tahapan sebagai berikut. Pertama, penyusunan product backlog berdasarkan hasil

ISSN 3123-4224
Vol. 2 No. 1

86

wawancara dan observasi terhadap proses pemesanan tiket bus di PO.Harapan
Kasih, yang menghasilkan total 89 story points. Kedua, perencanaan sprint (sprint
planning) yang membagi proyek ke dalam 3 sprint dengan durasi masing -masing 2
minggu dan kapasitas t im ±28 story points per sprint. Ketiga, pelaksanaan sprint
(sprint execution) yang mencakup tahap perancangan menggunakan UML,
pengkodean menggunakan framework Laravel dengan arsitektur MVC, serta
pengujian fungsional menggunakan metode blackbox testing pa da 24 skenario uji
dan uji ahli sistem, uji ahli konten serta pengujian usability testing menggunakan
USE Questionnaire. Keempat, sprint review untuk mengevaluasi hasil
pengembangan bersama pemangku kepentingan. Kelima, tahap deployment
menggunakan alur ke rja berbasis Git dan GitHub Actions dengan protokol FTP ke
shared hosting.

HASIL DAN PEMBAHASAN

Hasil penelitian menggunakan metode scrum dengan 4 tahap utama: product
backlog, sprint planning, sprint execution, dan sprint review menunjukkan bahwa
sistem informasi E-Ticketing bus berbasis web yang dikembangkan telah berfungsi
sesuai dengan kebutuhan pengguna. Tahap perancangan sistem menggunakan
Unified Modeling Language (UML) seperti Use Case Diagram, Activity Diagram,
Sequence Diagram, dan Class Diagram.

Use Case Diagram
Use Case Diagram digunakan untuk menggambarkan interaksi antara aktor
pengguna dengan sistem serta fitur -fitur apa saja yang dapat diakses oleh masing
masing aktor yang dapat dilihat pada Gambar 1. Dalam sistem informasi E-Ticketing
bus ini, terdapat tiga aktor Tabel  1 yang berinteraksi dengan sistem, yaitu Admin,
penumpang dan sopir.

Tabel 1. Definisi Aktor
Aktor Deskripsi
Admin Pengguna dengan hak akses penuh untuk mengelola sistem. Admin bertugas
mengelola data bus, rute, jadwal keberangkatan, memverifikasi pembayaran,
serta melihat laporan pemesanan dan pembayaran tiket.
Penumpang Pengguna sistem yang melakukan pemesanan tiket bus. Penumpang dapat
melakukan registrasi dan login, melihat jadwal keberangkatan, melihat
ketersediaan kursi, memilih kursi, melakukan pemesanan tiket, melakukan
pembayaran, serta melihat riwayat pemesanan.
Sopir Pengguna sistem yang bertugas mengoperasikan bus. Sopir dapat login
menggunakan ID bus, melihat jadwal dan daftar penumpang (beserta nomor
kursi), konfirmasi keberangkatan.

ISSN 3123-4224
Vol. 2 No. 1

87

Gambar 1. Use Case Diagram

Tampilan Antarmuka Sistem
Berikut beberapa tampilan utama yang dihasilkan dalam pengembangan
sistem ini antara lain halaman login, halaman dashboard admin, halaman hasil
pencarian tiket, halaman input data penumpang, halaman pembayaran, e -ticket,
dashboard sopir yang dapat dilihat pada Gambar 2.

ISSN 3123-4224
Vol. 2 No. 1

88

Gambar 2. Tampilan Antar Muka Sistem

Implementasi dan Pengujian Sistem
Tabel 2 menunjukkan hasil pengujian Black Box terhadap seluruh use case
yang tersedia pada sistem. Pengujian mencakup proses login, registrasi akun,
pengelolaan data bus, pengelolaan rute dan jadwal, pencarian jadwal bus, pemilihan

ISSN 3123-4224
Vol. 2 No. 1

89

kursi, pemesanan tiket, pembayaran, verifikasi pembayaran, riwayat pemesanan,
pembatalan tiket, pembuatan laporan, hingga fitur yang digunakan oleh sopir
seperti melihat jadwal, melihat daftar penumpang, dan konfirmasi keberangkatan.

Tabel 2. Pengujian Black Box
Use Case Input Skenario Uji Expected Result Hasil
UC-01 Login Email: emaarung@gmail.com
Password: 12345678
Login dengan
kredensial
penumpang
valid
Redirect ke
halaman utama
penumpang
Valid
UC-01 Login Email: emaarung@gmail.com
Password: salah
Login dengan
password salah
Pesan error
"username dan
password salah"
Valid
UC-02
Registrasi Akun
Nama : Emagusri, Email:
emaarung@gmail.com,
Password:12345678
Registrasi data
lengkap dan
valid
Akun
tersimpan,
redirect ke
halaman
verifikasi OTP
Valid
UC-02
Registrasi Akun
Email yang sudah terdaftar Registrasi
dengan email
duplikat
Pesan error
"Email sudah
digunakan"
Valid
UC-03
Mengelola Data
Bus
Nama: Sinar Mekar, Kelas:
Business, Plat: DT 7089 UE,
Kapasitas:30, Fasilitas: AC,
Selimut
Tambah bus
baru dengan
data valid
Bus tersimpan,
muncul di
daftar
Valid
UC-04
Mengelola Rute
Nama: Manado-Toraja Tambah rute
baru
Rute tersimpan,
muncul di
daftar, notifikasi
sukses
Valid
UC-04
Mengelola Rute
Klik tombol " Atur Harga" pada
rute
Klik tombol
" Atur Harga
Segmen"
Halaman
pengaturan
harga per
segmen tampil
Valid
UC-05
Mengelola
Jadwal
Bus, Rute, Sopir, Waktu
Berangkat, Kursi Tersedia
Tambah jadwal
valid
Jadwal
tersimpan,
notifikasi
sukses
Valid
UC-06 Melihat
Jadwal Bus
Asal: Manado, Tujuan: Toraja,
Tanggal: 22/05/2026
Pencarian
jadwal yang
tersedia

Daftar jadwal
sesuai filter
ditampilkan
Valid
UC-06 Melihat
Jadwal Bus
Asal: Manado, Tujuan: Toraja,
Tanggal: 23/05/2026 (tidak ada
jadwal)
Pencarian
jadwal kosong

Pesan "Belum
ada jadwal
tersedia untuk
kriteria ini"
Valid
UC-07 Memilih
Kursi
Pilih kursi nomor 1 yang
tersedia
 Memilih kursi
yang tersedia
Kursi berubah
warna menjadi
biru (terpilih)
Valid

ISSN 3123-4224
Vol. 2 No. 1

90

Use Case Input Skenario Uji Expected Result Hasil
UC-07 Memilih
Kursi
Pilih kursi yang sudah terisi
(warna abu-abu/pink)
Memilih kursi
yang sudah
diambil
Kursi tidak
dapat dipilih,
tidak ada
perubahan
Valid
UC-08
Pemesanan
Tiket
Isi data penumpang lengkap,
pilih kategori umum
Pemesanan
tiket
Pemesanan
terkirim status
"Menunggu
Pembayaran"
Valid
UC-08
Pemesanan
Tiket
Nama tidak diisi, NIK kurang 16
digit
Pemesanan
dengan data
tidak lengkap
Pesan error
"Data tidak
lengkap atau
tidak valid"
Valid
UC-09
Pembayaran
Tiket
Transfer ke rekening tujuan,
upload bukti
Transfer
manual dan
upload bukti
Status menjadi
"Menunggu
Verifikasi"

Valid
UC-10
Verifikasi
Pembayaran
Admin klik "Verifikasi" pada
bukti valid
Verifikasi bukti
valid
Status menjadi
"Terbayar",
notifikasi ke
penumpang
Valid
UC-11 Melihat
Riwayat
Penumpang login, buka menu
riwayat
Buka menu
riwayat

Daftar pesanan
(kode booking,
status, tanggal)
tampil
Valid
UC-12
Pembatalan
Tiket
Batalkan tiket  Batalkan tiket
yang sudah di
pesan
Status
"Dibatalkan",
refund diproses,
kursi kembali
Valid
UC-13 Laporan
Pemesanan
Admin pilih periode: Mei 2026 Lihat laporan
per periode
Statistik &
grafik
(pendapatan,
jumlah tiket)
tampil
Valid
UC-13 Laporan
Pemesanan
Klik tombol “Cetak Laporan” Ekspor laporan

File PDF
laporan
terunduh
Valid
UC-14
Sopir Lihat
Jadwal
Sopir login, buka menu “ Jadwal
Saya”
Buka menu
"Jadwal Saya"
Tabel jadwal
(bus, rute,
waktu, status,
aksi) tampil
Valid
UC-15
Sopir Lihat
Daftar
Penumpang
Klik “Daftar Penumpang” pada
jadwal
Lihat daftar
penumpang
Nama
penumpang,
nomor kursi,
kategori
ditampilkan
Valid
UC-16
Konfirmasi
Keberangkatan
Klik “ Atur Perjalanan” dan
“Mulai”
Mulai
perjalanan
Status jadwal
jadi
"berangkat",
waktu
Valid

ISSN 3123-4224
Vol. 2 No. 1

91

Use Case Input Skenario Uji Expected Result Hasil
keberangkatan
tercatat
UC-16
Konfirmasi
Keberangkatan
Mulai perjalanan saat belum
waktunya
Konfirmasi
terlalu cepat

Pesan "Belum
waktunya
keberangkatan",
perjalanan
tidak dimulai
Valid

Hasil Pengujian Sistem, Konten dan Usability Testing

Tabel 3. Hasil Rata-rata Validasi Ahli Sistem
No Aspek Yang Dinilai Jumlah Butir Pertanyaan Rata-rata Penilaian
1 Functional suitability 5 4,4
2 Usability 7 4,4
3 Performance Efficiency 2 4,0
4 Security 2 4,5
5 Maintainability 2 4,5
Total Rata-rata keseluruhan 18 4,36

Berdasarkan pada Tabel 3, total rata -rata keseluruhan sebesar 4.36, maka
sistem dikategorikan "Sangat Layak" untuk digunakan. Dengan demikian, hasil
validasi oleh ahli sistem menunjukkan bahwa sistem informasi yang dikembangkan
telah memenuhi standar kelayakan dari sisi fungsionalitas, kegunaan, performa,
keamanan, dan kemudahan pemeliharaan.

Tabel 4. Hasil Rata-rata Validasi Ahli Konten
No Aspek Yang Dinilai Jumlah Butir Pertanyaan Rata-rata Penilaian
1 Usability 5 4,0
2 Information Quality 6 4,0
3 Interoperability 3 4,3
Total Rata-rata keseluruhan 13 4,1

Berdasarkan pada Tabel 4, total rata -rata keseluruhan sebesar 4.1, maka
sistem dikategorikan "Sangat Layak" untuk digunakan. Dengan demikian, hasil
validasi oleh ahli sistem menunjukkan bahwa sistem informasi yang dikembangkan
telah memenuhi standar kelayakan dari sisi fungsionalit as, kegunaan, performa,
keamanan, dan kemudahan pemeliharaan.

Tabel 5. Rekapitulasi Skor Rata-rata USE Questionnaire
No Dimensi Jumlah Butir Skor Rata-rata
1 Usefulness (U) 8 4,44
2 East of Use (EU) 9 4,37
3 East of Learning (EL) 6 4,30
4 Satisfaction (S) 7 4,45
Rata-rata Keseluruhan 30 4,39

ISSN 3123-4224
Vol. 2 No. 1

92

Berdasarkan pada Tabel 5, total rata -rata keseluruhan sebesar 4.39,
menunjukkan bahwa usability sistem berada pada kategori “Sangat Baik” untuk
digunakan. Dengan demikian, hasil dari  rata-rata skor pengujian usability
menunjukkan bahwa sistem informasi yang dikembangkan telah memenuhi standar
kelayakan dari sisi kegunaan, kemudahan penggunaan, kemudahan pembelajaran,
kepuasan.

KESIMPULAN

Berdasarkan hasil penelitian dan pengembangan yang telah dilakukan,
Sistem Informasi E -Ticketing pada Armada Bus PO. Harapan Kasih berhasil
dikembangkan menggunakan metode Agile Scrum yang meliputi tahapan Product
Backlog, Sprint Planning, Sprint Execution , Sprint Review, dan Deployment.
Penggunaan UML dalam perancangan membantu memvisualisasikan alur sistem
secara terstruktur, termasuk diagram aktivitas untuk proses pemesanan tiket dan
pengelolaan data oleh admin.
Pengujian fungsional menggunakan Black Box Testing menunjukkan bahwa
seluruh fitur sistem berjalan sesuai kebutuhan yang ditetapkan tanpa ditemukan
kesalahan kritis yang menghambat operasional. Hasil validasi oleh ahli sistem dan
ahli konten keduanya mengh asilkan kategori sangat layak, yang menunjukkan
bahwa sistem telah memenuhi standar kualitas dari sisi fungsionalitas, keamanan,
antarmuka, maupun kualitas konten. Uji usability yang melibatkan 35 responden
pada empat dimensi yaitu Usefulness, Ease of Use, Ease of Learning, dan Satisfaction
juga menghasilkan kategori sangat layak. Dengan demikian, sistem informasi e -
ticketing yang dikembangkan dinyatakan layak diimplementasikan dan efektif
dalam meningkatkan efisiensi serta kualitas layanan pemesanan tiket bus PO.
Harapan Kasih.

DAFTAR PUSTAKA

Amarta, A. A. F., & Anugrah, I. G. (2021). Implementasi Agile Scrum Dengan
Menggunakan Trello Sebagai Manajemen Proyek Di PT Andromedia. Jurnal
Nasional Komputasi Dan Teknologi Informasi (JNKTI), 4(6), 528 –534.
https://doi.org/10.32672/jnkti.v4i6.3702
Anggono, S. U., Achaqie, H. N. R., Kuncoro, W. A., & Huda, N. M. (2026). Evaluasi
Usability Sistem Pemesanan Menu Berbasis Web: Pendekatan Mixed -
Methods Menggunakan SUS dan UEQ.  Jurnal Ilmiah Sistem Informasi , 5(1),
593-605.
Djamen, A., Mustafah, F. M., & Rianto, I. (2023). Sistem Monitoring Jumlah Parkir
Berbasis Internet Of Things (IOT) di Manado Town Square 3. JOINTER :
Journal of Informatics Engineering, 4(02), 1 –15.
https://doi.org/10.53682/jointer.v4i02.240

ISSN 3123-4224
Vol. 2 No. 1

93

Hardiansyah, F., Rizal, A., & Purnamasari, I. (2023). Implementasi Metode Agile
Scrum Dalam Pengembangan Aplikasi Pembelajaran Olahraga. JATI (Jurnal
Mahasiswa Teknik Informatika), 7(2), 1242 –1247.
https://doi.org/10.36040/jati.v7i2.6734
Hidayanti, S., Palilingan, V., & Mewengkang, A. (2025). Pengembangan Sistem
Informasi Pengelolaan Dana Komite Berbasis Web di SMK Negeri 1 Mopuya.
JOURNAL OF EDUCATION METHOD AND TECHNOLOGY, 3(1), 61 –70.
https://doi.org/10.70716/jocsit.v1i1.190
Korompot, O., Djamen, A. C., & Parinsi, M. T. (2025). Pengembangan Sistem Informasi
Inventory Barang berbasis Web di Fakultas Teknik. 3(2), 10–20.
Latifah, N., Taufiq, M., & Fitri, S. (2026). Evaluasi Fungsional Sistem Informasi
Manajemen Kemasjidan Berbasis Web Menggunakan Metode Black Box
Testing. Switch: Jurnal Sains dan Teknologi Informasi, 4(4), 161-173.
Lelet, M., Kaparang, D. R., & Pratasik, S. (2023). Pengembangan Sistem Informasi
Layanan Mahasiswa Fakultas Teknik Universitas Negeri Manado. Edutik :
Jurnal Pendidikan Teknologi Informasi Dan Komunikasi, 3(1), 138 –148.
https://doi.org/10.53682/edutik.v3i1.6867
Prasojo, G. A., & Kontesta, R. P. (2023). Rancang Bangun Aplikasi Pemesanan Tiket
Bus Online (BeTik Bus)Berbasis Website. JIFOTECH (JOURNAL OF
INFORMATION TECHNOLOGY) Vol., 3(1).
Rachman, F. N., Hadiwijaya, N. A., & Bustomi, T. (2024). Rancang Bangun Aplikasi
Pemesanan Tiket Kapal Menggunakan Framework Laravel. JURNAL VOKASI
TEKNIK (JuVoTek), 2(2). https://doi.org/10.12345/xxxxx
Ramdhani, A. I., Khasanah, S., & Farizki , R. (2020). SISTEM APLIKASI PEMESANAN
TIKET BUS BERBASIS WEBSITE PADA PO SINAR JAYA Adhitya. 2(9).
Sari, T. V., Olii, D., & Kaparang, D. R. (2025). Perancangan Sistem Informasi Desa
Mopuya Utara II berbasis Website. 3(3), 40–50.
Trisnawati, L., Setiawan, D., & Budiman. (2022). Sistem Monitoring Kegiatan
Kemahasiswaan Menggunakan Metode Agile Development. JOISIE Journal Of
Information System And Informatics Engineering, 6(1), 49–57.
Vita Ariska, Tiara Aulia, & Tinuk Agustin. (2023). Sistem Informasi Pemesanan Tiket
Bus Online Berbasis Website Pada Po.Haryanto. Jurnal Penelitian Sistem
Informasi (Jpsi), 1(3), 107–117.
Wiharko, T., & Setiawan, H. (2020). Sistem Informasi E-Ticketing di PT Pos Indonesia
Cabang Cianjur berbasis Web dengan Metode Fifo. Media Jurnal Informatika,
10(2), 36. https://doi.org/10.35194/mji.v10i2.881.
