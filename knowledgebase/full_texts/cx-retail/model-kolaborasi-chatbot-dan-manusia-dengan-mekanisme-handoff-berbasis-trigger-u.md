---
title: Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff berbasis Trigger untuk Optimalisasi
  Layanan Pelanggan UMKM di Era Digital
url: https://doi.org/10.35315/dinamik.v31i2.10398
category: cx-retail
subcategory: framework
date: 2026-07
venue: Dinamik
authors:
- Dimas Adi Wicaksono
- Heru Yulianto
- Aji Priyambodo
source: openalex-oa
pdf_url: https://www.unisbank.ac.id/ojs/index.php/fti1/article/download/10398/4431
pages: 11
chars: 44924
fetched_at: '2026-11-08T18:11:13+00:00'
kb_version: 1
---

# Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff berbasis Trigger untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  389
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
MODEL KOLABORASI CHATBOT DAN MANUSIA DENGAN MEKANISME HANDOFF BERBASIS
TRIGGER UNTUK OPTIMALISASI LAYANAN PELANGGAN UMKM DI ERA DIGITAL
Dimas Adi Wicaksono1, Heru Yulianto2, Aji Priyambodo3
1,2,3Institut Teknologi dan Bisnis Semarang
e-mail: 1priyambodo@itbsemarang.ac.id

ABSTRAK
Perkembangan teknologi kecerdasan buatan (AI) telah mengubah paradigma layanan pelanggan
dengan menghadirkan Chatbot sebagai solusi untuk meningkatkan efisiensi dan ketersediaan layanan.
Namun, pada konteks usaha mikro, kecil , dan menengah (UMKM), keterbatasan sumber daya dan
kompleksitas interaksi pelanggan memerlukan pendekatan hybrid yang mengintegrasikan Chatbot
dengan agen manusia. Penelitian ini merancang model kolaborasi Chatbot dan manusia dengan
mekanisme handoff berbasis trigger yang memungkinkan transisi otomatis berdasarkan indikator
terukur, seperti sentimen negatif, pertanyaan kompleks, dan permintaan eksplisit pelanggan. Dengan
pendekatan simulasi pada 5.000 percakapan pelanggan, penelitian ini menemukan bahwa model hybrid
mampu meningkatkan Customer Satisfaction Score  (CSAT) dari 3.6 menjadi 4.2, mengurangi waktu
penyelesaian dari 6.2 menit menjadi 3.8 menit, serta meningkatkan loyalitas pelanggan dari 52%
menjadi 68%. Roadmap implementasi disusun dalam tiga tingkat (pemula, menengah, mahir) agar
sesuai dengan variasi kapabilitas digital UMKM. Penelitian ini berkontribusi pada literatur human
dan AI collaboration  dan omnichannel customer experience , serta menawarkan kerangka kerja
aplikatif bagi UMKM dalam mempercepat transformasi digital layanan pelanggan.
Kata Kunci: Chatbot, Human and AI Collaboration, Customer Experience, Handoff, UMKM
ABSTRACT
The rapid advancement of Artificial Intelligence (AI) has transformed the customer service
paradigm by introducing chatbots as an effective solution for improving service efficiency and
availability. However, in the context of Micro, Small, and Medium Ente rprises (MSMEs), limited
resources and the complexity of customer interactions necessitate a hybrid approach that integrates
chatbots with human agents. This study proposes a collaborative human–chatbot model incorporating
a trigger-based handoff mechanism  that enables seamless transitions from chatbot to human agents
based on measurable indicators, including negative sentiment, complex inquiries, and explicit customer
requests. Using a simulation of 5,000 customer conversations, the findings demonstrate th at the
proposed hybrid model improves the Customer Satisfaction Score (CSAT) from 3.6 to 4.2, reduces the
average resolution time from 6.2 minutes to 3.8 minutes, and increases customer loyalty from 52% to
68%. Furthermore, a three -level implementation roadmap (beginner, intermediate, and advanced) is
developed to accommodate the varying digital capabilities of MSMEs. This study contributes to the
literature on human –AI collaboration and omnichannel customer experience while providing a
practical framework to support MSMEs in accelerating their digital transformation in customer service.
Keywords: Chatbot, Human –AI Collaboration, Customer Experience, Handoff, Micro, Small, and
Medium Enterprises (MSMEs)
1. PENDAHULUAN
Perkembangan teknologi digital dan kecerdasan buatan telah mengubah ekspektasi konsumen
terhadap layanan: kini pelanggan menuntut pengalaman yang cepat, konsisten, dan personal di seluruh
jalur interaksi antara kanal daring dan luring [1]. Laporan industri dan kajian akademik menegaskan
bahwa konsumen menghargai pengalaman terhubung ( connected experience) dan menaruh perhatian
besar pada transparansi serta kepercayaan ketika AI digunakan dalam layanan pelanggan. Hal ini
menjadikan omnichannel customer experience  (OCX) bukan sekadar pilihan strategis, melainkan
elemen inti dalam mempertahankan kepuasan serta loyalitas pelanggan [1], [2].
Di sisi praktik, UMKM menghadapi tekanan ganda: kebutuhan untuk mengadopsi omnichannel
demi menjangkau pelanggan sekaligus keterbatasan sumber daya manusia, modal, dan literasi digital
yang membatasi kemampuan mereka dalam menerapkan solusi teknologi kompleks [3], [4]. Kajian
sistematis mengenai transformasi digital UMKM di Indonesia menunjukkan hambatan struktural dan

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  390
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
operasional ini, sehingga solusi teknologi harus dirancang berlapis dan kontekstual agar dapat diadopsi
secara luas di sektor tersebut [3], [4]. Dengan demikian, UMKM membutuhkan model yang ringan,
murah, dan mudah dioperasikan, berbeda dengan korporasi besar yang memiliki sumber daya melimpah
[5]. Chatbot dan agen konversasional berbasis AI muncul sebagai solusi efisiensi untuk menangani
pertanyaan rutin dan mengotomasi proses layanan berulang. Teknologi ini memungkinkan layanan
24/7, konsistensi interaksi, dan pengurangan beban tenaga manusia [6], [7]. Namun literatur teknik dan
tinjauan tentang human in the loop  (HITL) menegaskan bahwa desain interaksi antara manusia dan
mesin memerlukan mekanisme kolaborasi yang eksplisit  mulai dari active learning hingga transfer
konteks antar aktor  untuk menjaga kegunaan, akurasi, dan keterterimaan pengguna [8],[[9]. Tanpa
mekanisme demikian, Chatbot sering kali gagal pada kasus kompleks yang membutuhkan penilaian
kontekstual dan empati manusia [10],[11].
Penelitian eksperimen dan tinjauan meta analisis juga menunjukkan bahwa penggabungan
manusia dan AI tidak otomatis menghasilkan sinergi yang lebih baik dibandingkan penggunaan salah
satu pihak saja. Hasil kolaborasi cenderung bergantung pada tipe tugas (kr eatif vs keputusan), desain
pembagian kerja, serta mekanisme umpan balik dan transparansi [12],[13]. Temuan ini menegaskan
perlunya merancang model kolaborasi yang mempertimbangkan karakteristik tugas serta performa
relatif manusia dan AI, sehingga pendelegasian peran dapat berbasis bukti [14].
Selain aspek kinerja, faktor komunikasi dan disclosure berperan penting. Penelitian terbaru
menemukan bahwa ketika pengguna diinformasikan bahwa interaksi melibatkan keterlibatan manusia,
gaya komunikasi mereka berubah menuju pendekatan yang lebih manusiawi [9]. Fenomena ini dapat
memperbaiki kualitas percakapan namun juga meningkatkan beban eskalasi bagi agen manusia.
Penelitian lapangan eksperimental mengenai efek human disclosure mengindikasikan adanya trade off
antara transparansi dan kebutuhan kapasitas layanan, sehingga mekanisme handoff (aturan trigger,
ringkasan konteks, SLA eskalasi) menjadi elemen operasional krusial yang harus didesain dengan
cermat [9],[15].
Dalam perspektif omnichannel, tinjauan literatur terkini menyoroti pentingnya pengelolaan
konteks pelanggan dan integrasi data antar kanal sebagai fondasi evaluasi pengalaman pelanggan
(seamlessness, reliability, responsiveness)  [2],[16],[17]. Kerangka konseptual omnichannel
menempatkan pelanggan di pusat integrasi kanal, tetapi penelitian yang menghubungkan desain teknis
handoff Chatbot dan manusia dengan metrik CX, khususnya dalam konteks UMKM, masih terbatas
[3],[[4]. Studi aplikatif di area ritel dan keuangan memperlihatkan potensi efisiensi besar dari Chatbot
generatif pada skala perusahaan, namun juga memunculkan bukti empiris tentang kegagalan layanan
dan resistensi konsumen terhadap otomatisasi bila desain pengalaman buruk [10],[18]. Konteks UMKM
menuntut adaptasi praktik ini ke dalam bentuk yang sesuai dengan keterbatasan mereka [4], [5].
Berangkat dari landasan teoretis dan temuan empiris tersebut, penelitian ini memfokuskan pada
tiga kontribusi utama. Pertama, identifikasi taksonomi tugas layanan pelanggan sehingga keputusan
delegasi ( Chatbot vs manusia) dapat berbasis bukti. Kedua, perancangan mekanisme handoff yang
memastikan transfer konteks tanpa mengorbankan pengalaman pengguna. Ketiga, penyusunan roadmap
implementasi bertingkat yang sesuai dengan variasi tingkat kematangan digital UMKM. Rancangan ini
diharapkan tidak hanya menambah pemahaman teoretis dalam literatur human dan AI collaboration
dan omnichannel CX, tetapi juga menghasilkan artefak praktis yang dapat diadopsi oleh UMKM dengan
sumber daya terbatas.
Konteks Indonesia, khususnya ekosistem UMKM di kota menengah seperti Semarang,
menyediakan setting empiris yang relevan untuk mengeksplorasi feasibility dan dampak kebijakan
operasional ini. Dengan demikian, hipotesis utama penelitian ini adalah bahwa model kolaborasi
Chatbot dan tenaga penjualan manusia yang didesain khusus untuk konteks UMKM akan meningkatkan
indikator pengalaman pelanggan omnichannel (misalnya CSAT, first contact resolution , waktu
penyelesaian) dibandingkan praktik ad hoc tanpa aturan delegasi dan handoff yang jelas. Jika terbukti,
temuan ini akan memberi kontribusi signifikan bagi teori kolaborasi manusia dan AI sekaligus
menyediakan panduan implementasi praktis yang dapat membantu UMKM mempercepat transformasi
digital mereka secara bertanggung jawab dan berkelanjutan.

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  391
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
2. TINJAUAN PUSTAKA
Konsep omnichannel customer experience (OCX) telah menjadi pusat perhatian dalam literatur
pemasaran dan sistem informasi dalam tiga tahun terakhir. OCX menekankan pentingnya memberikan
pengalaman yang konsisten dan mulus di berbagai kanal layanan pelanggan, baik daring maupun luring
[1]. Integrasi kanal tidak hanya menambah kenyamanan bagi pelanggan, tetapi juga memperkuat
loyalitas dan mendorong peningkatan nilai seumur hidup pelanggan (customer lifetime value) [2], [16].
Penelitian menunjukkan bahwa seamlessness, reliability, dan responsiveness adalah determinan utama
keberhasilan OCX, terutama ketika pelanggan berpindah antar kanal [17]. Studi empiris pada sektor
ritel menemukan bahwa integrasi informasi lintas kanal meminimalkan friksi layanan dan
meningkatkan persepsi profesionalisme perusahaan [18].
Dalam konteks teknologi layanan, Chatbot telah menjadi salah satu inovasi yang paling banyak
diadopsi untuk mendukung strategi omnichannel. Chatbot memungkinkan organisasi untuk menangani
volume interaksi tinggi dengan biaya rendah, memberikan jawaban cepat terhadap pertanyaan rutin,
serta mendukung layanan 24/7 [6], [7]. Namun, literatur menekankan keterbatasan Chatbot dalam
menangani tugas yang bersifat kompleks, kontekstual, atau emosional [10], [11]. Oleh karena itu, riset
mengenai human in the loop  (HITL) menjadi relevan untuk menjembatani kesenjangan kemampuan
Chatbot dengan kebutuhan pelanggan [8].
Kajian sistematis menunjukkan bahwa kolaborasi manusia dan AI menghasilkan performa
terbaik ketika peran keduanya jelas dibedakan berdasarkan kompleksitas tugas [12]. Dalam hal ini,
Chatbot berperan pada interaksi sederhana seperti pengecekan status transaksi atau FAQ, sedangkan
agen manusia mengambil alih kasus yang membutuhkan empati, interpretasi, atau pengambilan
keputusan berbasis konteks [9]. Penelitian meta terbaru menegaskan bahwa tanpa mekanisme
pembagian kerja yang eksplisit, kombinasi manusia dan AI tidak selalu menghasilkan sinergi yang
diharapkan [12],[[13].
Lebih lanjut, penelitian mengenai human disclosure menunjukkan bahwa komunikasi pengguna
dipengaruhi oleh persepsi keterlibatan manusia dalam interaksi. Ketika pengguna diberi tahu bahwa ada
manusia yang ikut terlibat, mereka cenderung lebih terbuka, tetapi hal ini juga meningkatkan beban
eskalasi bagi ag en manusia [9], [15]. Dengan demikian, diperlukan handoff mechanism yang jelas,
yakni seperangkat aturan atau trigger yang memutuskan kapan Chatbot harus menyerahkan percakapan
kepada manusia [14], [11]. Literatur tentang handover di bidang robotika bahkan memberikan inspirasi
dalam hal desain transisi yang mulus, dengan mengukur kecepatan, kenyamanan, dan ketepatan sebagai
indikator utama [14]. Prinsip ini dapat diadaptasi untuk layanan digital, di mana transisi percakapan
yang mulus memastikan pelanggan tidak kehilangan konteks interaksi.
Khusus pada UMKM, adopsi Chatbot dan omnichannel CX menghadapi kendala tambahan
berupa keterbatasan infrastruktur, literasi digital yang rendah, serta alokasi anggaran yang minim [3],
[4], [5]. Penelitian di Indonesia menunjukkan bahwa tingkat kapabilitas digital UMKM sangat
bervariasi, dari yang baru menggunakan media sosial hingga yang sudah memanfaatkan marketplace
atau ERP sederhana [4]. Oleh karena itu, literatur menekankan perlunya roadmap implementasi
bertingkat, sehingga UMKM dapat mengadopsi teknologi secara bertahap tanpa menimbulkan disrupsi
berlebihan [3].
Secara keseluruhan, tinjauan pustaka ini memperlihatkan adanya gap penelitian: meskipun
banyak studi membahas Chatbot, omnichannel, dan human dan AI collaboration secara terpisah, kajian
yang mengintegrasikan ketiganya dalam konteks UMKM masih jarang. Terutama, mekanisme handoff
Chatbot dan manusia dalam lingkungan omnichannel UMKM belum banyak diuji secara empiris.
Dengan mengisi celah ini, penelitian ini tidak hanya memperkuat teori kolaborasi manusia dan AI, tetapi
juga menyediakan artefak praktis berupa model implementasi yang adaptif terhadap keterbatasan
UMKM di Indonesia.
3. METODE PENELITIAN
Metodologi penelitian ini dirancang untuk memberikan gambaran yang jelas dan rinci mengenai
langkah-langkah penelitian sehingga dapat direplikasi oleh peneliti independen. Desain penelitian
mengadopsi pendekatan mixed method dengan alasan bahwa penelitian mengenai kolaborasi Chatbot
dan manusia tidak dapat dijelaskan hanya dengan data kuantitatif semata, tetapi juga membutuhkan
wawasan kualitatif dari pengalaman pengguna dan penyedia layanan. Pendekatan ini sesuai dengan

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  392
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
literatur terkini yang menekankan perlunya kombinasi metode untuk memahami fenomena human dan
AI collaboration secara lebih utuh.
3.1 Partisipan dan Populasi
Populasi penelitian mencakup Usaha Mikro, Kecil, dan Menengah (UMKM) di sektor ritel dan
jasa di Kota Semarang. Pemilihan lokasi didasarkan pada karakteristik kota menengah yang
menghadapi tekanan digitalisasi namun dengan heterogenitas tinggi dalam tingka t adopsi teknologi .
Semarang dipandang representatif untuk konteks Indonesia karena memiliki jumlah UMKM yang
signifikan, sekaligus menghadapi keterbatasan sumber daya yang serupa dengan kota menengah
lainnya.
Sampel penelitian terdiri dari 50 UMKM yang dipilih menggunakan metode purposive sampling.
Kriteria inklusi meliputi (1) memiliki kanal digital layanan pelanggan seperti WhatsApp Business ,
Instagram, atau marketplace; (2) aktif melayani lebih dari 100 interaksi pelanggan per bulan; dan (3)
bersedia mengikuti rangkaian penelitian. Strategi ini dipilih untuk memastikan bahwa UMKM yang
terlibat memiliki pengalaman nyata dalam mengelola interaksi pelanggan digital. Demografi UMKM
mencakup sektor kuliner (30%), fesyen (25%), kerajinan (20%), dan jasa pendidikan (25%). Penelitian
terdahulu menunjukkan bahwa variasi sektor memberikan peluang untuk melihat perbedaan pola
interaksi pelanggan yang relevan bagi desain sistem hybrid Chatbot dan manusia [10], [5].
3.2 Sumber Data dan Spesifikasi Alat Simulasi dan Analisis
Data yang digunakan dalam penelitian ini adalah hasil dari 5.000 percakapan pelanggan yang
dikumpulkan dari 50 UMKM yang terlibat. Percakapan ini dianalisis menggunakan teknik natural
language processing  (NLP) untuk mengidentifikasi berbagai kategori interaksi pelanggan, seperti
sederhana, menengah, dan kompleks. Simulasi numerik juga dilakukan untuk menguji dua kondisi,
yaitu model Chatbot Only dan model hybrid yang menggabungkan Chatbot dengan agen manusia. Alat
analisis yang digunakan mencakup perangkat berbasis AI yang dapat mengidentifikasi sentimen,
kompleksitas pertanyaan, dan permintaan eksplisit untuk berbicara dengan manusia sebagai indikator
trigger untuk eskalasi.
Spesifikasi alat yang digunakan dalam simulasi meliputi perangkat lunak analitik percakapan
berbasis NLP dan machine learning, yang memungkinkan untuk mendeteksi secara otomatis indikator
trigger yang relevan, seperti sentimen negatif, pertanyaan dengan lebih dari tiga kata kunci teknis, dan
permintaan eksplisit dari pelanggan. Alat ini memungkinkan simulasi terhadap ribuan interaksi
pelanggan untuk mengukur efektivitas model Chatbot Only dibandingkan dengan model hybrid.
3.2 Instrumen Penelitian
Instrumen penelitian dirancang dalam tiga kategori utama. Pertama, panduan wawancara semi
terstruktur digunakan untuk menggali pengalaman, hambatan, dan ekspektasi UMKM terhadap
penggunaan Chatbot. Panduan ini disusun berdasarkan literatur tentang transformasi digital UMKM
dan penelitian sejenis pada layanan Chatbot [6], [7]. Pertanyaan mencakup tema adopsi teknologi,
persepsi efektivitas Chatbot, serta preferensi terkait eskalasi ke agen manusia. Kedua, checklist
observasi interaksi disusun untuk mencatat pola percakapan antara pelanggan dengan Chatbot.
Checklist ini memuat indikator seperti jumlah interaksi, jenis pertanyaan, frekuensi eskalasi, waktu
yang dibutuhkan untuk penyelesaian, serta respon pelanggan terhadap transisi ke agen manusia.
Indikator ini diadaptasi dari penelitian tentang handoff mechanism yang menekankan pentingnya
mengukur sentimen, kompleksitas pertanyaan, dan permintaan eskalasi eksplisit [14], [11].
Ketiga, kuesioner Customer Satisfaction (CSAT) digunakan untuk mengukur kepuasan pelanggan
setelah interaksi dengan Chatbot maupun agen manusia. Kuesioner ini mengadopsi skala Likert 1 dan
5 dan telah divalidasi dalam penelitian tentang Chatbot pada sektor perbankan dan ritel [10], [15]. Selain
CSAT, kuesioner juga mencakup indikator loyalitas pelanggan (niat melakukan pembelian ulang) dan
first contact resolution (FCR). Kombinasi instrumen ini memungkinkan peneliti untuk menghubungkan
data kualitatif dengan indikator kuantitatif dalam mengevaluasi efektivitas model kolaborasi hybrid.
3.3 Prosedur Penelitian
Prosedur penelitian dibagi ke dalam empat tahap utama. Tahap pertama adalah pengumpulan data
percakapan pelanggan. Setiap UMKM diamati selama satu bulan dengan target 100 interaksi pelanggan.
Percakapan dicatat, dianonimkan, dan dikodekan menggunakan pendekatan grounded theory. Untuk

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  393
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
meningkatkan efisiensi, analisis awal dilakukan dengan bantuan large language model (LLM) sebagai
coding assistant, yang telah digunakan dalam penelitian kualitatif berbasis percakapan [19].
Tahap kedua adalah wawancara semi terstruktur dengan pemilik atau staf UMKM. Wawancara
berlangsung selama 45 dan 60 menit untuk menggali persepsi mereka tentang efektivitas Chatbot,
kendala implementasi, serta ekspektasi terhadap mekanisme handoff. Pendekatan ini sejalan dengan
metode yang direkomendasikan dalam literatur transformasi digital UMKM, di mana wawancara
digunakan untuk mengeksplorasi faktor manusia dan organisasi [3], [4]. Tahap ketiga adalah simulasi
numerik. Dari data percakapan, ditentukan indikator trigger untuk handoff: (1) sentimen negatif dengan
skor <40%, (2) pertanyaan kompleks dengan ≥3 keyword teknis, dan (3) permintaan eksplisit pelanggan
untuk berbicara dengan manusia [14], [11]. Simulasi 100 percakapan dilakukan pada setiap UMKM
untuk membandingkan performa Chatbot only dengan model hybrid Chatbot dan manusia. Tahap
keempat adalah evaluasi indikator CX. Percakapan dinilai menggunakan metrik CSAT, waktu
penyelesaian, tingkat eskalasi, dan loyalitas pelanggan. Penilaian ini mengikuti kerangka yang banyak
digunakan dalam penelitian omnichannel customer experience [1], [16], [18].
3.4 Teknik Analisis
Data kualitatif dari wawancara dianalisis menggunakan thematic analysis . Proses analisis
melibatkan tiga peneliti independen yang melakukan open coding secara terpisah, kemudian hasilnya
dibandingkan untuk mengukur reliabilitas. Nilai Cohen’s Kappa  digunakan sebagai indikator
reliabilitas, dengan target >0.7 sebagaimana standar penelitian kualitatif [19]. Data kuantitatif dianalisis
melalui statistik deskriptif dan uji inferensial. Pertama, dihitung rerata CSAT, waktu penyelesaian, dan
tingkat eskalasi untuk model Chatbot only dan hybrid. Kedua, dilakukan uji t berpasangan untuk
membandingkan perbedaan performa antar kondisi [12]. Selain itu, analisis trade off dilakukan dengan
menghitung beban kerja staf manusia berdasarkan jumlah percakapan yang dialihkan dan estimasi
waktu yang dibutuhkan. Analisis ini memberikan gambaran mengenai implikasi biaya operasional yang
sering menjadi pertimbangan utama bagi UMKM.
3.5 Validitas dan Reliabilitas
Validitas instrumen wawancara dan kuesioner diperoleh melalui expert judgment dari dua pakar
bidang sistem informasi dan manajemen UMKM. Proses validasi dilakukan dengan mengevaluasi
kejelasan pertanyaan, relevansi indikator, dan kesesuaian dengan tujuan penelitian. Untuk memastikan
validitas eksternal, penelitian ini mencakup UMKM dari berbagai sektor (kuliner, fesyen, kerajinan,
jasa) sehingga hasil dapat digeneralisasi pada konteks yang lebih luas. Reliabilitas data percakapan diuji
dengan inter coder reliability  pada proses analisis kualitatif. Tiga peneliti independen melakukan
coding terhadap 20% sampel data. Hasil menunjukkan nilai Cohen’s Kappa >0.7, yang menandakan
konsistensi interpretasi antar peneliti. Reliabilitas instrumen kuantitatif diuji menggunakan Cronbach’s
Alpha, dengan nilai α >0.8 pada kuesioner CSAT. Temuan ini menunjukkan bahwa instrumen memiliki
konsistensi internal yang tinggi.
3.6 Etika Penelitian
Aspek etika dijaga melalui proses informed consent . Semua UMKM diberikan penjelasan
mengenai tujuan penelitian, metode pengumpulan data, dan cara data digunakan. Percakapan pelanggan
dianonimkan sehingga tidak dapat ditelusuri kembali ke individu tertentu, sejalan dengan praktik
perlindungan data dalam riset layanan digital. Selain itu, peneliti menekankan prinsip do no harm
dengan meminimalkan risiko pada UMKM. Implementasi simulasi dilakukan tanpa mengganggu
operasi bisnis sehari hari. UMKM juga diberikan umpan balik berupa laporan hasil evaluasi Chatbot
mereka, sehingga mereka memperoleh manfaat praktis dari partisipasi dalam penelitian ini. Etika
penelitian ini selaras dengan pedoman penelitian internasional di bidang layanan pelanggan berbasis AI
[13].
4. HASIL DAN PEMBAHASAN
4.1 Hasil
4.1.1 Taksonomi Tugas Layanan Pelanggan
Analisis distribusi interaksi pelanggan pada 50 UMKM memperlihatkan bahwa Chatbot
menangani sebagian besar interaksi sederhana. Dari 5.000 percakapan yang dianalisis (rata rata 100
percakapan per UMKM), sebanyak 2.750 percakapan (55%) termasuk kategori sederhana, 1.500

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  394
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
percakapan (30%) kategori menengah, dan 750 percakapan (15%) kategori kompleks. Chatbot mampu
menyelesaikan 95% interaksi sederhana, tetapi hanya 40% dari interaksi menengah, dan praktis gagal
pada interaksi kompleks yang selalu dialihkan ke manusia. Temuan ini menunjukkan bahwa Chatbot
paling efektif pada domain layanan berulang, sedangkan peran manusia tetap kritis pada domain
kompleks. Perbedaan proporsi ini konsisten dengan teori task dan technology fit  yang menyatakan
bahwa efektivitas sistem dipengaruhi oleh kesesuaian antara karakteristik tugas dan kapabilitas
teknologi, seperti nampak pada tabel 1 berikut:
Tabel 1. Simulasi Distribusi Tugas Layanan pada 5.000 Percakapan
Kategori
Tugas
Jumlah
Percakapan Proporsi (%) Diselesaikan Chatbot (%) Dialihkan ke Manusia (%)
Sederhana 2.750 55 95 5
Menengah 1.500 30 40 60
Kompleks 750 15 0 100
Total 5.000 100
4.1.2 Mekanisme Handoff Berbasis Trigger
Hasil simulasi mekanisme handoff seperti nampak pada tabel 2 menunjukkan bahwa 2.000 dari
5.000 percakapan (40%) berakhir dengan eskalasi ke manusia. Dari jumlah tersebut, penyebab utama
adalah sentimen negatif (50% dari seluruh eskalasi), diikuti pertanyaan kompleks (30%), dan
permintaan eksplisit pelanggan (20%). Simulasi ini memperlihatkan bahwa indikator trigger berfungsi
sebagai filter efektif untuk menentukan kapan Chatbot harus menyerahkan percakapan. Jika tanpa
mekanisme trigger, Chatbot akan mencoba menyelesaikan semua kasus, yang dalam uji awal
menghasilkan tingkat CSAT hanya 3.6. Dengan trigger handoff, CSAT meningkat ke 4.2, menunjukkan
bahwa transisi tepat waktu ke agen manusia meningkatkan pengalaman pelanggan.
Tabel 2. Simulasi Distribusi Trigger Handoff (n=2.000 percakapan)
Indikator Trigger Ambang Batas Jumlah Kasus Persentase dari Eskalasi (%)
Sentimen negatif Skor < 40% 1.000 50
Pertanyaan kompleks ≥3 keyword teknis 600 30
Permintaan eksplisit “Ingin bicara dengan CS” 400 20
Total Eskalasi  2.000 100
4.1.3 Evaluasi Indikator Customer Experience (CX)
Pengukuran terhadap empat indikator CX seperti nampak pada gambar 1 memperlihatkan
perbaikan signifikan ketika UMKM menggunakan model hybrid dibanding layanan manual penuh.
Simulasi pada 5.000 percakapan memperlihatkan rata rata CSAT meningkat dari 3.6 menjadi 4.2, waktu
penyelesaian berkurang dari 6.2 menit menjadi 3.8 menit, tingkat eskalasi terkendali di 40%, dan
loyalitas pelanggan meningkat dari 52% menjadi 68%. Analisis ini menegaskan bahwa hybrid model
tidak hanya memberikan efisiensi operasional, tetapi juga meningkatkan kualitas pengalaman
pelanggan. Peningkatan CSAT lebih dari 15% dan loyalitas pelanggan hampir 20% mengindikasikan
adanya hubungan positif antara desain layanan hybrid dan retensi pelanggan.

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  395
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital

Gambar 1. Perbandingan model Chatbot dan hybrid
4.1.4 Roadmap Implementasi UMKM
Hasil penelitian juga menghasilkan roadmap implementasi berbasis kapabilitas digital UMKM.
Simulasi menunjukkan bahwa 60% UMKM berada pada tingkat pemula, 30% pada tingkat menengah,
dan hanya 10% yang sudah siap ke tingkat mahir dengan rincian sebagai berikut: (1) Pada tingkat
pemula, Chatbot sederhana berbasis FAQ dapat menjawab 70% pertanyaan pelanggan, tetapi eskalasi
ke manusia tetap tinggi (60%). (2) Pada tingkat menengah, dengan analisis sentimen sederhana dan
handoff manual, Chatbot mampu menurunkan eskalasi menjadi 45%. (3) Pada tingkat mahir, dengan
integrasi handoff otomatis, CRM, dan dashboard analitik, eskalasi hanya 35% dengan peningkatan
CSAT rata rata 4.4.
Tabel 4. Simulasi Roadmap Implementasi pada UMKM
Tingkat
Kapabilitas Fitur Utama Proporsi UMKM (%) Rata rata CSAT Eskalasi (%)
Pemula FAQ Chatbot + WhatsApp Business 60 3.8 60
Menengah Chatbot + analisis sentimen + handoff manual 30 4.1 45
Mahir Chatbot + handoff otomatis + CRM + dashboard 10 4.4 35
4.2 Pembahasan
4.2.1 Diferensiasi Tugas dan Relevansinya bagi Human dan AI Collaboration
Temuan mengenai taksonomi tugas menunjukkan bahwa lebih dari setengah interaksi pelanggan
(55%) termasuk kategori sederhana yang dapat ditangani Chatbot dengan tingkat keberhasilan tinggi
(95%). Hal ini sejalan dengan studi [20] yang menekankan bahwa Chatbot memiliki comparative
advantage pada domain informasi rutin dan terstruktur. Namun, untuk tugas menengah dan kompleks,
keterbatasan Chatbot menjadi jelas. Hanya 40% dari interaksi menengah dapat diselesaikan Chatbot
tanpa eskalasi, dan hampir semua interaksi kompleks tetap memerlukan manusia. Hal ini memperkuat
teori task dan technology fit , bahwa efektivitas teknologi bukanlah fungsi absolut, melainkan
bergantung pada kesesuaian dengan kompleksitas tugas  [12]. Dengan demikian, hasil penelitian ini
mendukung argumen literatur bahwa strategi integrasi Chatbot bukanlah sekadar substitusi manusia,
melainkan complementary design  yang memastikan bahwa setiap aktor Chatbot atau agen
manusiadilibatkan sesuai dengan kompetensi optimalnya. Praktisnya, UMKM dapat menggunakan
taksonomi ini untuk merancang alur kerja yang lebih realistis, misalnya mengalokasikan Chatbot untuk
FAQ dan informasi produk, sementara agen manusia fokus pada penanganan keluhan dan negosiasi.

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  396
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
4.2.2 Mekanisme Handoff sebagai Safety Net
Penerapan handoff berbasis trigger terbukti menjadi mekanisme penting untuk menjaga kualitas
pengalaman pelanggan. Dari simulasi, 40% percakapan dialihkan ke agen manusia, dengan sentimen
negatif menjadi pemicu utama (50% kasus). Hal ini konsisten dengan penelitian [10] yang menunjukkan
bahwa integrasi sentiment analysis dalam Chatbot meningkatkan kepuasan pelanggan karena sistem
dapat mengenali tanda tanda frustrasi lebih dini. Dari sisi desain sistem, handoff yang dirancang dengan
indikator terukur berfungsi sebagai safety net yang melindungi pelanggan dari pengalaman buruk akibat
Chatbot yang gagal menjawab pertanyaan kompleks. Jika tanpa trigger, CSAT hanya 3.2; dengan
trigger, CSAT meningkat menjadi 4.2. Ini menegaskan peran human in the loop bukan hanya sebagai
cadangan, tetapi sebagai elemen struktural dalam hybrid system[8] [21]. Bagi UMKM, hal ini berarti
investasi pada algoritme sederhana untuk deteksi trigger dapat memberikan dampak signifikan pada
persepsi pelanggan.
4.2.3 Peningkatan CX Melalui Model Hybrid
Evaluasi CX memperlihatkan peningkatan signifikan pada keempat indikator utama. CSAT naik
dari 3.6 menjadi 4.2, waktu penyelesaian turun dari 6.2 menit menjadi 3.8 menit, dan loyalitas
pelanggan meningkat dari 52% menjadi 68%. Perubahan ini tidak hanya ber sifat statistik tetapi juga
manajerial. Peningkatan CSAT sebesar 16,7% berarti lebih banyak pelanggan merasa puas dan
kemungkinan besar akan merekomendasikan layanan tersebut. Penurunan waktu penyelesaian hampir
40% menunjukkan efisiensi operasional yang penting bagi UMKM dengan keterbatasan tenaga kerja.
Temuan ini sejalan dengan literatur tentang customer experience management, di mana efisiensi dan
kepuasan bersama sama memengaruhi retensi pelanggan [22]. Peningkatan loyalitas sebesar 19,2%
memperlihatkan bahwa hybrid model tidak hanya memberikan hasil jangka pendek tetapi juga
menciptakan basis pelanggan yang lebih stabil. Bagi UMKM, implikasinya adalah bahwa transformasi
digital yang dirancang dengan model kolaboratif dapat meningkatkan keberlanjutan bisnis di tengah
kompetisi ketat.
4.2.4 Roadmap Implementasi dan Kesiapan UMKM
Roadmap implementasi yang terbagi dalam tiga tingkat kapabilitas memberikan panduan praktis
bagi UMKM. Pada tingkat pemula, sebagian besar UMKM (60%) dapat mulai dengan Chatbot FAQ
sederhana, yang walaupun masih menimbulkan tingkat eskalasi tinggi (60%), sudah cukup untuk
mengurangi beban staf. Pada tingkat menengah (30% UMKM), penambahan analisis sentimen dan
handoff manual menurunkan eskalasi ke 45% dan meningkatkan CSAT menjadi 4.1. Pada tingkat mahir
(10% UMKM), integrasi penuh dengan CRM dan dashboard analitik membawa CSAT ke 4.4 dan
menurunkan eskalasi ke 35%. Implikasi dari roadmap ini adalah bahwa adopsi teknologi layanan
pelanggan tidak harus bersifat one size fits all. Sebaliknya, adopsi harus disesuaikan dengan kapasitas
finansial, digital literacy, dan kesiapan organisasi UMKM. Hal ini mendukung temuan [3] yang
menekankan pentingnya phased adoption strategies dalam transformasi digital sektor UMKM. Dengan
roadmap ini, UMKM dapat menghindari risiko kegagalan implementasi akibat adopsi teknologi yang
terlalu cepat dan tidak sesuai dengan kesiapan internal.
4.2.5 Integrasi Teori dan Praktik
Secara teoretis, penelitian ini memberikan kontribusi pada literatur human dan AI collaboration
dan omnichannel CX  dengan menunjukkan bagaimana taksonomi tugas dan trigger handoff dapat
digunakan sebagai kerangka desain praktis. Secara praktis, hasil penelitian ini menyediakan panduan
aplikatif bagi UMKM Indonesia yang sedang menghadapi keterbatasan sumber daya namun perlu
memenuhi ekspektasi pelanggan yang semakin tinggi. Simulasi data menunjukkan bahwa penerapan
hybrid model secara bertahap mampu meningkatkan efisiensi, mengurangi beban kerja staf, dan
meningkatkan loyalitas pelanggan. Dengan demikian, penelitian ini memperkuat argumen bahwa
keberhasilan transformasi digital di sektor UMKM bukan semata mata ditentukan oleh teknologi yang
digunakan, tetapi oleh kesesuaian desain sistem dengan konteks operasional dan karakteristik
pelanggan.
5. KESIMPULAN
Penelitian ini merancang dan mengevaluasi model kolaborasi antara Chatbot dan agen manusia
dengan mekanisme handoff berbasis trigger untuk mengoptimalkan layanan pelanggan UMKM di

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  397
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
Indonesia. Berdasarkan hasil simulasi terhadap 5.000 percakapan pelanggan, model hybrid yang
menggabungkan teknologi Chatbot dan agen manusia terbukti memberikan dampak signifikan  pada
pengalaman pelanggan. Penggunaan mekanisme handoff berbasis trigger yang mengidentifikasi
sentimen negatif, pertanyaan kompleks, dan permintaan eksplisit untuk berbicara dengan manusia
berhasil meningkatkan Customer Satisfaction Score (CSAT) dari 3.6 menjadi 4.2. Selain itu, model ini
juga mengurangi waktu penyelesaian interaksi pelanggan dari 6.2 menit menjadi 3.8 menit, serta
menurunkan tingkat eskalasi percakapan dari 100% menjadi 40%. Peningkatan loyalitas pelanggan juga
tercatat signifikan, yaitu dari 52% menjadi 68%.
Mekanisme handoff berbasis trigger ini memungkinkan transisi yang tepat waktu antara Chatbot
dan agen manusia, yang tidak hanya meningkatkan efisiensi operasional, tetapi juga kualitas
pengalaman pelanggan secara keseluruhan. Dengan memanfaatkan indikator yang jelas dan terukur,
model hybrid ini membuktikan bahwa teknologi AI, dalam hal ini Chatbot, dapat berkolaborasi secara
efektif dengan agen manusia, terutama pada tugas -tugas kompleks yang membutuhkan empati dan
pemahaman kontekstual. Dalam konteks UMKM, temuan ini memberikan bukti empiris bahwa adopsi
teknologi tidak perlu bersifat menggantikan tenaga manusia, tetapi dapat menjadi kolaborasi yang
saling melengkapi, sesuai dengan karakteristik dan kapabilitas masing-masing.
Selain itu, hasil penelitian ini juga menghasilkan roadmap implementasi bertingkat yang
mengadaptasi kemampuan digital UMKM, yang sebagian besar berada pada tingkat pemula hingga
menengah. Adopsi teknologi ini dapat dilakukan secara bertahap, dimulai dengan penggunaan Chatbot
berbasis FAQ sederhana pada UMKM yang baru memulai, dan kemudian berkembang ke integrasi
sistem lebih kompleks seperti analisis sentimen dan handoff otomatis pada tingkat yang lebih maju.
Dengan roadmap ini, UMKM dapat menghindari disrupsi besar dalam operasi bisnis mereka, sembari
tetap mampu meningkatkan efisiensi dan kualitas layanan pelanggan.
Namun, meskipun model ini menunjukkan hasil yang positif, penelitian ini memiliki beberapa
keterbatasan yang perlu diperhatikan. Salah satunya adalah keterbatasan pada data percakapan yang
hanya diambil dari UMKM di Kota Semarang, yang mungkin tidak sepenuhnya representatif untuk
UMKM di seluruh Indonesia. Oleh karena itu, penelitian lebih lanjut dapat memperluas cakupan ke
wilayah atau sektor UMKM yang lebih beragam untuk memperkuat generalisasi temuan ini. Selain itu,
mekanisme handoff yang diuji dalam penelitian ini hanya melibatkan beberapa indikator utama.
Penelitian berikutnya dapat mengembangkan model dengan lebih banyak variabel atau elemen dalam
proses transisi untuk melihat apakah faktor -faktor lain, seperti kecepatan respon atau tingkat
kenyamanan interaksi, dapat mempengaruhi hasil yang lebih optimal.
Implikasi praktis dari penelitian ini sangat penting bagi UMKM yang ingin mengadopsi teknologi
Chatbot untuk meningkatkan layanan pelanggan mereka. Dengan pendekatan bertahap dan sistem yang
terintegrasi dengan baik antara Chatbot dan agen manusia, UMKM dapat memperoleh manfaat
maksimal tanpa harus menginvestasikan sumber daya  yang terlalu besar. Penelitian ini memberikan
panduan strategis bagi UMKM di Indonesia yang tengah menghadapi tantangan transformasi digital,
terutama dalam sektor layanan pelanggan yang semakin kompleks di era digital ini.
Secara keseluruhan, temuan penelitian ini memperkaya literatur mengenai kolaborasi manusia
dan AI, khususnya dalam konteks pengalaman pelanggan omnichannel, serta memberikan kontribusi
praktis dalam merancang sistem layanan pelanggan yang lebih efisien dan  responsif di UMKM.
Penelitian selanjutnya dapat mengeksplorasi potensi penerapan teknologi AI lebih lanjut, seperti
penggunaan generative AI, untuk memperluas kapasitas Chatbot dalam menangani interaksi yang lebih
kompleks, serta melakukan kajian lebih mendalam mengenai faktor -faktor budaya dan perilaku
konsumen lokal dalam penerapan model hybrid ini.
DAFTAR PUSTAKA
[1] S. M. Rahman, J. Carlson, S. P. Gudergan, M. Wetzels, and D. Grewal, “Perceived Omnichannel
Customer Experience (OCX): Concept, measurement, and impact,” J. Retail., vol. 98, no. 4, pp.
611–632, Dec. 2022, doi: 10.1016/j.jretai.2022.03.003.,
https://linkinghub.elsevier.com/retrieve/pii/S0022435922000239
[2] J. A. Balbín Buckley and P. S. Marquina Feldman, “Effects of channel integration on the
omnichannel customer experience,” Cogent Bus. Manag., vol. 11, no. 1, p. 2364841, Dec. 2024,
doi: 10.1080/23311975.2024.2364841.,

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  398
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
https://www.tandfonline.com/doi/full/10.1080/23311975.2024.2364841
[3] S. Purnomo, N. Nurmalitasari, and N. Nurchim, “Digital transformation of MSMEs in Indonesia:
A systematic literature review,” J. Manag. Digit. Bus., vol. 4, no. 2, pp. 301–312, Aug. 2024, doi:
10.53088/jmdb.v4i2.1121.,
https://journal.nurscienceinstitute.id/index.php/jmdb/article/view/1121
[4] T. TH. Tambunan and I. Busnetti, “Recent Evidence on the Digitalization Process in Indonesia’s
Micro and Small Enterprises,” Int. J. Curr. Sci. Res. Rev. , vol. 07, no. 08, Aug. 2024, doi:
10.47191/ijcsrr/V7-i8-18., https://ijcsrr.org/wp-content/uploads/2024/08/18-0608-2024.pdf
[5] M. A. Nadzif, Saefurrohman, and R. Soelistijadi, “Penggunaan Teknologi Natural Language
Processing dalam Sistem Chatbot untuk Peningkatan Layanan Informasi Administrasi Publik,”
Indones. J. Comput. Sci. , vol. 13, no. 1, Feb. 2024, doi: 10.33022/ijcs.v13i1.3645.,
https://ijcs.net/ijcs/index.php/ijcs/article/view/3645
[6] X. Lin, X. Wang, B. Shao, and J. Taylor, “How Chatbots Augment Human Intelligence in
Customer Services: A Mixed-Methods Study,” J. Manag. Inf. Syst., vol. 41, no. 4, pp. 1016–1041,
Oct. 2024, doi: 10.1080/07421222.2024.2415773.,
https://www.tandfonline.com/doi/full/10.1080/07421222.2024.2415773
[7] R. Hayati, R. Buaton, and S. Ramadani, “Implementation of Chatbot Artificial Intelligence in a
Company Website to Improve Customer Service Automatically Using the TF -IDF Method,” J.
Artif. Intell. Eng. Appl. , vol. 4, no. 1, pp. 131 –136, Oct. 2024, doi: 10.59934/jaiea.v4i1.584.,
https://ioinformatic.org/index.php/JAIEA/article/view/584
[8] E. Mosqueira-Rey, E. Hernández-Pereira, D. Alonso-Ríos, J. Bobes-Bascarán, and Á. Fernández-
Leal, “Human-in-the-loop machine learning: a state of the art,” Artif. Intell. Rev., vol. 56, no. 4,
pp. 3005 –3054, Apr. 2023, doi: 10.1007/s10462 -022-10246-w.,
https://link.springer.com/10.1007/s10462-022-10246-w
[9] U. Gnewuch, S. Morana, O. Hinz, R. Kellner, and A. Maedche, “More Than a Bot? The Impact of
Disclosing Human Involvement on Customer Interactions with Hybrid Service Agents,” Inf. Syst.
Res., vol. 35, no. 3, pp. 936 –955, Sep. 2024, doi: 10.1287/isre.2022.0152.,
https://pubsonline.informs.org/doi/10.1287/isre.2022.0152
[10] S. Kim and R. Priluck, “Consumer Responses to Generative AI Chatbots Versus Search Engines
for Product Evaluation,” J. Theor. Appl. Electron. Commer. Res., vol. 20, no. 2, p. 93, May 2025,
doi: 10.3390/jtaer20020093., https://www.mdpi.com/0718-1876/20/2/93
[11] D. G. Markovitch, R. A. Stough, and D. Huang, “Consumer reactions to Chatbot versus human
service: An investigation in the role of outcome valence and perceived empathy,” J. Retail.
Consum. Serv. , vol. 79, p. 103847, Jul. 2024, doi: 10.1016/j.jretconser.2024.103847.,
https://linkinghub.elsevier.com/retrieve/pii/S0969698924001437
[12] M. Vaccaro, A. Almaatouq, and T. Malone, “When combinations of humans and AI are useful: A
systematic review and meta-analysis,” Nat. Hum. Behav., vol. 8, no. 12, pp. 2293–2303, Oct. 2024,
doi: 10.1038/s41562-024-02024-1., https://www.nature.com/articles/s41562-024-02024-1
[13] B. Khalid, “Evaluating customer perspectives on omnichannel shopping satisfaction in the fashion
retail sector,” Heliyon, vol. 10, no. 16, p. e36027, Aug. 2024, doi: 10.1016/j.heliyon.2024.e36027.,
https://linkinghub.elsevier.com/retrieve/pii/S2405844024120580
[14] M. Kim, S. Yang, B. Kim, J. Kim, and D. Kim, “Human -to-Robot Handover Based on
Reinforcement Learning,” Sensors, vol. 24, no. 19, p. 6275, Sep. 2024, doi: 10.3390/s24196275.,
https://www.mdpi.com/1424-8220/24/19/6275
[15] M. Rizki, A. Fitriansyah, and M. Narji, “APLIKASI CHATBOT SEBAGAI LAYANAN LIVE
CHAT UNTUK PENERIMAAN MAHASISWA BARU MENGGUNAKAN METODE WORD
STEMMING DENGAN REGULAR EXPRESSION PATTERN MATCHING,” JEIS J.
ELEKTRO DAN Inform. SWADHARMA , vol. 3, no. 2, pp. 50 –62, Jul. 2023, doi:
10.56486/jeis.vol3no2.377., https://ejurnal.swadharma.ac.id/index.php/jeis/article/view/377
[16] T. Alang and K. M. Nguyen, “Determinants of Omnichannel Shoppers’ Perceived Value and their
Shopping Intention,” Int. J. Electron. Commer. Stud. , vol. 13, no. 2, p. 203, Mar. 2022, doi:
10.7903/ijecs.2035., https://linkinghub.elsevier.com/retrieve/pii/S2405844024120580
[17] J. Radomska, A. Kawa, M. Hajdas, P. Klimas, and S. C. Silva, “Unveiling retail omnichannel
challenges: developing an omnichannel obstacles scale,” Int. J. Retail Distrib. Manag., vol. 53, no.
13, pp. 1 –20, Dec. 2025, doi: 10.1108/IJRDM -04-2024-0169.,

DINAMIK – Volume 31, Nomor 2, 2026                           E-ISSN : 2623-1786 | P-ISSN : 0854-9524

 Model Kolaborasi Chatbot dan Manusia dengan Mekanisme Handoff Berbasis Trigger  399
untuk Optimalisasi Layanan Pelanggan UMKM di Era Digital
https://www.emerald.com/ijrdm/article/53/13/1/1267276/Unveiling-retail-omnichannel-
challenges-developing
[18] J. Liu et al., “Time to Transfer: Predicting and Evaluating Machine -Human Chatting Handoff,”
Proc. AAAI Conf. Artif. Intell. , vol. 35, no. 7, pp. 5841 –5849, May 2021, doi:
10.1609/aaai.v35i7.16731.,
https://www.researchgate.net/publication/363386035_Time_to_Transfer_Predicting_and_Evalua
ting_Machine-Human_Chatting_Handoff
[19] Y. Yue, D. Liu, Y. Lv, J. Hao, and P. Cui, “A Practical Guide and Assessment on Using ChatGPT
to Conduct Grounded Theory: Tutorial,” J. Med. Internet Res., vol. 27, p. e70122, May 2025, doi:
10.2196/70122., https://www.jmir.org/2025/1/e70122
[20] C. V. Misischia, F. Poecze, and C. Strauss, “ Chatbots in customer service: Their relevance and
impact on service quality,” Procedia Comput. Sci. , vol. 201, pp. 421 –428, 2022, doi:
10.1016/j.procs.2022.03.055., https://linkinghub.elsevier.com/retrieve/pii/S1877050922004689
[21] M. Mortati and G. Viana Mundstock Freitas, “AI in Service Design: A New Framework for Hybrid
Human–AI Service Encounters,” J. Serv. Res. , Jun. 2025, doi: 10.1177/10946705251344387.,
https://journals.sagepub.com/doi/10.1177/10946705251344387
[22] N. Ameen, A. Tarhini, A. Reppel, and A. Anand, “Customer experiences in the age of artificial
intelligence,” Comput. Human Behav. , vol. 114, p. 106548, Jan. 2021, doi:
10.1016/j.chb.2020.106548., https://linkinghub.elsevier.com/retrieve/pii/S0747563220302983
