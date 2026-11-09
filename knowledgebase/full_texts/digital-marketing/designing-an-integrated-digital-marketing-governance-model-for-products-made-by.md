---
title: Designing an Integrated Digital Marketing Governance Model for Products Made by Inmates in Correctional
  Institutions
url: https://doi.org/10.32520/stmsi.v15i6.6485
category: digital-marketing
subcategory: review
date: 2026-06
venue: SISTEMASI
authors:
- Melanie Mardolna Sine
- Eko Sediyono
- Evi Maria
source: openalex-oa
pdf_url: https://sistemasi.ftik.unisi.ac.id/index.php/stmsi/article/download/6485/1298
pages: 12
chars: 47177
fetched_at: '2026-11-08T18:05:38+00:00'
kb_version: 1
---

# Designing an Integrated Digital Marketing Governance Model for Products Made by Inmates in Correctional Institutions

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2316

Desain Model Tata Kelola Pemasaran Digital Terintegrasi bagi
Produk Warga Binaan pada Lingkungan Pemasyarakatan

Designing an Integrated Digital Marketing Governance Model for
Products Made by Inmates in Correctional Institutions

1Melanie Mardolna Sine,  2Eko Sediyono, 3Evi Maria*
1,2,3Departemen sistem Informasi, Teknologi Informasi, Universitas Kristen Satya Wacana
Salatiga, Indonesia
*e-mail: evi.maria@uksw.edu

(received: 27 May 2026, revised: 15 June 2026, accepted: 16 June 2026)

Abstrak
Penelitian ini bertujuan untuk mengembangkan model tata kelola pemasaran digital terintegrasi bagi
produk warga binaan pada lingkungan pemasyarakatan. Permasalahan penelitian terletak pada belum
terintegrasinya aktivitas pemasaran produk warga binaan, mulai dari pengelo laan produk, promosi
digital, transaksi penjualan, hingga pelaporan aktivitas yang sebagian besar masih dilakukan secara
manual. Penelitian menggunakan Design Science Research (DSR) melalui tahapan identifikasi
kebutuhan sistem, p erancangan model, pengembangan arsitektur sistem, visualisasi proses bisnis,
serta evaluasi konseptual melalui review ahli dan diskusi terbatas. Penelitian ini menghasilkan model
tata kelola pemasaran digital terintegrasi yang menghubungkan pengelolaan produk, promosi digital,
transaksi penjualan, dokumentasi aktivitas, monitoring digital, dan pengawasan institusional dalam
satu mekanisme tata kelola. Evaluasi konseptual yang melibatkan empat evaluator, terdiri atas dua
petugas pembinaan dan dua pengelola k egiatan kerja, menunjukkan bahwa model dinilai sesuai
dengan kebutuhan pengelolaan pemasaran digital pada lingkungan pemasyarakatan. Penelitian juga
menunjukkan bahwa pemanfaatan media sosial, marketplace, dan platform komunikasi digital dapat
mendukung pe masaran produk warga binaan tanpa menghilangkan mekanisme pengawasan
institusional. Kontribusi penelitian terletak pada pengembangan model tata kelola pemasaran digital
berbasis pengawasan institusional yang dapat diterapkan melalui pendekatan low-cost dig ital
architecture pada organisasi dengan pembatasan akses digital yang tinggi.
Kata kunci: lingkungan pemasyarakatan , design science research, tata kelola digital, pemasaran
digital, sistem informasi
Abstract
This study aims to develop an integrated digital marketing governance model for products made
by inmates in correctional institutions. The research addresses the lack of integration in the
marketing activities of inmate -produced products, where product management, digital promotion,
sales transactions, and activity reporting are largely performed through fragmented and manual
processes. The study adopts the Design Science Research (DSR) methodology, encompassing the
stages of system requirements identification, model design, system arch itecture development, business
process visualization, and conceptual evaluation through expert review and focused group
discussions. The proposed model integrates product management, digital promotion, sales
transactions, activity documentation, digital mo nitoring, and institutional oversight into a unified
digital marketing governance framework. The conceptual evaluation involved four experts,
comprising two correctional rehabilitation officers and two vocational program managers, who
confirmed that the pr oposed model adequately addresses the digital marketing management needs of
correctional institutions.  The findings further demonstrate that the use of social media, online
marketplaces, and digital communication platforms can effectively support the marke ting of inmate -
produced products while maintaining appropriate institutional oversight and security controls. This
study contributes by proposing an institutionally governed digital marketing model that can be
implemented through a low-cost digital architecture, making it particularly suitable for organizations
operating in environments with strict digital access restrictions.

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2317

Keywords: correctional institutions, design science research, digital governance, digital marketing,
information systems

1 Pendahuluan
Pemasaran digital dalam bidang sistem informasi tidak lagi dipahami sebagai aktivitas promosi,
tetapi bagian dari sistem digital yang mengintegrasikan pengelolaan informasi, transaksi, komunikasi
pelanggan, dan pelaporan organisasi  [1]. Dalam bidang sistem informasi, integrasi pemasaran digital
dengan platform digital terbukti mampu meningkatkan efisiensi operasional, memperluas jangkauan
pasar, men ingkatkan customer engagement , dan memperkuat pengambilan keputusan berbasis data
[2], [3]. Perkembangan tersebut mendorong berbagai organisasi, termasuk UMKM dan usaha berbasis
komunitas, mulai mengintegrasikan media sosial dan marketplace ke dalam aktivitas bisnis mereka.
Namun demikian, sebagian besar penelitian me ngenai pemasaran digital  masih berfokus pada
organisasi bisnis yang bersifat terbuka  dan memiliki akses teknologi yang fleksibel, seperti e-
commerce, retail digital , dan UMKM konvensional  [4], [5]. Penelitian terdahulu umumnya
menempatkan pemasaran digital  sebagai alat promosi dan peningkatan penjualan,  sementara aspek
tata kelola sistem digital dan kontrol organisasi masih relatif sedikit dibahas. Padahal, tidak semua
organisasi memiliki karakteristik yang sama dalam penggunaan teknologi digital. Pada organisasi
tertentu, terutama organisasi dengan kont rol institusional yang tinggi, penggunaan platform digital
tidak dapat diterapkan secara bebas sebagaimana pada bisnis konvensional.
Pada lingkungan pemasyarakatan, penggunaan teknologi digital tidak hanya untuk mendukung
pemasaran produk, tetapi juga mempertimbangkan keamanan informasi, pembatasan akses digital,
pengawasan transaksi . Berbeda dengan organisasi bisnis umum yang menekankan keterbukaan
interaksi digital, lingkungan pemasyarakatan memerlukan mekanisme pengawasan dalam setiap
aktivitas digital [6], [7]. Karena itu, pendekatan digital commerce konvensional tidak dapat diterapkan
secara langsung tanpa penyesuaian terhadap kebutuhan pengendalian institusional  [8]. Konteks ini
menjadi semakin penting karena lingkungan pemasyarakatan saat ini tidak hanya berfungsi sebagai
tempat menjalani hukuman, tetapi juga sebagai ruang reintegrasi sosial bagi  warga binaan
pemasyarakatan (WBP) [9]. Melalui berbagai kegiatan produktif , WBP menghasilkan produk kreatif
seperti tenun, kerajinan tangan, tata boga, salon, dan hasil pertanian sederhana  yang memiliki nilai
ekonomi dan potensi pasar. Aktivitas tersebut tidak hanya menduk ung penguatan keterampilan dan
kemandirian WBP, tetapi juga bagian dari rehabilitasi sosial. Oleh sebab itu, pemasaran produk WBP
tidak hanya berkaitan dengan aspek ekonomi, tetapi juga merupakan upaya rehabilitasi dan
pemberdayaan sosial warga binaan.
Meskipun demikian, hasil observasi pada Lapas Perempuan Kelas II B Kupang menunjukkan
bahwa pengelolaan pemasaran dilakukan secara konvensional. Pencatatan produk dan transaksi
penjualan masih dilakukan s ecara manual, promosi produk masih bergantung pada pameran dan
komunikasi langsung, serta belum tersedia sistem digital yang mampu mengintegrasikan katalog
produk, promosi digital, transaksi dan pelaporan penjualan secara terstruktur. Selain itu, promosi
produk masih bersifat sementara dan belum memiliki mekanisme digital yang mampu mendukung
pemasaran secara berkelanjutan. Kondisi tersebut menyebabkan jangkauan pemasaran produk menjadi
terbatas dan potensi ekonomi produk WBP belum berkembang secara optimal.
Permasalahan tersebut menunjukkan bahwa tantangan utama dalam pemasaran digital produk
WBP bukan hanya rendahnya penggunaan media sosial atau marketplace, tetapi belum adanya model
tata kelola pemasaran digital yang sesuai dengan karakteristik l ingkungan pemasyarakatan. Pada
organisasi bisnis umum, pemasaran digital dapat diterapkan secara terbuka dan fleksibel. Sebaliknya,
pada lingkungan pemasyarakatan, seluruh aktivitas pemasaran harus mempertimbangkan validasi
produk, kontrol akses digital, pengawasan transaksi, dan pembatasan interaksi digital antara WBP dan
pihak luar. Oleh karena itu, l ingkungan pemasyarakatan tidak hanya membutuhkan media promosi
digital, tetapi membutuhkan model tata kelola pemasaran digital yang mampu mengintegrasikan
pemasaran, pengelolaan informasi, dan kontrol institusional dalam satu sistem yang terstruktur.
Secara akademik, penelitian mengenai pemasaran digital  pada organisasi dengan keterbatasan
akses digital masih relatif sedikit. Sebagian besar penelitian sistem informasi  masih menempatkan
pemasaran digital sebagai instrumen promosi dan peningkatan penjualan, bukan sebagai bagian dari
desain tata kelola organisasi dengan kebutuhan pengawasan institusional  dan controlled digital
interaction [10]. Selain itu, penelitian yang secara khusus membahas integrasi media sosial,

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2318

marketplace, pengelolaan data produk, dan mekanisme pengawasan institusi dalam lingkungan
pemasyarakatan juga masih sangat terbatas. Kondisi tersebut menunjukkan adanya research gap
mengenai bagaimana model tata kelola pemasaran digital dapat dirancang secara terintegrasi untuk
organisasi dengan karakteristik terbatas dan terkontrol seperti lingkungan pemasyarakatan.
Berdasarkan kondisi tersebut, penelitian ini bertujuan mendesain model tata kelola pemasaran
digital terintegrasi bagi produk warga binaan pada lingkungan pemasyaraka tan. Penelitian ini
menggunakan pendekatan Design Science Research  (DSR) karena penelitian ini tidak hanya
menganalisis masalah, tetapi juga menghasilkan artefak berupa model tata kelola pemasaran digital
yang sesuai dengan kebutuhan l ingkungan pemasyarakatan. Model yang dikembangkan mencakup
pengelolaan data produk, katalog digital, promosi berbasis media sosial dan marketplace, transaksi
penjualan, pelaporan, monitoring pemasaran, serta mekanisme kontrol institusional dan keterlibatan
stakeholder. Penelitian ini diharapkan dapat memberikan kontribusi dalam pengembangan sistem
informasi dan digital governance pada organisasi dengan keterbatasan akses digital, sekaligus
mendukung transformasi digital program pembinaan dan pemberdayaan ekonomi warga binaan secara
lebih terstruktur dan berkelanjutan.

2 Tinjauan Literatur
Studi pemasaran digital  dalam sistem informasi selama ini lebih banyak dibangun dalam
orientasi kinerja penjualan dan efisiensi transaksi  [3], [4], [11]. Dalam penelitian tersebut,
keberhasilan sistem digital umumnya d iukur dari efisiensi transaksi, kemudahan penggunaan sistem,
dan peningkatan interaksi pelanggan. Akibatnya, aspek kontrol organisasi sering tidak menjadi
perhatian utama dalam desain sistem digital.  Pandangan tersebut juga terlihat pada penelitian sistem
informasi penjualan yang banyak menekankan usability system, efisiensi transaksi , dan adopsi e-
commerce pada organisasi bisnis terbuka. Fokus penelitian  diarahkan pada bagaimana sistem dapat
mempercepat transaksi dan memperluas interaksi pasar  [5]. Sebagian besar model pemasaran digital
akhirnya dibangun dengan asumsi bahwa organisasi memiliki akses digital terbuka dan interaksi
pengguna yang relatif bebas.
Pendekatan tersebut menjadi kurang memadai ketika diterapkan pada organisasi dengan
mekanisme pengawasan yang lebih ketat. Pada kondisi seperti ini, desain sistem digita l tidak hanya
berkaitan dengan efisiensi transaksi, tetapi juga dengan kemampuan menjag a konsistensi pengawasan
dan validitas aktivitas digital [12]. Kajian digital governance menunjukkan bahwa sistem digital tidak
hanya berfungsi sebagai media transaksi, tetapi juga mekanisme koordinasi dan kontrol organisasi.
Karena itu, desain sistem perlu menyesuaikan karakteristik organisasi yang menggunakannya. Sistem
yang dirancang untuk organisasi bisnis terbuka belum tentu sesuai diterapkan pada organisasi dengan
pembatasan akses dan pengawasan aktivitas digital yang lebih ketat.
Kesenjangan penelitian terlihat dari dominannya konteks retail digital, e-commerce, dan UMKM
dalam kajian pemasaran digital dan sistem informasi penjualan [3], [4], [5]. Sebagian besar penelitian
masih berorientasi pada kinerja bisnis, sedangkan aspek pengawasan aktivitas, validasi proses, kontrol
akses, dan institutional supervision belum banyak dibaha s sebagai bagian inti dari desain sistem
digital [10],[13],[14]. Studi mengenai tata kelola sistem digital pada organisasi dengan  pembatasan
akses digital masih relatif terbatas [6],[15]. Berbeda dengan penelitian sebelumnya yang berorientasi
pada peningkatan kinerja bisnis dan efisiensi transaksi, penelitian ini  menempatkan pemasaran digital
sebagai bagian dari tata kelola sistem digital. Karena itu, penelitian ini tidak hanya mem bahas
penggunaan media sosial atau marketplace sebagai media promosi, tetapi mengembangkan model
yang mengintegrasikan promosi digital, transaksi, pelaporan, monitoring aktivitas, validasi proses,
dan kontrol institusional dalam satu tata kelola sistem digital yang terstruktur.

3 Metode Penelitian
Penelitian ini menggunakan pendekatan Design Science Research (DSR) untuk merancang
model tata kelola pemasaran digital terintegrasi bagi produk warga binaan pada lingkungan
pemasyarakatan. Pendekatan DSR dipilih karena penelitian tidak hanya berfokus pada identifikasi
permasalahan, tetapi juga menghasilkan artefak berupa model tata kelola sistem digital yang dapat
digunakan sebagai solusi terhadap permasalahan pemasaran produk warga binaan. Dalam bidang
sistem informasi, DSR digunakan untuk mengembangkan artefak seperti model, framework, metode,

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2319

maupun desain sistem yang berorientasi pada penyelesaian masalah organisasi melalui pendekatan
berbasis teknologi dan tata kelola digital [16], [17].
Penelitian dilakukan pada Lapas Perempuan Kelas II B Kupang sebaga i salah satu  lingkungan
pemasyarakatan yang menjalankan program pembinaan kemandirian melalui berbagai kegiatan
produksi produk kreatif warga binaan. Subjek penelitian meliputi petugas pembinaan, pengelola
kegiatan kerja, dan warga binaan yang terlibat dal am aktivitas produksi dan pemasaran produk.
Pemilihan lokasi penelitian didasarkan pada masih terbatasnya pemanfaatan sistem digital dalam
pengelolaan pemasaran produk warga binaan, sementara aktivitas produksi telah berjalan secara rutin
dan memiliki potensi ekonomi yang cukup berkembang.
Pengumpulan data dilakukan melalui observasi, wawancara semi -terstruktur, dan dokumentasi.
Observasi dilakukan terhadap proses pengelolaan produk, pencatatan transaksi, promosi, dan
pelaporan penjualan. Wawancara dilakuk an dengan petugas pembinaan dan pengelola kegiatan kerja
untuk mengidentifikasi kebutuhan sistem, kendala pemasaran, serta kebutuhan pengawasan
institusional dalam aktivitas pemasaran produk warga binaan. Dokumentasi digunakan untuk
melengkapi data terkait proses produksi, katalog produk, pencatatan penjualan, serta aktivitas promosi
yang telah berjalan.
Tahapan penelitian mengacu pada tahapan DSR  [17] disajikan pada Gambar 1 . Tahapan
penelitian dimulai dari identifikasi permasalahan pemasaran produk warga binaan, dilanjutkan dengan
analisis kebutuhan sistem  dan perancangan model tata kelola pemasaran digital terintegrasi. Model
yang dihasilkan kemudian divisualisasikan melalui use case diagram, activity diagram, dan arsitektur
sistem sebelum dievaluasi secara konseptual melalui review ahli dan diskusi terbatas dengan petugas
pembinaan serta pengelola kegiatan kerja di Lapas Perempuan Kelas IIB Kupang.

Gambar 1 Tahapan DSR dalam pengembangan model tata kelola pemasaran digital
Tahap identifikasi masalah dilakukan melalui observasi terhadap proses pemasaran produk warga
binaan yang masih dilakukan secara konvensional dan belum terintegrasi secara digital. Tahap analisis
kebutuhan dilakukan untuk mengidentifikasi kebutuhan sistem terkait pengelolaan data produk,
katalog digital, promosi berbasis media sosial dan marketplace, transaksi penjualan, pelaporan,
monitoring aktivitas, dan kontrol institusional. Berdasarkan hasil analisis kebutuhan, penelitian
kemudian merancang artefak be rupa model tata kelola pemasaran digital terintegrasi yang
divisualisasikan melalui use case diagram, activity diagram, dan arsitektur sistem pemasaran digital.

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2320

Evaluasi model dilakukan melalui review ahli dan diskusi terbatas yang melibatkan empat
evaluator, terdiri atas dua petugas pembinaan dan dua pengelola kegiatan kerja pada Lapas Perempuan
Kelas IIB Kupang yang terlibat dalam aktivitas pemasaran dan pengelolaan produk warga binaan.
Karena penelitian ini masih berada pada tahap pengembangan artefak d an belum sampai pada
implementasi sistem secara penuh, evaluasi difokuskan pada penilaian kesesuaian konseptual dan
kelayakan model. Aspek yang dievaluasi meliputi kelengkapan komponen model, kemudahan
implementasi, dukungan terhadap aktivitas pemasaran pr oduk, serta kemampuan model dalam
mendukung mekanisme monitoring dan pengawasan institusional pada lingkungan dengan
pembatasan akses digital. Hasil evaluasi digunakan sebagai dasar penyempurnaan struktur model dan
integrasi antar komponen sistem yang dikembangkan.

4 Hasil dan Pembahasan
4.1 Permasalahan dan Kebutuhan Tata Kelola Pemasaran Digital
Hasil penelitian menunjukkan bahwa kegiatan pembinaan kemandirian di Lapas Perempuan
Kelas II B Kupang telah menghasilkan berbagai produk warga binaan pemasyarakatan  (WBP), seperti
produk tata boga, tenun, rajutan, salon dan hasil kebun. Aktivitas produksi tersebut dikelola secara
rutin dalam program pembinaan kemandirian yang melibatkan warga binaan, petugas pembinaan, dan
pengelola kegiatan kerja. Produk yang dihasi lkan tidak hanya menjadi bagian dari aktivitas
pembinaan keterampilan, tetapi juga mulai diarahkan sebagai bagian dari penguatan kemandirian
ekonomi warga binaan. Meskipun kegiatan produksi berjalan aktif, hasil observasi menunjukkan
bahwa pengelolaan pema saran produk masih dilakukan secara sederhana dan belum didukung tata
kelola digital yang memadai. Pengelola kegiatan kerja masih melakukan pencatatan stok produk dan
transaksi penjualan secara manual melalui buku administrasi. Kondisi tersebut menyebabkan  data
produk, transaksi penjualan, dan laporan pemasaran belum terdokumentasi secara konsisten sehingga
proses monitoring penjualan masih sulit dilakukan secara sistematis.
Pada aspek promosi, petugas pembinaan dan pengelola kegiatan masih mengandalkan keg iatan
pameran, komunikasi personal, serta penyebaran informasi melalui media sosial sederhana untuk
memperkenalkan produk warga binaan. Informasi produk belum dikelola dalam katalog digital yang
terstruktur dan belum terhubung dengan sistem pencatatan transaksi maupun pengelolaan data produk.
Akibatnya, aktivitas promosi, penjualan dan pelaporan masih berjalan secara terpisah dan belum
memiliki alur koordinasi yang konsisten. Penelitian juga menemukan bahwa proses pemesanan dan
transaksi produk masih bergantung pada interaksi langsung antara konsumen dan petugas pembinaan.
Ketergantungan pada mekanisme manual tersebut menyebabkan distribusi informasi produk dan
pengelolaan transaksi belum mampu mendukung perluasan pemasaran secara lebih luas.
Selain keterbatasan pemasaran digital, hasil wawancara dengan petugas pembinaan dan
pengelola kegiatan kerja menunjukkan bahwa seluruh aktivitas digital tetap harus berada dalam
pengawasan institusi pemasyarakatan. Aktivitas promosi, komunikasi pelanggan, transaksi penjualan,
dan pengelolaan data produk tidak dapat dilakukan secara bebas seperti pada organisasi bisnis umum.
Karena itu, kebutuhan sistem tidak hanya berkaitan dengan promosi dan transaksi penjualan, tetapi
juga berkaitan dengan monitoring akti vitas, validasi proses, dokumentasi transaksi, dan pengelolaan
akses pengguna dalam lingkungan pemasyarakatan.
Berdasarkan hasil observasi dan wawancara dengan petugas pembinaan, pengelola kegiatan
kerja, dan warga binaan, penelitian mengidentifikasi beberapa kebutuhan utama dalam pengembangan
tata kelola pemasaran digital produk warga binaan. Kebutuhan utama sistem meliputi pengelolaan
data produk, koordinasi promosi digital, pencatatan transaksi, pelaporan aktivitas pemasaran,
monitoring aktivitas penggu na, dan mekanisme kontrol institusional terhadap aktivitas digital. Selain
itu, sistem juga perlu mendukung keterlibatan petugas pembinaan dalam proses validasi aktivitas
pemasaran dan pengawasan transaksi penjualan. Hasil identifikasi tersebut menunjukkan  bahwa
permasalahan utama tidak hanya terletak pada keterbatasan media promosi digital, tetapi juga pada
belum adanya tata kelola sistem digital yang mampu menghubungkan aktivitas pemasaran, transaksi,
pelaporan, dan pengawasan institusional dalam satu mek anisme tata kelola digital terintegrasi.
Temuan tersebut memperlihatkan bahwa kebutuhan organisiasi pemasyarakatan tidak hanya berkaitan
dengan perluasan pemasaran produk warga binaan, tetapi juga dengan kemampuan sistem dalam
menjaga koordinasi, dokumentasi aktivitas, dan pengawasan digital secara berkelanjutan.

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2321

4.2 Desain Model Tata Kelola Pemasaran Digital Terintegrasi
Berdasarkan hasil identifikasi kebutuhan sistem, penelitian mengembangkan model tata kelola
pemasaran digital terintegrasi yang menghubungka n promosi digital, transaksi penjualan, pelaporan
aktivitas, dan pengawasan institusional dalam satu mekanisme tata kelola digital yang ter integrasi.
Model ini dikembangkan untuk mengatasi fragmentasi pengelolaan pemasaran produk warga binaan
yang sebelumnya masih berjalan secara terpisah antara aktivitas promosi dan transaksi . Model yang
dikembangkan menempatkan pengelolaan data produk sebagai pusat koordinasi aktivitas digital.
Seluruh data produk, stok, transaksi penjualan, promosi, dan laporan aktivitas dihubungkan dalam
satu alur pengelolaan sehingga proses pemasaran tidak lagi bergantung pada mekanisme manual dan
komunikasi personal. Pendekatan t ersebut memungkinkan proses pemasaran berjalan secara lebih
terstruktur dan mudah dimonitor.
Berbeda dengan sistem pemasaran digital  pada organisasi bisnis umum, model yang
dikembangkan dalam penelitian ini menempatkan pengawasan institusional sebagai bag ian inti dari
tata kelola sistem digital. Aktivitas promosi, transaksi penjualan, komunikasi pelanggan, dan publikasi
produk tetap berada pada koordinasi  petugas pembinaan dan pengelola kegiatan kerja. Karena itu,
sistem tidak hanya berfungsi sebagai media pemasaran digital, tetapi juga sarana validasi aktivitas dan
pengendalian interaksi dalam lingkungan pemasyarakatan.  Dalam model yang dikembangkan, media
sosial, marketplace, dan layanan komunikasi digital digunakan untuk mendukung promosi produk dan
interaksi pelanggan. Seluruh aktivitas digital tetap terhubung dengan database produk, pencatatan
transaksi, dan pelaporan aktivitas sehingga proses pemasaran dapat berjalan secara lebih terstruktur
dan terdokumentasi tanpa menghilangkan mekanisme pengawasan lingkungan pemasyarakatan.
Integrasi antara governance layer , digital marketing layer , dan database layer  menunjukkan
bahwa model yang dikembangkan tidak hanya berorientasi pada efisiensi pemasaran digital, tetapi
juga pada pengendalian aktivitas digital da lam lingkungan organisasi dengan tingkat regulasi tinggi.
Dalam konteks pemasyarakatan, aktivitas publikasi produk, interaksi pelanggan, dan transaksi
penjualan tidak dapat diposisikan sebagai aktivitas digital yang sepenuhnya terbuka sebagaimana pada
platform e -commerce konvensional. Oleh karena itu, model ini mengintegrasikan validasi produk,
kontrol akses pengguna, dokumentasi aktivitas, dan monitoring digital sebagai bagian dari struktur
tata kelola sistem. Pendekatan tersebut memungkinkan proses digitalisasi pemasaran berjalan secara
lebih akuntabel dan terkendali sesuai kebutuhan lingkungan pemasyarakatan.
Model tata kelola digital yang dikembangkan terdiri atas beberapa komponen utama, yaitu user
layer, digital marketing layer, governance & monitoring layer, appl ication and database layer, serta
infrastructure layer. User layer melibatkan petugas pembinaan, pengelola kegiatan kerja,  warga
binaan,  konsumen, dan stakeholder eksternal sebagai pihak yang terlibat dalam proses pemasaran
digital. Digital marketing layer memanfaatkan media sosial , marketplace, dan layanan komunikasi
digital untuk mendukung promosi produk dan interaksi pelanggan. Selanjutnya, governance &
monitoring layer berfungsi sebagai mekanisme pengawasan institusional yang mendukung validasi
publikasi produk, monitoring aktivitas dan transaksi, dokumentasi aktivitas, dan kontrol akses
pengguna. Pada sisi operasional, application and database layer  digunakan untuk mendukung
pengelolaan produk, katalog digital, transaksi penjualan, pelanggan, promosi, serta pelaporan aktivitas
pemasaran yang terhubung dalam database terintegrasi. Sementara itu , infrastructure layer
mendukung operasional sistem melalui server, database, jaringan internet, dan mekanisme keamanan
sistem yang memungkinkan aktivitas digital berjalan secara lebih stabil dan terdokumentasi.
Hubungan antara aktor , alur aktivitas, dan struktur sistem  dalam model divisualisasikan  melalui
model tata kelola pemasaran digital terintegrasi (Gambar 2),  use case diagram  (Gambar 3), activity
diagram (Gambar 4) , dan arsitektur sistem digital  (Gambar 5) . Visualisasi tersebut menunjukkan
bahwa sistem tidak hanya mendukung aktivitas promosi dan transaksi digital , tetapi juga koordinasi
informasi, dokumentasi aktivitas, dan pengawasan institusional secara berkelanjutan. Selain itu,
penelitian merancang model menggunakan low-cost digital architecture dengan memanfaatkan
platform digital yang te lah tersedia tanpa memerlukan pengembangan aplikasi yang kompleks.
Pendekatan tersebut dipilih agar model dapat diterapkan secara lebih realistis sesuai keterbatasan
sumber daya lingkungan pemasyarakatan. Dengan pendekatan tersebut, digitalisasi pemasaran produk

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2322

warga binaan tetap dapat berjalan secara lebih luas, terdokumentasi, dan tetap berada dalam
mekanisme tata kelola lingkungan pemasyarakatan.

Gambar 2 Model tata kelola pemasaran digital terintegrasi

Gambar 3 Use case sistem informasi pemasaran digital terintegrasi

Gambar 4 Activity diagram tata kelola pemasaran digital terintegrasi

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2323

Gambar 5 Skema arsitektur sistem informasi pemasaran digital terintegrasi

4.3  Evaluasi dan Validasi Model Tata Kelola Pemasaran Digital Terintegrasi
Evaluasi dan validasi model dilakukan untuk menilai kesesuaian desain tata kelola pemasaran
digital terintegrasi dengan kebutuhan operasional lingkungan pemasyarakatan. Proses evaluasi
menunjukkan bahwa model yang dikembangkan memiliki kesesuaian dengan kebutuhan pengelolaan
pemasaran digital pada lingkungan pemasyarakatan . Karena penelitian ini masih berada pada tahap
pengembangan artefak dan belum sampai pada implementasi sistem secara  penuh, evaluasi
difokuskan pada penilaian kesesuaian konseptual dan kelayakan model berdasarkan perspektif
evaluator yang terlibat dalam pengelolaan pemasaran produk warga binaan.  Hasil evaluasi konseptual
terhadap model yang dikembangkan diringkas pada Tabel 1.
Tabel 1 Hasil evaluasi dan validasi model tata kelola pemasaran digital terintegrasi
Aspek
Evaluasi
Temuan Utama Implikasi terhadap Tata
Kelola
Pengelolaan
Data Produk
Seluruh evaluator menyatakan bahwa integrasi data
produk dalam satu basis data mempermudah proses
dokumentasi dan pelacakan informasi produk
dibandingkan mekanisme pencatatan manual yang
digunakan sebelumnya.
Mendukung dokumentasi
produk dan mempermudah
monitoring dan pelaporan
aktivitas digital
Katalog
Digital
Evaluator meni lai bahwa penyajian katalog digital
membuat informasi produk lebih terstruktur dan lebih
mudah dipahami dibandingkan mekanisme promosi
yang digunakan sebelumnya.
Memperkuat penyajian
informasi produk secara
digital
Sistem
Pemesanan
dan Transaksi
Seluruh evaluator menyatakan bahwa integrasi proses
pemesanan dan pencatatan transaksi berpotensi
mengurangi ketergantungan pada pencatatan manual
serta mempermudah dokumentasi penjualan.
Mendukung efisiensi
transaksi dan dokumentasi
penjualan
Pelaporan
Aktivitas
Evaluator menilai bahwa ketersediaan data transaksi
dan aktivitas pemasaran dalam satu sistem
mempermudah penyusunan laporan dan proses
monitoring kegiatan.
Mendukung monitoring dan
evaluasi aktivitas
pemasaran
Pemanfaatan Evaluator menilai bahwa pemanfaatan media sosial Memperluas jangkauan

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2324

Media Sosial dan marketplace berpotensi memperluas jangkauan
informasi produk dibandingkan pendekatan promosi
yang selama ini bergantung pada pameran dan
komunikasi langsung.
pemasaran produk
Integrasi
Platform
Digital
Evaluator menyatakan bahwa integrasi media sosial
dan marketplace mendukung koordinasi aktivitas
promosi dan komunikasi pelanggan secara lebih
terstruktur.
Mendukung koordinasi
aktivitas pemasaran digital
Kemudahan
akses
Informasi
Evaluator menilai bahwa penyediaan informasi
produk secara digital berpotensi meningkatkan
kemudahan akses informasi bagi calon konsumen.
Meningkatkan aksesibilitas
informasi produk
Efektivitas
Pemasaran
Evaluator menilai bahwa perluasan akses informasi
dan kemudahan pemesanan berpotensi mendukung
peningkatan minat beli serta pemasaran produk
warga binaan.
Mendukung keberlanjutan
pemasaran produk warga
binaan
Secara umum, keempat evaluator menyatakan bahwa model yang dikembangkan telah mencakup
komponen utama yang dibutuhkan dalam pengelolaan pemasaran digital produk warga binaan,
khususnya terkait integrasi pengelolaan produk, promosi digital, transaksi, pelaporan, dan
pengawasan institusional. Namun demik ian, evaluator juga menekankan bahwa ef ektivitas
implementasi model masih dipengaruhi oleh kesiapan sumber daya manusia, konsistensi pengawasan
institusional, serta kemampuan organisasi dalam mengelola aktivitas digital secara berkelanjutan.
Evaluator menilai bahwa aspek sistem informasi memberikan kontribusi utama pada pengelolaan
data produk, pencatatan transaksi, dan penyusunan laporan aktivitas pemasaran. Sebelum model
dikembangkan, sebagian besar aktivitas pencatatan masih dilakukan secara manual sehingga proses
dokumentasi produk dan trans aksi belum berjalan secara konsisten. Melalui model yang
dikembangkan, pengelolaan informasi produk dan transaksi menjadi lebih terstruktur sehingga
mempermudah proses monitoring dan pelaporan aktivitas pemasaran.
Pada aspek pemasaran digital, evaluator me nilai bahwa integrasi media sosial, marketplace, dan
katalog digital berpotensi memperluas akses informasi produk warga binaan dibandingkan mekanisme
promosi konvensional. Temuan tersebut menunjukkan bahwa pemasaran digital tidak hanya berfungsi
sebagai me dia promosi, tetapi juga sebagai sarana distribusi informasi yang lebih terstruktur dan
mudah diakses. Selain itu, evaluasi menunjukkan bahwa integrasi antara sistem informasi dan
pemasaran digital memungkinkan proses pemasaran berjalan secara lebih terstr uktur, terdokumentasi,
dan mudah dimonitor dalam lingkungan pemasyarakatan. Meskipun demikian, implementasi model
tetap memerlukan mekanisme pengawasan institusional yang konsisten. Aktivitas publikasi produk,
komunikasi pelanggan, dan pengelolaan transaks i tetap harus berada dalam koordinasi petugas
pembinaan dan pengelola kegiatan kerja. Temuan ini memperlihatkan bahwa keberhasilan digitalisasi
pemasaran pada lingkungan pemasyarakatan tidak hanya ditentukan oleh kemampuan teknologi,
tetapi juga oleh kemampuan organisasi dalam menjaga mekanisme monitoring, validasi aktivitas, dan
kontrol akses digital secara berkelanjutan.  Secara umum, hasil evaluasi dan validasi menunjukkan
bahwa model  yang dikembangkan memiliki kesesuaian konseptua l dengan kebutuhan tata kelola
pemasaran digital di lingkungan pemasyarakatan, khususnya  dalam mendukung integrasi pengelolaan
produk, transaksi, dokumentasi aktivitas, dan pengawasan institusional terintegrasi.

4.4 Diskusi
Hasil penelitian menunjukkan bahwa digitalisasi pemasaran pada lingkungan pemasyarakatan
tidak dapat dipahami hanya sebagai upaya perluasan promosi dan penjualan produk secara digital.
Pada konteks ini, sistem digital juga berfungsi sebagai mekanisme koordinasi, dokumentasi aktivitas,
dan pengawasan institusional. Temuan tersebut memperlihatkan bahwa kebutuhan utama lingkungan
pemasyarakatan tidak hanya berkaitan dengan efektivitas pemasaran, tetapi juga dengan kemampuan
sistem menjaga kontrol aktivitas digital dalam lingkungan dengan pembatasan akses yang tinggi.
Temuan penelitian memperluas perspektif pemasaran digital  yang selama ini lebih banyak
dikembangkan pada konteks retail digital, e-commerce, dan organisasi bisnis terbuka yang
menekankan fleksibilitas interaksi pengguna dan efisiensi transaksi digital [3], [18], [19]. Pada

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2325

organisasi bisnis umum, keberhasilan pemasaran digital  umumnya diukur melalui peningkatan
interaksi pelanggan, perluasan pasar, dan efektivitas promosi digital. Namun, hasil penelitian ini
menunjukkan bahwa pendekatan tersebut tidak sepenuhnya sesuai diterapkan pada organis asi dengan
mekanisme kontrol institusional yang kuat seperti lingkungan pemasyarakatan.
Dalam lingkungan pemasyarakatan, aktivitas publikasi produk, komunikasi pelanggan, transaksi
penjualan, dan distribusi informasi digital tetap berada dalam koordinasi petugas pembinaan dan
pengelola kegiatan kerja. Karena itu, efektivitas pemasaran digital tidak hanya ber gantung pada
kemampuan sistem memperluas akses pasar, tetapi juga pada kemampuan sistem menjaga
akuntabilitas aktivitas digital dan konsistensi pengawasan institusional . Temuan ini menunjukkan
bahwa pemasaran digital  pada restricted digital environment memerlukan tata kelola yang berbeda
dibandingkan platform digital konvensional yang berasumsi pada keterbukaan interaksi digital [6].
Berbeda dengan penelitian pemasaran digital pada UMKM dan e-commerce yang berfokus pada
peningkatan visibilitas produk, customer engagement , dan efisiensi transaksi [3], [5], model yang
dikembangkan dalam penelitian ini menambahkan dimensi tata kelola dan pengawasan institusional
sebagai komponen inti sistem. Keunggulan utama model terletak pada integras i antara aktivitas
pemasaran digital dan mekanisme kontrol organisasi melalui governance and monitoring layer .
Integrasi tersebut penting karena lingkungan pemasyarakatan memiliki karakteristik organisasi
dengan pembatasan akses digital yang tinggi sehing ga pendekatan pemasaran digital konvensional
tidak dapat diterapkan secara langsung.
Temuan penelitian menunjukkan bahwa kendala utama digitalisasi pemasaran pada lingkungan
pemasyarakatan bukan terletak pada ketiadaan media promosi digital, melainkan pada  belum adanya
mekanisme yang mampu mengintegrasikan aktivitas promosi, transaksi, dan pengawasan institusional
dalam satu alur yang terkoordinasi. Pada organisasi bisnis umum, media sosial dan marketplace dapat
digunakan secara langsung karena pengguna mem iliki keleluasaan berinteraksi dengan pelanggan dan
mengelola aktivitas digital secara mandiri. Sebaliknya, pada lingkungan pemasyarakatan, seluruh
aktivitas digital harus melalui proses validasi, monitoring, dan pengawasan institusional. Oleh karena
itu, pendekatan pemasaran digital yang hanya berfokus pada peningkatan visibilitas produk menjadi
kurang memadai karena tidak mampu mengakomodasi kebutuhan kontrol institusional yang menjadi
karakteristik utama organisasi pemasyarakatan. Temuan ini menunjukkan bahwa keberhasilan
digitalisasi pemasaran pada organisasi dengan pembatasan akses tinggi tidak hanya ditentukan oleh
adopsi teknologi, tetapi juga oleh kemampuan sistem mengintegrasikan fungsi pemasaran dan tata
kelola secara simultan.
Hasil penelitian memperlihatkan bahwa penggunaan media sosial, marketplace, dan layanan
komunikasi digital memiliki peran penting dalam memperluas akses informasi produk warga binaan.
Namun, penelitian ini menunjukkan bahwa integrasi platform digital saja tidak cukup untuk
mendukung keberlanjutan pemasaran pada lingkungan pemasyarakatan. Sistem tetap memerlukan
mekanisme validasi publikasi produk, monitoring transaksi, dan pengawasan digital agar seluruh
proses pemasaran tetap berada dalam mekansime tata ke lola pemasyarakatan. Temuan tersebut
memperkuat pandangan bahwa transformasi digital organisasi tidak hanya berkaitan dengan adopsi
teknologi, tetapi juga berkaitan dengan kemampuan organisasi membangun mekanisme koordinasi
dan kontrol aktivitas digital se cara konsisten [20]. Selain itu, penelitian ini menunjukkan bahwa
pendekatan low-cost digital architecture memiliki relevansi penting pada organisasi dengan
keterbatasan sumber daya teknologi. Model dikembangkan dengan memanfaatkan platform digital
yang telah tersedia tanp a memerlukan pengembangan aplikasi yang kompleks. Pendekatan tersebut
memungkinkan organisasi melakukan digitalisasi pemasaran secara lebih realistis dan bertahap sesuai
kapasitas institusi. Temuan ini memperlihatkan bahwa keberhasilan transformasi digital  tidak selalu
ditentukan oleh kompleksitas teknologi, tetapi oleh kemampuan organisasi membangun koordinasi
pemasaran digital dan pengawasan institusional secara konsisten.
Dari sisi konseptual dan teoretis, penelitian ini memperluas literatur digital mark eting dan digital
governance dengan menunjukkan bahwa keberhasilan pemasaran digital pada organisasi dengan
pembatasan akses tinggi tidak hanya dipengaruhi oleh aspek promosi dan pemanfaatan teknologi
digital, tetapi juga oleh mekanisme tata kelola yang me ngatur validasi aktivitas, kontrol akses,
monitoring, dan akuntabilitas digital. Berbeda dengan penelitian sebelumnya yang umumnya
menempatkan pemasaran digital sebagai instrumen peningkatan penjualan dan customer engagement,
penelitian ini menunjukkan bah wa pada organisasi dengan tingkat regulasi dan pengawasan yang

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2326

tinggi, pemasaran digital perlu diposisikan sebagai bagian dari mekanisme tata kelola organisasi.
Temuan ini memperkenalkan perspektif governance-oriented digital marketing  yang
mengintegrasikan fungsi promosi, transaksi, dokumentasi aktivitas, monitoring digital, dan kontrol
institusional dalam satu kerangka tata kelola terintegrasi. Dengan demikian, penelitian ini tidak hanya
menghasilkan model tata kelola pemasaran digital yang sesuai untuk l ingkungan pemasyarakatan,
tetapi juga menunjukkan bahwa tata kelola digital merupakan faktor yang sama pentingnya dengan
teknologi dan pemasaran dalam mendukung keberhasilan transformasi digital pada organisasi dengan
tingkat pembatasan akses yang tinggi.

5 Kesimpulan
Penelitian ini menghasilkan model tata kelola pemasaran digital terintegrasi bagi produk warga
binaan pada lingkungan pemasyarakatan yang menghubungkan pengelolaan produk, promosi digital,
transaksi penjualan, pelaporan aktivitas, monitoring di gital, dan pengawasan institusional dalam satu
mekanisme tata kelola sistem digital terintegrasi. Hasil penelitian menujukkan bahwa digitalisasi
pemasaran pada lingkungan pemasyarakatan tidak hanya berkaitan dengan efektivitas promosi dan
transaksi penjualan, tetapi juga berkaitan dengan kebutuhan validasi aktivitas, dokumentasi transaksi,
kontrol akses, dan monitoring aktivitas digital secara berkelanjutan. Penelitian ini juga memperluas
perspektif pemasaran digital  dari yang sebelumnya lebih berorientasi pada efektivitas pemasaran
menjadi tata kelola pemasaran digital yang terintegrasi dengan mekanisme pengawasan organisasi.
Penelitian ini masih terbatas pada pengembangan dan evaluasi model pada satu lingkungan
pemasyarakatan sehingga hasil penelitian bel um dapat digeneralisasi pada seluruh lingkungan
pemasyarakatan dengan karakteristik organisasi yang berbeda. Selain itu, penelitian belum mengukur
dampak implementasi sistem terhadap peningkatan penjualan produk warga binaan secara
longitudinal. Penelitian  selanjutnya dapat mengembangkan implementasi model pada berbagai
organisasi publik dengan tingkat pengawasan institusional yang tinggi serta mengevaluasi efektivitas
sistem terhadap keberlanjutan pemasaran digital, pengelolaan informasi, dan tata kelola a ktivitas
digital secara lebih luas.

Referensi
[1] D. Chaffey and F. Ellis -Chadwick, Digital Marketing: Strategy, Implementation and Practice,
Fifth Edit. Pearson Education Limited, 2012.
[2] Y. K. Dwivedi et al., “Artificial intelligence (AI): Multidisciplinary Perspectives on Emerging
Challenges, Opportunities, and Agenda for Research, Practice and Policy,” Int. J. Inf.
Manage., Vol. 57, p. 101994, 2021, DOI: 10.1016/j.ijinfomgt.2019.08.002.
[3] P. C. Verhoef et al. , “ Digital Transformation: A Multidisciplinary Reflection and Research
Agenda,” J. Bus. Res., Vol. 122, pp. 889–901, Jan. 2021, DOI: 10.1016/j.jbusres.2019.09.022.
[4] A. A. Alalwan, N. P. Rana, Y. K . Dwivedi, and R. Algharabat, “Social Media in Marketing: A
Review and Analysis of the Existing Literature ,” Telemat. Informatics , Vol. 34, No. 7, pp.
1177–1190, Nov. 2017, DOI: 10.1016/j.tele.2017.05.008.
[5] N. Fitriani, D. Setiawan, Y. A. Aryani, and T.  Arifin, “Does Social Media Affect Performance
in e-Commerce Business? The Role of Customer Management,” J. Open Innov. Technol. Mark.
Complex., Vol. 9, No. 4, p. 100171, Dec. 2023, DOI: 10.1016/j.joitmc.2023.100171.
[6] Y. S. Dwijayanti and I. Sulhin, “Sistem Informasi Pemasyarakatan : Urgensi dan Tantangan
Pengembangan (Dalam Perspektif Teori Transisi Ruang ),” J. Correct. Issues , Vol. 2, No. 1,
pp. 1–12, 2019, DOI: 10.52472/jci.v2i1.19.
[7] I. N. T. W. R. Meranggi and J. P. Lukman, “Transformasi Digital Layanan Pemasyarakatan di
Kantor Wilayah Kementerian Hukum dan Hak Asasi Manusia (Kemenkumham) Bali,” Socio-
political Commun. Policy Rev., Vol. 1, No. 4, pp. 89–95, 2024, DOI: 10.61292/shkr.139.
[8] N. Bagherifam, S. Naghdi , V. Ahmadian, A. Fazlzadeh, and M. Baghalzadeh
Shishehgarkhaneh, “ Digital Regulatory Governance : The Role of RegTech and SupTech in
Transforming Financial Oversight and Administrative Capacity ,” Int. J. Financ. Stud. , Vol.
13, No. 4, p. 217, Nov. 2025, DOI: 10.3390/ijfs13040217.
[9] C. Haney, “ The Psychological Effects of Imprisonment ,” Prison. Prison. , 2018, DOI:
10.1093/oxfordhb/9780199730148.013.0024.

Sistemasi: Jurnal Sistem Informasi                                     ISSN:2302-8149
Volume 15, Nomor 6, 2026: 2316-2327                         e-ISSN:2540-9719

http://sistemasi.ftik.unisi.ac.id

2327

[10] M.-L. Martín -Peña, P. C. Lorenzo, and N. Meyer, “ Digital Platforms and Business
Ecosystems: A Multidisciplinary Approach for New and Sustainable Business Models ,” Rev.
Manag. SCI., Vol. 18, No. 9, pp. 2465–2482, Sep. 2024, DOI: 10.1007/s11846-024-00772-y.
[11] G. Natalie and E. Maria, “ Analysis of User Satisfaction of Mysooltan Application as Single
Digital Touch using Pieces Framework,” JURTEKSI (Jurnal Teknol. dan Sist. Informasi), Vol.
IX, No. 2, pp. 319–328, 2023, DOI: 10.33330/JURTEKSI.V9I2.2020.
[12] P. Y. Adhiatma and S. M. Mahmudah, “Optimalisasi Integrasi Media Sosial Direktorat
Jenderal Pemasyarakatan sebagai Bentuk Keterbukaan Informasi Publik ,” J. Pustaka Komun.,
Vol. 6, No. 2, pp. 232–246, 2023, DOI: 10.32509/pustakom.v6i2.2648.
[13] S. V. Scott and W. J. Orlikowski, “ Reconfiguring Relations of Accountability: Materialization
of Social Media in the Travel Sector,” Accounting, Organ. Soc., Vol. 37, No. 1, pp. 26–40, Jan.
2012, DOI: 10.1016/j.aos.2011.11.005.
[14] A. Tiwana, B. Konsynski, and A. A. Bush, “ Research Commentary: Platform Evolution :
Coevolution of Platform Architecture, Governance, and Environmental Dynamics,” Inf. Syst.
Res., Vol. 21, No. 4, p. . 675 -687, 2010, [Online]. Available:
https://www.jstor.org/stable/23015636
[15] R. L. Baskerville, M. D. Myers, and Y. Yoo, “ Digital First: The Ontological Reversal  and
New Challenges for Information Systems Research,” MIS Q., Vol. 44, No. 2, pp. 509–524, Jun.
2020, DOI: 10.25300/MISQ/2020/14418.
[16] S. Gregor and A. R. Hevner, “ Positioning and Presenting Design Science Research for
Maximum Impact ,” MIS Q. , Vol. 37,  No. 2, pp. 337 –355, Jun. 2013, DOI:
10.25300/MISQ/2013/37.2.01.
[17] K. Peffers, T. Tuunanen, M. A. Rothenberger, and S. Chatterjee, “ A Design Science Research
Methodology for Information Systems Research,” J. Manag. Inf. Syst. , Vol. 24, No. 3, pp. 45–
77, 2007, DOI: 10.2753/MIS0742-1222240302.
[18] R. Cuel, F. Ceci, I. Pappas, and P. K. Senyo, “ Transformation and Sustainability of Digital
Platforms and Ecosystems: A Multidisciplinary Exploration,” Int. J. Electron. Commer. , Vol.
28, No. 2, pp. 148–155, Apr. 2024, DOI: 10.1080/10864415.2024.2332045.
[19] H.-T. Liao, C. -L. Pan, and Z. Wu, “ Digital Transformation and Innovation and Business
Ecosystems: A Bibliometric Analysis for Conceptual Insights and Collaborative Practices for
Ecosystem Innovation ,” Int. J. Innov. Stud. , Vol. 8, No. 4, pp. 406 –431, Dec. 2024, DOI:
10.1016/j.ijis.2024.04.003.
[20] L. F. Luna -Reyes and J. R. Gil -Garcia, “ Digital Government Transformation and Internet
Portals: The Co-Evolution of Technology, Organizations, and Institutions,” Gov. Inf. Q., Vol.
31, No. 4, pp. 545–555, Oct. 2014, DOI: 10.1016/j.giq.2014.08.001.
