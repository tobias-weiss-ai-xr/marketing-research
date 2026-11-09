---
title: Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data
url: https://doi.org/10.61132/jupiter.v3i4.1450
category: analytics
subcategory: review
date: 2025-07
venue: Jupiter Publikasi Ilmu Keteknikan Industri Teknik Elektro dan Informatika
authors:
- Achmad Solechan
source: openalex-oa
pdf_url: https://journal.aritekin.or.id/index.php/Jupiter/article/download/1450/1543
pages: 21
chars: 58153
fetched_at: '2026-11-08T17:42:03+00:00'
kb_version: 1
---

# Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

Jupiter: Publikasi Ilmu Keteknikan Industri, Teknik Elektro dan Informatika
Volume 3, Nomor. 4 Juli 2025
e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330
DOI: https://doi.org/10.61132/jupiter.v3i4.1450
Tersedia: https://journal.aritekin.or.id/index.php/Jupiter

Naskah masuk: 25 Juni 2025; Direvisi: 12 Juni 2025; Diterima: 29 Juli 2025; Terbit: 30 Juli 2025

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan
Keputusan Berbasis Data

Achmad Solechan
Program Studi Bisnis Digital, Universitas Telogorejo Semarang, Indonesia
Penulis Korespondensi: achmad_solechan@universitastelogorejo.ac.id

Abstract. Rapid growth of digital platforms has generated large volumes of unstructured data, particularly
customer reviews, social media comments, and online opinions, which contain valuable insights for organizations.
This study aims to examine the role of sentimen t analysis in Business Intelligence and data -driven decision-
making. The method used is a narrative literature review by analyzing 30 selected journal articles related to
sentiment analysis, business intelligence, decision -making, customer reviews, marketi ng analytics, and data -
driven culture. The findings show that sentiment analysis plays an important role in transforming textual data
into strategic information that can support customer understanding, marketing decisions, product development,
customer relationship management, reputation monitoring, and strategic planning. The integration of sentiment
analysis into Business Intelligence enables organizations to not only understand what happens through numerical
data, but also why it happens through customer  opinions and emotions. However, its implementation still faces
challenges related to data quality, informal language, sarcasm, algorithmic bias, model interpretability, and
human validation. This study implies that sentiment analysis can strengthen modern  Business Intelligence and
support more responsive, objective, and evidence-based managerial decision-making.

Keywords: Business Intelligence; Customer Reviews; Data-Driven Decision -Making; Marketing Analytics;
Sentiment Analysis.

Abstrak. Perkembangan platform digital telah menghasilkan data tidak terstruktur dalam jumlah besar, terutama
berupa ulasan pelanggan, komentar media sosial, dan opini online yang memiliki nilai strategis bagi organisasi.
Penelitian ini bertujuan untuk mengkaji per an sentiment analysis dalam Business Intelligence dan pengambilan
keputusan berbasis data. Metode yang digunakan adalah narrative literature review dengan menganalisis 30 artikel
jurnal terpilih yang berkaitan dengan sentiment analysis, Business Intelligen ce, decision -making, customer
reviews, marketing analytics, dan data -driven culture. Hasil kajian menunjukkan bahwa sentiment analysis
berperan penting dalam mengubah data teks menjadi informasi strategis yang dapat mendukung pemahaman
pelanggan, keputusan  pemasaran, pengembangan produk, customer relationship management, pemantauan
reputasi, dan perencanaan strategis. Integrasi sentiment analysis ke dalam Business Intelligence memungkinkan
organisasi tidak hanya memahami apa yang terjadi melalui data numeri k, tetapi juga memahami alasan di balik
suatu fenomena bisnis melalui opini dan emosi pelanggan. Namun, penerapannya masih menghadapi tantangan,
seperti kualitas data, bahasa informal, sarkasme, bias algoritma, interpretabilitas model, dan kebutuhan valida si
manusia. Kajian ini berimplikasi bahwa sentiment analysis dapat memperkuat Business Intelligence modern dan
mendukung pengambilan keputusan manajerial yang lebih responsif, objektif, dan berbasis bukti.

Kata kunci : Analisis Sentimen; Analitik Pemasaran; Business Intelligence ; Pengambilan Keputusan Berbasis
Data; Ulasan Pelanggan.

1. LATAR BELAKANG
Transformasi digital telah mendorong organisasi untuk semakin bergantung pada data
dalam memahami dinamika pasar, perilaku konsumen, serta perubahan lingkungan bisnis.
Perkembangan platform digital, media sosial, e -commerce, aplikasi layanan pelanggan, dan
kanal komunikasi daring telah menghasilkan data dalam jumlah besar, baik dalam bentuk
terstruktur maupun tidak terstruktur. Salah satu bentuk data tidak terstruktur yang memiliki
nilai strategis adalah teks opini pelanggan, seperti ulasan produk, komentar media sosial,
tanggapan layanan, berita bisnis, dan percakapan digit al. Data tersebut mencerminkan

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

311        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

pengalaman, persepsi, emosi, dan preferensi konsumen yang dapat dimanfaatkan organisasi
untuk memperbaiki produk, meningkatkan layanan, serta memperkuat strategi bisnis (Aguilar-
Moreno et al., 2024); (Cui et al., 2023); (Ligthart et al., 2021).
Dalam konteks bisnis modern, pemanfaatan data tidak lagi hanya berfokus pada
pencatatan transaksi, tetapi juga pada kemampuan organisasi dalam mengubah data menjadi
wawasan yang dapat digunakan untuk pengambilan keputusan. Business Intelligence (BI) hadir
sebagai pendekatan strategis yang memungkinkan organisasi mengumpulkan, mengolah,
menganalisis, dan menyajikan data dalam bentuk informasi yang relevan bagi manajemen. BI
berperan dalam mendukung pengambilan keputusan di berbagai level organisasi melalui
penyediaan informasi yang cepat, akurat, dan berbasis bukti. (Mekimah et al., 2024)
menjelaskan bahwa BI merupakan alat penting dalam pengambilan keputusan organisasi
karena mampu mengubah data menjadi insight yang mendukung keputusan strategis dan
keunggulan kompetitif. Sejalan dengan itu, (Hurbean et al., 2025)  menunjukkan bahwa
business intelligence and analytics serta budaya berbasis data berpengaruh terhadap efektivitas
pengambilan keputusan dan kinerja manajerial.
Namun demikian, BI tradisional cenderung lebih banyak memanfaatkan data terstruktur,
seperti data penjualan, laporan keuangan, data pelanggan, indikator operasional, serta ukuran
kinerja organisasi. Padahal, dalam era digital, banyak informasi penting justru tersimpan dalam
data tidak terstruktur berupa teks opini pelanggan. Data opini tersebut sering kali berisi
informasi yang lebih kaya karena dapat menjelaskan alasan di balik kepuasan, ketidakpuasan,
loyalitas, keluhan, atau persepsi pelanggan terhadap s uatu produk dan layanan. Oleh karena
itu, organisasi membutuhkan pendekatan analitik yang mampu mengekstraksi makna dari data
teks tersebut agar dapat diintegrasikan ke dalam sistem BI.
Salah satu pendekatan yang dapat digunakan untuk menjawab kebutuhan tersebut adalah
sentiment analysis. Sentiment analysis atau opinion mining merupakan teknik dalam Natural
Language Processing (NLP) yang digunakan untuk mengidentifikasi, mengekstraksi, da n
mengklasifikasikan opini, emosi, serta sikap seseorang terhadap suatu objek, produk, layanan,
organisasi, atau peristiwa. (Rokade & Aruna Kumari, 2019)  menjelaskan bahwa sentiment
analysis digunakan untuk menganalisis sentimen, penilaian, dan impresi masyarakat terhadap
entitas, topik, maupun layanan, sehingga hasilnya dapat dimanfaatkan oleh individu, bisnis,
dan pemerintah dalam proses pengambilan keputusan. Dalam kajian lain, (Ligthart et al., 2021)
menegaskan bahwa sentiment analysis berperan penting dalam membantu bisnis memahami
umpan balik pelanggan terhadap produk dan layanan, khususnya pada budaya bisnis yang
semakin berorientasi pada pelanggan.

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

Peran sentiment analysis dalam BI menjadi semakin penting karena organisasi tidak
cukup hanya mengetahui apa yang terjadi, tetapi juga perlu memahami mengapa suatu
fenomena bisnis terjadi. Misalnya, penurunan penjualan tidak hanya dapat dijelaskan melalui
angka transaksi, tetapi juga melalui opini negatif pelanggan terkait kualitas produk, harga,
layanan, pengiriman, atau pengalaman penggunaan. (Kauffmann et al., 2019)  menunjukkan
bahwa sentiment analysis terhadap ulasan online dapat membantu pengambilan keputusan
pemasaran dengan mengevaluasi fitur produk berdasarkan opini konsumen. Text mining dan
sentiment analysis terhadap ulasan online dapat digunakan untuk memahami sentimen
pelanggan dan daya saing produk, sehingga dapat membantu perusahaan mengoptimalkan
produk dan layanan. Dengan demikian, sentiment analysis dapat memperkaya BI kare na
mampu menghubungkan indikator kuantitatif dengan pemahaman kualitatif mengenai persepsi
pelanggan (Wen et al., 2024).
Selain dalam pemasaran, sentiment analysis juga berperan dalam customer relationship
management (CRM), e-commerce, perencanaan strategis, layanan pelanggan, dan pengelolaan
reputasi. (Capuano et al., 2021)  menjelaskan bahwa sentiment analysis dalam CRM dapat
membantu mengukur kepuasan pelanggan, memantau opini konsumen, menentukan prioritas
permintaan, mempercepat respons, dan membangun loyalitas pelanggan.  (Grande-Ramírez et
al., 2022) mengintegrasikan sentiment analysis media sosial ke dalam proses strategic planning
untuk menghasilkan balanced scorecard, sehingga informasi tekstual yang tidak terstruktur
dapat diarahkan pada indikator kinerja utama organisasi. Sementara itu, (Nichifor et al., 2023)
menunjukkan bahwa kecerdasan buatan dapat dimanfaatkan untuk mengubah ulasan pelanggan
menjadi peningkatan bisnis melalui sentiment analysis, khususnya dalam konteks e-commerce.
Perkembangan metode sentiment analysis juga menunjukkan kemajuan yang signifikan.
Pada tahap awal, sentiment analysis banyak menggunakan pendekatan berbasis leksikon dan
machine learning tradisional. Namun, perkembangan deep learning, transformer, dan Larg e
Language Models (LLMs) telah membuka peluang baru dalam analisis sentimen yang lebih
kontekstual dan adaptif. (Ghatora et al., 2024) menunjukkan bahwa model LLM seperti GPT-
4 mampu menangkap sentimen yang lebih halus pada teks yang kaya konteks dibandingkan
beberapa model tradisional. (Ashbaugh & Zhang, 2024) juga membandingkan model machine
learning dan deep learning dalam menganalisis ulasan pelanggan, serta menegaskan bahwa
setiap pendekatan memiliki kekuatan dan keterbatasan masing -masing. Dalam konteks
Indonesia, (Wangsa et al., 2025) mengembangkan topic-level sentiment analysis berbasis LLM
pada ulasan konsumen e -grocery, yang menunjukkan bahwa sentiment analysis dapat
memberikan insight strategis bagi keputusan bisnis di ekonomi digital.

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

313        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

Meskipun memiliki potensi besar, penerapan sentiment analysis dalam BI dan
pengambilan keputusan berbasis data masih menghadapi berbagai tantangan. Tantangan
tersebut mencakup kualitas data, bahasa tidak baku, sarkasme, ambiguitas makna, bias
algoritma, ke terbatasan dataset, rendahnya interpretabilitas model, serta kebutuhan validasi
manusia. (Hua et al., 2024)  menunjukkan bahwa penelitian aspect -based sentiment analysis
masih menghadapi masalah keberagaman domain dan dataset, sehingga dapat menghambat
generalisasi hasil penelitian. (Adak et al., 2022) juga menekankan bahwa banyak model deep
learning dalam analisis sentimen masih bersifat sulit diinterpretasikan, sehingga diperlukan
pendekatan explainable artificial intelligence agar hasil analisis lebih dapat dipercaya oleh
organisasi. Selain itu, (Herrera-Poyatos et al., 2025)  menegaskan bahwa penggunaan LLM
dalam sentiment analysis masih memiliki tantangan terkait ketidakpastian, variasi keluaran
model, sensitivitas prompt, dan kebutuhan explainability.
Berdasarkan perkembangan tersebut, kajian mengenai peran sentiment analysis dalam BI
dan pengambilan keputusan berbasis data menjadi penting untuk dilakukan. Sejumlah
penelitian telah membahas sentiment analysis dalam konteks pemasaran, CRM, e -commerce,
ulasan pelanggan, media sosial, dan prediksi bisnis. Namun, kajian yang secara naratif
menghubungkan sentiment analysis dengan BI serta pengambilan keputusan be rbasis data
masih perlu diperkuat, terutama untuk menjelaskan bagaimana data opini pelanggan dapat
diubah menjadi insight strategis yang mendukung keputusan organisasi. Oleh karena itu, artikel
ini menggunakan pendekatan narrative literature review untuk m enyintesis berbagai temuan
penelitian terdahulu mengenai kontribusi sentiment analysis dalam memperkuat BI,
mendukung keputusan berbasis data, serta mengidentifikasi manfaat, tantangan, dan arah
pengembangan penelitian ke depan.
Tujuan artikel ini adalah untuk mengkaji peran sentiment analysis dalam Business
Intelligence dan pengambilan keputusan berbasis data berdasarkan literatur terdahulu. Secara
khusus, artikel ini bertujuan untuk menjelaskan konsep sentiment analysis dalam ko nteks BI,
mengidentifikasi kontribusinya terhadap pengambilan keputusan organisasi, menganalisis
manfaat integrasi data sentimen ke dalam BI, serta menguraikan tantangan dan peluang
pengembangan sentiment analysis dalam mendukung organisasi yang semakin be rorientasi
pada data.

2. KAJIAN TEORITIS
Sentiment analysis atau opinion mining merupakan bagian dari Natural Language
Processing (NLP) yang digunakan untuk mengidentifikasi, mengekstraksi, dan

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

mengklasifikasikan opini, emosi, serta sikap seseorang terhadap suatu objek, seperti produk,
layanan, merek, organisasi, maupun peristiwa. Dalam konteks bisnis, sentiment analysis
digunakan untuk memahami persepsi pelanggan melalui ulasan online, komentar media sosial,
berita bisnis, percakapan digital, dan berbagai bentuk user -generated content. (Rokade &
Aruna Kumari, 2019)  menjelaskan bahwa sentiment analysis dapat digunakan untuk
menganalisis sentimen dan penilaian masyarakat terhadap entitas, topik, maupun layanan
sehingga hasilnya dapat dimanfaatkan oleh organisasi dalam pengambilan keputusan. Sejalan
dengan itu, (Ligthart et al., 2021)  menegaskan bahwa sentiment analysis memiliki peran
penting dalam membantu bisnis memahami umpan balik pelanggan terhadap produk dan
layanan.
Perkembangan sentiment analysis semakin relevan karena meningkatnya volume data
tidak terstruktur di era digital. (Cui et al., 2023) menjelaskan bahwa sentiment analysis dapat
digunakan untuk menambang sikap, emosi, evaluasi, dan opini masyarakat terhadap isu,
produk, layanan, dan peristiwa. Pada tingkat yang lebih rinci, aspect -based sentiment analysis
(ABSA) mampu mengidentifikasi asp ek tertentu dari suatu produk atau layanan dan
menghubungkannya dengan sentimen pelanggan. (Hua et al., 2024) menyatakan bahwa ABSA
memberikan analisis yang lebih detail karena pelanggan dapat memiliki sentimen berbeda
terhadap aspek produk yang berbeda, misalnya positif terhadap kualitas tetapi negatif terhadap
harga atau layanan pengiriman.
Business Intelligence (BI) merupakan pendekatan yang digunakan organisasi untuk
mengumpulkan, mengolah, menganalisis, dan menyajikan data menjadi informasi yang
berguna bagi pengambilan keputusan. BI mencakup proses integrasi data, pelaporan,
visualisasi, dashboard, data mining, serta analitik bisnis. (Mekimah et al., 2024)  menjelaskan
bahwa BI menjadi alat penting dalam pengambilan keputusan organisasi karena mampu
mengubah data menjadi actionable insights yang mendukung keputusan strategis dan
keunggulan kompetitif. (Hurbean et al., 2025) juga menunjukkan bahwa Business Intelligence
and Analytics (BI&A) serta budaya berbasis data berpengaruh terhadap efektivitas
pengambilan keputusan dan kinerja manajerial. Dengan demikian, BI tidak hanya berkaitan
dengan teknologi, tetapi juga dengan kemampuan organisasi membangun budaya pengambilan
keputusan berbasis data.
Dalam konteks transformasi digital, BI semakin penting karena organisasi dituntut untuk
mampu memanfaatkan data sebagai dasar strategi bisnis. (Solechan et al., 2023) menekankan
bahwa transformasi digital berperan dalam meningkatkan daya saing UMKM. Hal ini
menunjukkan bahwa kemampuan organisasi dalam mengadopsi teknologi digital menjadi

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

315        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

faktor penting dalam memperkuat kinerja dan daya saing. Selain itu, (Solechan & Abidin,
2024) membahas implementasi teknologi blockchain dalam digital marketing, yang
memperlihatkan bahwa perkembangan teknologi digital mendorong perubahan cara organisasi
mengelola data, pemasaran, dan hubungan dengan konsumen. Oleh karena itu, integrasi
sentiment analysis ke dalam BI dapat dipahami sebagai bagian dari transformasi digital yang
mendukung organisasi dalam memahami pelanggan secara lebih cepat dan berbasis data.
Sentiment analysis dapat menjadi bagian penting dari BI modern karena mampu
mengolah data tidak terstruktur menjadi informasi yang bernilai strategis. (Aguilar-Moreno et
al., 2024)  menunjukkan bahwa sentiment analysis semakin banyak digunakan untuk
mendukung business decision -making, khususnya melalui pemanfaatan ulasan pelanggan,
media sosial, dan platform digital. (Kauffmann et al., 2019)  juga menunjukkan bahwa
sentiment analysis terhadap ulasan online dapat membantu pengambilan keputusan pemasaran
melalui evaluasi fitur produk berdasarkan opini konsumen. Dengan demikian, sentiment
analysis dapat memperkaya BI karena tidak hanya menjelaska n apa yang terjadi berdasarkan
angka, tetapi juga mengapa hal tersebut terjadi berdasarkan persepsi pelanggan.
Peran sentiment analysis dalam pengambilan keputusan berbasis data dapat dilihat pada
berbagai bidang, seperti e -commerce, customer relationship management, pemasaran digital,
layanan pelanggan, pariwisata, startup, dan keuangan. (Capuano et al., 2021)  menjelaskan
bahwa sentiment analysis dalam Customer Relationship Management (CRM) dapat membantu
mengukur kepuasan pelanggan, memantau opini konsumen, menentukan prioritas permintaan,
dan mempercepat respons organisasi. (Nichifor et al., 2023)  menunjukkan bahwa kecerdasan
buatan dapat digunakan untuk mengubah ulasan pelanggan menjadi peningkatan bisnis. (Wen
et al., 2024) juga menjelaskan bahwa text mining dan sentiment analysis terhadap ulasan online
dapat digunakan untuk memahami sentimen pelanggan dan daya saing produk.
Perkembangan metode sentiment analysis juga mengalami kemajuan dari pendekatan
berbasis leksikon, machine learning, deep learning, hingga Large Language Models (LLMs).
(Hamed & Madanchian, 2023)  menyatakan bahwa artificial intelligence meningkatkan
kemampuan sentiment analysis karena mampu memahami nada suatu pernyataan, bukan
sekadar mengenali kata positif atau negatif. (Ghatora et al., 2024)  menunjukkan bahwa LLM
seperti GPT-4 mampu menangkap sentimen yang lebih halus pada teks yang kaya konteks.
(Wangsa et al., 2025) juga mengembangkan topic-level sentiment analysis berbasis LLM pada
ulasan konsumen e -grocery, yang menunjukkan bahwa analisis sentimen dapat membantu
bisnis memperoleh insight strategis pada tingkat topik tertentu.

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

Meskipun demikian, penerapan sentiment analysis dalam BI masih memiliki tantangan.
Tantangan tersebut mencakup kualitas data, bahasa informal, sarkasme, ambiguitas makna,
bias algoritma, keterbatasan dataset, serta rendahnya interpretabilitas model. (Adak et al.,
2022) menekankan pentingnya explainable artificial intelligence karena banyak model deep
learning dalam sentiment analysis sulit diinterpretasikan. (Herrera-Poyatos et al., 2025)  juga
menjelaskan bahwa LLM menghadapi persoalan ketidakpastian dan variasi hasil model,
sehingga diperlukan transparansi, validasi, dan explainability agar hasil analisis dapat
dipercaya dalam pengambilan keputusan.
Berdasarkan kajian tersebut, sentiment analysis dapat dipahami sebagai mekanisme
analitik yang menghubungkan data opini pelanggan dengan proses BI dan pengambilan
keputusan berbasis data. Data tidak terstruktur berupa ulasan pelanggan, komentar media
sosial, berita bisnis, dan percakapan digital dapat diproses menjadi insight yang kemudian
diintegrasikan ke dalam dashboard BI, laporan manajerial, sistem pendukung keputusan, atau
perencanaan strategis. Dengan demikian, sentiment analysis memiliki peran penti ng dalam
memperkuat BI modern, meningkatkan pemahaman organisasi terhadap pelanggan,
mendukung strategi pemasaran, memperbaiki kualitas layanan, serta membantu organisasi
mengambil keputusan yang lebih responsif, objektif, dan berbasis data.

3. METODE PENELITIAN
Penelitian ini menggunakan metode narrative literature review (NLR), yaitu kajian
pustaka yang dilakukan dengan menelaah, membandingkan, dan menyintesis berbagai hasil
penelitian terdahulu yang relevan dengan topik kajian. Pendekatan ini digunakan karena
penelitian bertujuan untuk menjelaskan secara konseptual peran sentiment analysis dalam
Business Intelligence dan pengambilan keputusan berbasis data. Kajian pustaka merupakan
proses penting dalam penelitian karena membantu peneliti memahami teori, konsep, hasil
penelitian sebelumnya, serta menemukan celah penelitian yang masih dapat dikembangkan
(Sugiyono, 2019) . Selain itu, pendekatan kualitatif dalam kajian literatur memungkinkan
peneliti melakukan interpretasi mendalam terhadap berbagai sumber ilmiah yang berkaitan
dengan fenomena yang diteliti (Moleong, 2017).
Sumber data dalam penelitian ini adalah 30 artikel jurnal referensi inti yang relevan
dengan tema sentiment analysis, Business Intelligence, decision -making, customer reviews,
marketing analytics, dan data -driven culture. Artikel -artikel tersebut dipilih k arena memiliki
keterkaitan langsung dengan tujuan penelitian, yaitu mengkaji bagaimana data opini pelanggan
dan data teks tidak terstruktur dapat diolah menjadi insight yang mendukung Business

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

317        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

Intelligence dan pengambilan keputusan organisasi. (Aguilar-Moreno et al., 2024) menjelaskan
bahwa sentiment analysis semakin banyak digunakan untuk mendukung business decision -
making melalui pemanfaatan data tidak terstruktur dari platform online. Sementara itu,
(Mekimah et al., 2024)  menegaskan bahwa Business Intelligence berperan penting dalam
mengubah data menjadi actionable insights untuk mendukung keputusan organisasi.
Seleksi artikel dilakukan berdasarkan beberapa kriteria inklusi, yaitu artikel membahas
sentiment analysis atau opinion mining dalam konteks bisnis, pemasaran, e -commerce,
customer reviews, media sosial, CRM, atau pengambilan keputusan; artikel membahas
Business Intelligence, data-driven culture, atau decision-making; artikel tersedia dalam bentuk
jurnal ilmiah; serta artikel memiliki relevansi langsung dengan fokus penelitian. Adapun artikel
yang hanya membahas aspek teknis algoritma tanpa keterkaitan deng an bisnis atau
pengambilan keputusan tidak dijadikan sumber utama.
Tahapan penelitian dilakukan melalui empat langkah. Pertama, menentukan fokus kajian,
yaitu peran sentiment analysis dalam Business Intelligence dan pengambilan keputusan
berbasis data. Kedua, mengidentifikasi dan memilih 30 artikel jurnal inti yang relevan. Ketiga,
membaca dan mengelompokkan artikel berdasarkan tema, seperti konsep sentiment analysis,
BI, customer reviews, marketing analytics, data -driven culture, machine learning, deep
learning, LLM, serta tantangan implementasi. Keempat, melakukan sintes is naratif dengan
membandingkan temuan antarartikel untuk memperoleh pemahaman mengenai manfaat, peran,
tantangan, dan arah pengembangan sentiment analysis dalam BI.
Analisis data dilakukan secara deskriptif -kualitatif melalui proses reduksi, kategorisasi,
sintesis, dan interpretasi literatur. Reduksi dilakukan dengan memilih informasi yang relevan
dari setiap artikel. Kategorisasi dilakukan dengan mengelompokkan artik el berdasarkan tema
utama. Sintesis dilakukan dengan membandingkan hasil penelitian terdahulu, sedangkan
interpretasi dilakukan dengan menghubungkan temuan literatur dengan konteks pengambilan
keputusan berbasis data. Pendekatan ini digunakan agar penelitian dapat menghasilkan uraian
konseptual yang sistemat is mengenai integrasi sentiment analysis ke dalam Business
Intelligence modern.
Melalui metode narrative literature review ini, penelitian diharapkan dapat memberikan
gambaran menyeluruh mengenai peran sentiment analysis sebagai alat analitik untuk mengolah
data tidak terstruktur menjadi informasi strategis. Hasil kajian ini tidak dim aksudkan untuk
menghasilkan generalisasi statistik, melainkan untuk memberikan pemahaman konseptual dan
sintesis literatur yang dapat menjadi dasar bagi penelitian selanjutnya.

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

4. HASIL DAN PEMBAHASAN
Hasil kajian narrative literature review terhadap 30 artikel rujukan menunjukkan bahwa
sentiment analysis memiliki peran penting dalam mendukung Business Intelligence dan
pengambilan keputusan berbasis data. Secara umum, literatur yang dikaji dapat dikelompokkan
ke dalam beberapa tema utama, yaitu: sentiment analysis sebagai alat analitik data tidak
terstruktur, integrasi sentiment analysis dalam Business Intelligence, pemanfaatan customer
reviews untuk marketing analytics, dukungan sentiment analysis terha dap customer
relationship management, perkembangan metode machine learning, deep learning, dan Large
Language Models, serta tantangan implementasi sentiment analysis dalam konteks bisnis.
Tabel 1. Ringkasan Riset Terdahulu Berdasarkan Narrative Literature Review.
No.
Penulis dan
Tahun Fokus Penelitian
Metode/
Pendekatan Temuan Utama
Relevansi dengan
Penelitian
1 (Aguilar-
Moreno et al.,
2024)
Sentiment
analysis untuk
business
decision-making
Bibliometric
analysis
Sentiment
analysis semakin
banyak digunakan
untuk mendukung
keputusan bisnis,
terutama melalui
customer
feedback dari
platform online.
Menjadi dasar
bahwa sentiment
analysis relevan
untuk
pengambilan
keputusan
berbasis data.
2 (Rokade &
Aruna Kumari,
2019)
Business
intelligence
analytics
menggunakan
sentiment
analysis
Survey Sentiment
analysis
membantu
organisasi
memahami
sentimen pasar
terhadap layanan
dan produk.
Menjelaskan
hubungan
langsung antara
sentiment
analysis dan BI
analytics.
3 (Kauffmann et
al., 2019)
Sentiment
analysis untuk
keputusan
pemasaran
Text data
mining dan
sentiment
analysis
Ulasan online
dapat digunakan
untuk
mengevaluasi
fitur produk dan
mendukung
keputusan
pemasaran.
Mendukung
pembahasan
marketing
analytics berbasis
opini pelanggan.
4 (Nichifor et al.,
2023)
AI untuk
mengubah
review menjadi
business
enhancement
NLP, machine
learning, dan
SaaS platform
AI dan sentiment
analysis dapat
mengubah ulasan
pelanggan
menjadi masukan
peningkatan
bisnis.
Menguatkan
peran sentiment
analysis dalam
perbaikan
layanan dan
strategi bisnis.
5 (Hamed &
Madanchian,
2023)
AI dan sentiment
analysis dalam
competitive
research
Literature
review
AI meningkatkan
kemampuan
sentiment
analysis dalam
memahami opini
Mendukung
argumen bahwa
sentiment
analysis dapat
memperkuat

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

319        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

No.
Penulis dan
Tahun Fokus Penelitian
Metode/
Pendekatan Temuan Utama
Relevansi dengan
Penelitian
pelanggan dan
pesaing.
competitive
intelligence.
6 (Grande-
Ramírez et al.,
2022)
Integrasi
sentiment
analysis dalam
strategic
planning
Lexicon,
machine
learning, dan
Balanced
Scorecard
Sentiment
analysis media
sosial dapat
diintegrasikan ke
KPI dan Balanced
Scorecard.
Relevan untuk
menjelaskan
integrasi
sentiment
analysis ke dalam
BI strategis.
7 (Ciocodeică et
al., 2022)
Adopsi BI dan
sentiment
analysis sebagai
alat marketing
analytics
Kualitatif dan
kuantitatif
Sentiment
analysis
membantu
perusahaan
memahami reaksi
publik dan
konteks
pemasaran
digital.
Mendukung
hubungan antara
BI, digital
marketing, dan
analisis sentimen.
8 (Yang et al.,
2022)
Business
sentiment
analysis berbasis
news text mining
CNN-based
framework
Sentiment
analysis berita
bisnis memiliki
nilai ekonomi,
termasuk untuk
aplikasi prediksi
dan trading.
Menjelaskan
penggunaan
sentiment
analysis dalam
keputusan
ekonomi dan
bisnis.
9 (Susanto et al.,
2025)
Analisis
sentimen media
sosial untuk
UMKM
Perbandingan
dictionary-
based dan
machine
learning
Machine learning
lebih unggul dari
dictionary-based,
tetapi hybrid
framework lebih
potensial.
Relevan untuk
konteks UMKM
dan transformasi
digital berbasis
data.
10 (Lee & Anderl,
2025)
Sentimen berita
bisnis untuk
prediksi pasar
saham energi
FinBERT dan
LSTM
Sentimen isi
berita lebih
efektif daripada
headline dalam
meningkatkan
prediksi saham.
Menunjukkan
peran sentiment
analysis dalam
keputusan
finansial.
11 (Herrera-
Poyatos et al.,
2025)
Ketidakpastian
model LLM
dalam sentiment
analysis
Review LLM menghadapi
masalah
variabilitas, bias,
sensitivitas
prompt, dan
kebutuhan
explainability.
Mendukung
pembahasan
tantangan
implementasi
LLM dalam BI.
12 (Ligthart et al.,
2021)
Systematic
reviews dalam
sentiment
analysis
Tertiary study Sentiment
analysis
berkembang pesat
dengan berbagai
metode, dataset,
dan tantangan
terbuka.
Menjadi landasan
umum
perkembangan
sentiment
analysis.
13 (Cui et al.,
2023)
Evolusi metode
dan topik
Survey dan
keyword co-
occurrence
Sentiment
analysis
digunakan luas
Mendukung teori
bahwa sentiment

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

No.
Penulis dan
Tahun Fokus Penelitian
Metode/
Pendekatan Temuan Utama
Relevansi dengan
Penelitian
sentiment
analysis
dalam bisnis,
keuangan, politik,
pendidikan, dan
layanan.
analysis bersifat
multidomain.
14 (Alahmadi et
al., 2025)
Generalisasi
sentiment
analysis
Review Tantangan utama
sentiment
analysis adalah
domain
adaptation,
linguistic
diversity, dan
multimodal data.
Memperkuat
pembahasan
tantangan
generalisasi
model.
15 (Hua et al.,
2024)
Aspect-based
sentiment
analysis
Systematic
literature
review
ABSA
memberikan
analisis sentimen
yang lebih rinci
berdasarkan
aspek produk atau
layanan.
Penting untuk
menjelaskan
insight granular
dalam BI.
16 (Capuano et
al., 2021)
Sentiment
analysis untuk
CRM
Hierarchical
Attention
Networks dan
incremental
learning
Sentiment
analysis
membantu
mengukur
kepuasan,
menentukan
prioritas, dan
mempercepat
respons CRM.
Relevan untuk
pengambilan
keputusan
layanan
pelanggan.
17 (Karasenko &
Baier, 2025)
Pengukuran
technology
acceptance dari
online customer
reviews
Machine
learning dan
transformer
models
Ulasan pelanggan
dapat digunakan
untuk mengukur
konstruk TAM,
bukan hanya
polaritas
sentimen.
Menunjukkan
bahwa customer
reviews dapat
menghasilkan
insight lebih luas
dari sentimen.
18 (Mekimah et
al., 2024)
BI dalam
pengambilan
keputusan
organisasi
Bibliometric
analysis
BI berperan
penting dalam
mengubah data
menjadi
actionable
insights bagi
keputusan
organisasi.
Menjadi landasan
teori Business
Intelligence
dalam penelitian
ini.
19 (Hurbean et al.,
2025)
BI&A, data-
driven culture,
dan kinerja
manajerial
PLS-SEM Data-driven
culture
memengaruhi
adopsi BI&A,
efektivitas
keputusan, dan
kinerja
manajerial.
Relevan untuk
menjelaskan
budaya data
dalam
pengambilan
keputusan.

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

321        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

No.
Penulis dan
Tahun Fokus Penelitian
Metode/
Pendekatan Temuan Utama
Relevansi dengan
Penelitian
20 (Alawamleh et
al., 2025)
Pengaruh BI
terhadap kinerja
organisasi
SEM Kapabilitas BI,
infrastruktur BI,
dan pengalaman
pengguna BI
berpengaruh
terhadap kinerja
organisasi.
Menguatkan
peran BI dalam
peningkatan
kinerja
organisasi.
21 (Ghatora et al.,
2024)
Sentiment
analysis ulasan
produk
menggunakan
ML dan LLM
Random
Forest, Naïve
Bayes, SVM,
dan GPT-4
GPT-4 lebih baik
untuk teks kaya
konteks,
sedangkan model
tradisional efisien
untuk teks
pendek.
Mendukung
pembahasan
perkembangan
metode LLM.
22 (Ashbaugh &
Zhang, 2024)
Perbandingan
ML dan deep
learning pada
customer
reviews
CNN, RNN,
Logistic
Regression,
Random
Forest, Naïve
Bayes
ML dan deep
learning memiliki
kelebihan dan
keterbatasan
dalam mendeteksi
sentimen
pelanggan.
Relevan untuk
membandingkan
metode analisis
sentimen.
23 (Iqbal et al.,
2022)
Sentiment
analysis ulasan
konsumen
menggunakan
deep learning
Variasi LSTM Deep learning
mampu
meningkatkan
deteksi polaritas
pada data ulasan
konsumen.
Mendukung
pembahasan
metode deep
learning.
24 (Wen et al.,
2024)
Customer
sentiment dan
product
competitiveness
TF-IDF, k-
means, text
mining
Sentimen
pelanggan dapat
digunakan untuk
memahami
dimensi kualitas,
harga, layanan,
logistik, dan
loyalitas.
Relevan untuk
keputusan
peningkatan
produk dan
layanan.
25 (Wangsa et al.,
2025)
Topic-level
sentiment
analysis pada e-
grocery
BERT,
clustering, dan
GPT
Sentimen tingkat
topik membantu
mengidentifikasi
area negatif
meskipun tren
umum positif.
Menunjukkan
relevansi
sentiment
analysis untuk
bisnis digital
Indonesia.
26 (Shafiezad &
Mostofi, 2024)
Sentiment
analysis persepsi
wisatawan
terhadap kualitas
makanan
Lexicon-based
sentiment
analysis
Integrasi skor
sentimen dan
rating
memberikan
insight lebih
dalam terhadap
kualitas layanan.
Relevan untuk
pembahasan
integrasi data teks
dan rating.
27 (Saleh &
Semaan, 2024)
AI untuk
financial
sentiment
analysis
entrepreneur
ChatGPT,
LeChat-
Mistral, dan
FinBERT
Financial
sentiment
analysis dapat
digunakan untuk
memprediksi
Mendukung
perluasan
sentiment
analysis ke
bidang keuangan

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

No.
Penulis dan
Tahun Fokus Penelitian
Metode/
Pendekatan Temuan Utama
Relevansi dengan
Penelitian
keberlanjutan
entrepreneur.
dan
kewirausahaan.
28 (Saura et al.,
2019)
Indikator
keberhasilan
startup melalui
sentiment
analysis
LDA, SVM,
dan text
mining
User-generated
content dapat
digunakan untuk
mengidentifikasi
faktor
keberhasilan
startup.
Menunjukkan
peran sentiment
analysis dalam
strategi startup.
29 (Adak et al.,
2022)
Sentiment
analysis food
delivery services
Systematic
review
Banyak model
deep learning
belum
explainable,
sehingga XAI
diperlukan untuk
meningkatkan
kepercayaan.
Relevan untuk
tantangan
interpretabilitas
model.
30 (Kahya
Özyirmidokuz
et al., 2025)
Sentiment
analysis
bilingual
customer
feedback e-
commerce
ML dan
BERT
Sentiment
analysis bilingual
menghasilkan
insight merek dan
mendukung
keputusan
strategis-
operasional.
Mendukung
pembahasan
analisis sentimen
lintas bahasa dan
budaya.

Sentiment Analysis sebagai Sumber Insight dalam Business Intelligence
Hasil kajian menunjukkan bahwa sentiment analysis berperan sebagai jembatan antara
data tidak terstruktur dan Business Intelligence. Data tidak terstruktur seperti ulasan pelanggan,
komentar media sosial, berita bisnis, dan percakapan digital mengandung in formasi penting
mengenai persepsi, keluhan, harapan, dan pengalaman pelanggan. Informasi tersebut tidak
dapat sepenuhnya ditangkap melalui data numerik seperti penjualan, rating, atau jumlah
transaksi. Oleh karena itu, sentiment analysis menjadi alat penti ng untuk mengubah data teks
menjadi insight yang dapat digunakan dalam BI.
(Rokade & Aruna Kumari, 2019)  menjelaskan bahwa sentiment analysis dapat
membantu organisasi memahami suasana pasar terhadap produk dan layanan. Temuan ini
sejalan dengan (Aguilar-Moreno et al., 2024)  yang menyatakan bahwa sentiment analysis
semakin banyak digunakan dalam business decision -making karena mampu mengolah
customer feedback dari platform online menjadi informasi strategis. Dalam konteks BI, hal ini
menunjukkan bahwa sentiment analysis dapat  memperluas cakupan analisis dari data
terstruktur menuju data opini pelanggan.

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

323        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

Business Intelligence tidak hanya berfungsi sebagai alat pelaporan, tetapi juga sebagai
sistem pendukung keputusan. (Mekimah et al., 2024) menunjukkan bahwa BI memiliki peran
penting dalam mengubah data menjadi actionable insights. Namun, agar insight yang
dihasilkan lebih komprehensif, BI perlu mengintegrasikan data teks yang mencerminkan suara
pelanggan. Dengan demikian, sentiment analysis memperkuat BI karena mampu menjelaskan
alasan di balik suatu fenomena bisnis, misalnya mengapa penjualan menurun, mengapa
pelanggan tidak puas, atau mengapa reputasi merek mengalami perubahan.
Kontribusi Sentiment Analysis terhadap Pengambilan Keputusan Berbasis Data
Hasil kajian menunjukkan bahwa sentiment analysis memberikan kontribusi penting
terhadap pengambilan keputusan berbasis data, terutama pada bidang pemasaran, CRM, e -
commerce, layanan pelanggan, strategi produk, dan manajemen reputasi. (Kauffmann et al.,
2019) menunjukkan bahwa sentiment analysis terhadap ulasan online dapat membantu manajer
pemasaran mengevaluasi fitur produk berdasarkan opini pelanggan. (Wen et al., 2024)  juga
menemukan bahwa analisis sentimen terhadap ulasan online dapat mengidentifikasi dimensi
yang paling diperhatikan konsumen, seperti kualitas, rasa, kemasan, logistik, harga, layanan,
evaluasi, dan loyalitas pelanggan.
Dalam konteks customer relationship management, (Capuano et al., 2021) menunjukkan
bahwa sentiment analysis dapat digunakan untuk mengukur kepuasan pelanggan, menentukan
prioritas permintaan, mengarahkan keluhan, dan mempercepat respons organisasi. Hal ini
memperlihatkan bahwa sentiment analysis bukan hanya menghasilkan info rmasi deskriptif,
tetapi juga dapat mendukung keputusan operasional dalam pelayanan pelanggan. (Nichifor et
al., 2023)  juga menegaskan bahwa artificial intelligence dapat mengubah ulasan pelanggan
menjadi masukan peningkatan bisnis, khususnya dalam lingkungan e-commerce.
Selain itu, sentiment analysis juga mendukung keputusan strategis. (Grande-Ramírez et
al., 2022)  menunjukkan bahwa sentiment analysis media sosial dapat diintegrasikan dalam
strategic planning dan Balanced Scorecard. Dengan pendekatan tersebut, opini pelanggan dapat
dikaitkan dengan key performance indicators, sehingga organisasi dapat menghubungkan
persepsi pelanggan dengan tujuan strategis. (Hurbean et al., 2025)  juga menegaskan bahwa
data-driven culture dan penggunaan BI&A berpengaruh terhadap efektivitas pengambilan
keputusan dan kinerja manajerial. Artinya, manfaat sentiment analysis akan lebih optimal
apabila organisasi memiliki budaya kerja yang mendukung pen ggunaan data dalam proses
pengambilan keputusan.

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

Perkembangan Metode Sentiment Analysis dalam Mendukung BI
Literatur yang dikaji menunjukkan bahwa metode sentiment analysis berkembang dari
pendekatan berbasis leksikon, machine learning, deep learning, transformer, hingga Large
Language Models. Pada pendekatan awal, model berbasis leksikon banyak digunakan karen a
mudah dipahami dan lebih sederhana. Namun, pendekatan ini memiliki keterbatasan dalam
menangkap konteks, sarkasme, bahasa informal, dan variasi budaya. (Susanto et al., 2025)
menemukan bahwa pendekatan dictionary -based lebih sederhana dan interpretatif, tetapi
kurang akurat dalam memproses bahasa informal dan lokal, sedangkan machine learning
memiliki kinerja yang lebih baik dengan kebutuhan praproses yang lebih kompleks.
Pendekatan machine learning dan deep learning kemudian banyak digunakan untuk
meningkatkan akurasi klasifikasi sentimen. (Ashbaugh & Zhang, 2024) menunjukkan bahwa
model machine learning dan deep learning memiliki kelebihan dan keterbatasan masing -
masing dalam menganalisis customer reviews. (Iqbal et al., 2022)  menegaskan bahwa deep
learning, khususnya variasi LSTM, dapat meningkatkan performa analisis sentimen pada
ulasan konsumen. Perkembangan ini menunjukkan bahwa BI modern dapat memanfaatkan
metode yang lebih adaptif dalam mengolah data opini pelanggan.
Dalam perkembangan terbaru, LLM dan transformer memberikan peluang lebih besar
untuk analisis sentimen yang lebih kontekstual. (Ghatora et al., 2024)  menunjukkan bahwa
GPT-4 mampu menangkap sentimen campuran dan memberikan penjelasan yang lebih
informatif pada teks yang kaya konteks. (Wangsa et al., 2025)  mengembangkan topic -level
sentiment analysis berbasis BERT, clustering, dan GPT pada ulasan e -grocery, yang
menunjukkan bahwa analisis sentimen tidak hanya dapat dilakukan pada tingkat dokumen,
tetapi juga pada tingkat topik. (Kahya Özyirmidokuz et al., 2025)  juga menunjukkan bahwa
BERT dapat digunakan untuk analisis sentimen bilingual, meskipun validasi manusia tetap
diperlukan karena terdapat perbedaan antara label otomatis dan akurasi label manusia.
Selain analisis sentimen umum, aspect -based sentiment analysis juga memiliki nilai
penting dalam BI. (Hua et al., 2024) menjelaskan bahwa ABSA dapat mengidentifikasi aspek
dan opini terkait dari suatu teks secara lebih rinci. Hal ini sangat penting bagi organisasi karena
pelanggan dapat memberikan sentimen positif terhadap satu aspek produk, tetapi negatif
terhadap aspek l ain. Dengan ABSA, perusahaan dapat mengetahui aspek mana yang perlu
dipertahankan dan aspek mana yang harus diperbaiki.
Customer Reviews, Marketing Analytics, dan Competitive Intelligence
Hasil kajian menunjukkan bahwa customer reviews merupakan salah satu sumber data
utama dalam sentiment analysis untuk BI. Ulasan pelanggan tidak hanya berisi penilaian positif

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

325        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

atau negatif, tetapi juga memuat informasi mengenai kebutuhan, pengalaman, keluhan, dan
harapan konsumen. Dalam konteks marketing analytics, data tersebut dapat digunakan untuk
mengevaluasi produk, mengukur kepuasan, memahami perilaku pelanggan, serta mene ntukan
strategi pemasaran.
(Kauffmann et al., 2019) menunjukkan bahwa user-generated content merupakan sumber
big data yang memiliki nilai strategis dalam keputusan pemasaran. Dengan sentiment analysis,
perusahaan dapat memperoleh skor sentimen terhadap fitur produk dan menggunakannya
untuk menyusun strate gi positioning. (Ciocodeică et al., 2022)  juga menunjukkan bahwa
sentiment analysis dapat digunakan sebagai alat marketing analytics karena mampu
memberikan gambaran reaksi publik terhadap produk, layanan, atau merek dalam lingkungan
digital. Dengan demikian, sentiment analysis dapat memperkuat p roses pemasaran yang
berbasis data.
Sentiment analysis juga mendukung competitive intelligence. (Hamed & Madanchian,
2023) menjelaskan bahwa AI -powered sentiment analysis dapat digunakan untuk memahami
bagaimana pelanggan menilai pesaing, sehingga organisasi dapat mengidentifikasi kekuatan
dan kelemahan kompetitor. (Wen et al., 2024)  juga menunjukkan bahwa sentiment analysis
dapat digunakan untuk mengukur product competitiveness melalui dimensi -dimensi yang
muncul dalam ulasan pelanggan. Hal ini menunjukkan bahwa sentiment analysis tidak hanya
berguna untuk memahami pelanggan internal  perusahaan, tetapi juga untuk memantau posisi
kompetitif di pasar.
Tantangan Implementasi Sentiment Analysis dalam BI
Meskipun sentiment analysis memiliki manfaat besar, hasil kajian menunjukkan bahwa
implementasinya masih menghadapi berbagai tantangan. Tantangan pertama adalah kualitas
data. Data dari media sosial dan customer reviews sering kali mengandung bahasa tidak baku,
singkatan, salah ketik, emoji, bahasa campuran, dan konteks budaya tertentu. (Yang et al.,
2022) menjelaskan bahwa algoritma machine learning masih mengalami kesulitan dalam
mengenali makna ganda, lelucon, dan variasi struktur bahasa.
Tantangan kedua adalah generalisasi model. (Alahmadi et al., 2025) menunjukkan bahwa
sentiment analysis masih menghadapi tantangan domain adaptation, linguistic diversity, dan
perubahan pola komunikasi digital. Model yang baik pada satu domain belum tentu memiliki
kinerja yang sama pada domain lain. Hal ini sejalan dengan (Hua et al., 2024) yang menemukan
adanya masalah keberagaman domain dan dataset dalam penelitian ABSA.
Tantangan ketiga adalah interpretabilitas dan explainability. (Adak et al., 2022)
menunjukkan bahwa banyak model deep learning dalam sentiment analysis bersifat tidak

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

mudah diinterpretasikan, sehingga organisasi membutuhkan explainable artificial intelligence
untuk meningkatkan kepercayaan terhadap hasil analisis. (Herrera-Poyatos et al., 2025)  juga
menjelaskan bahwa LLM menghadapi masalah ketidakpastian, variasi hasil, sensitivitas
prompt, dan bias data pelatihan. Oleh karena itu, organisasi tidak boleh menggunakan hasil
sentiment analysis secara mekanis tanpa validasi dan interpretasi manajerial.
Tantangan keempat adalah integrasi ke dalam BI. Sentiment analysis akan lebih
bermanfaat apabila hasilnya tidak berdiri sendiri, tetapi dihubungkan dengan dashboard BI,
indikator kinerja, laporan manajerial, dan sistem pendukung keputusan. (Grande-Ramírez et
al., 2022) menunjukkan bahwa integrasi sentiment analysis ke dalam Balanced Scorecard dapat
membantu mengarahkan opini pelanggan pada KPI organisasi. Dengan demikian, tantangan
utama bukan hanya menghasilkan klasifikasi sentimen, tetapi juga mengubah hasil analisis
menjadi insight yang dapat ditindaklanjuti.
Sintesis Pembahasan
Berdasarkan hasil kajian terhadap 30 artikel rujukan, dapat disintesis bahwa sentiment
analysis memiliki tiga peran utama dalam Business Intelligence dan pengambilan keputusan
berbasis data. Pertama, sentiment analysis berperan sebagai alat ekstraksi insight dari data tidak
terstruktur. Data berupa customer reviews, komentar media sosial, berita bisnis, dan user -
generated content dapat diubah menjadi informasi mengenai persepsi pelanggan, kualitas
layanan, reputasi merek, dan daya saing produk.
Kedua, sentiment analysis berperan sebagai penguat Business Intelligence modern. BI
tradisional banyak mengandalkan data numerik, sedangkan sentiment analysis menambahkan
dimensi kualitatif berupa opini, emosi, dan pengalaman pelanggan. Integrasi keduanya
memungkinkan organisasi memahami apa yang terjadi melalui data kuantitatif dan mengapa
hal tersebut terjadi melalui data sentimen.
Ketiga, sentiment analysis berperan dalam mendukung pengambilan keputusan berbasis
data. Hasil analisis sentimen dapat digunakan untuk keputusan pemasaran, pengembangan
produk, manajemen layanan pelanggan, CRM, competitive intelligence, strategic planning,
serta pengelolaan reputasi. Namun, efektivitas pemanfaatan sentiment analysis sangat
bergantung pada kualitas data, pemilihan metode analisis, validasi hasil, explainability model,
serta kesiapan organisasi dalam membangun data-driven culture.
Dengan demikian, sentiment analysis dapat dipahami sebagai komponen penting dalam
ekosistem Business Intelligence modern. Peran tersebut semakin kuat seiring berkembangnya
machine learning, deep learning, transformer, dan Large Language Models. Meskipun
demikian, organisasi tetap perlu berhati -hati dalam menginterpretasikan hasil analisis karena

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

327        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

sentimen pelanggan bersifat kontekstual, dinamis, dan dipengaruhi oleh bahasa, budaya,
domain, serta kualitas data. Oleh karena itu, integrasi sentiment analysis ke dalam BI perlu
dilakukan secara sistematis agar hasilnya benar -benar dapat mendukung pengam bilan
keputusan yang objektif, responsif, dan berbasis data.

5. KESIMPULAN DAN SARAN
Berdasarkan hasil narrative literature review terhadap 30 artikel rujukan, dapat
disimpulkan bahwa sentiment analysis berperan penting dalam memperkuat Business
Intelligence dan pengambilan keputusan berbasis data. Sentiment analysis mampu mengolah
data tidak terstruktur, seperti ulasan pelanggan, komentar media sosial, berita bisnis, dan user-
generated content menjadi informasi strategis mengenai persepsi, kepuasan, keluhan, serta
kebutuhan pelanggan. Integrasi sentiment analysis ke dalam Business Intellig ence membuat
organisasi tidak hanya memahami apa yang terjadi melalui data numerik, tetapi juga
memahami alasan di balik perilaku pelanggan melalui opini dan emosi yang terekam dalam
data teks.
Sentiment analysis dapat dimanfaatkan dalam berbagai bidang, seperti pemasaran,
customer relationship management, e-commerce, competitive intelligence, strategic planning,
pengembangan produk, layanan pelanggan, keuangan, dan kewirausahaan. Perkembangan
metode berbasis leksikon, machine learning, deep learning, transformer, dan Large Language
Models semakin memperkuat kemampuan analisis sentimen dalam menghasilkan insight
bisnis. Namun, penerapannya masih menghadapi tantangan, seperti kualitas data, bahasa
informal, sarkasme, bias algoritma, keterbatasan dataset, rendahnya interpretabilitas model,
serta kebutuhan validasi manusia.
Organisasi disarankan untuk mengintegrasikan sentiment analysis ke dalam sistem
Business Intelligence, membangun data-driven culture, meningkatkan literasi data manajerial,
serta menggunakan metode analisis yang sesuai dengan karakteristik data dan kebutuh an
bisnis. Penelitian selanjutnya disarankan untuk menguji integrasi sentiment analysis dalam
dashboard Business Intelligence pada sektor tertentu, seperti UMKM, e-commerce, perbankan,
pendidikan, pariwisata, atau layanan publik. Selain itu, penelitian men datang perlu
membandingkan efektivitas berbagai metode sentiment analysis, khususnya pada data
berbahasa Indonesia, serta memperhatikan aspek etika, privasi, bias algoritma, dan explainable
artificial intelligence.

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

DAFTAR REFERENSI
Adak, A., Pradhan, B., & Shukla, N. (2022). Sentiment Analysis of Customer Reviews of Food
Delivery Services Using Deep Learning and Explainable Artificial Intelligence:
Systematic Review. Foods, 11(10), 1–16. https://doi.org/10.3390/foods11101500
Aguilar-Moreno, J. A., Palos-Sanchez, P. R., & Pozo-Barajas, R. (2024). Sentiment analysis to
support business decision -making. A bibliometric study. AIMS Mathematics , 9(2),
4337–4375. https://doi.org/10.3934/math.2024215
Alahmadi, K., Alharbi, S., Chen, J., & Wang, X. (2025). Generalizing Sentiment Analysis: a
Review of Progress, Challenges, and Emerging Directions. Social Network Analysis
and Mining, 15(1), 1–28. https://doi.org/10.1007/s13278-025-01461-8
Alawamleh, H. A. M., Alshweesh, R. G., Abu-darwish, N. J. S., Aljundi, A. hussein, & Salah,
A. A. (2025). Influence of Business Intelligence on Organizational Performance: The
Moderating Role of Employee BI Experiences. Administrative Sciences, 16(2), 1–17.
https://doi.org/10.3390/admsci16020100
Ashbaugh, L., & Zhang, Y. (2024). A Comparative Study of Sentiment Analysis on Customer
Reviews Using Machine Learning and Deep Learning. Computers, 13(12), 1 –16.
https://doi.org/10.3390/computers13120340
Capuano, N., Greco, L., Ritrovato, P., & Vento, M. (2021). Sentiment Analysis for Customer
Relationship Management: an Incremental Learning Approach. Applied Intelligence,
51(6), 3339–3352. https://doi.org/10.1007/s10489-020-01984-x
Ciocodeică, D. F., Chivu, R. G. P., Popa, I. C., Mihălcescu, H., Orzan, G., & Băjan, A. M. D.
(2022). The Degree of Adoption of Business Intelligence in Romanian Companies —
The Case of Sentiment Analysis as a Marketing Analytical Tool. Sustainability
(Switzerland), 14(12), 1–20. https://doi.org/10.3390/su14127518
Cui, J., Wang, Z., Ho, S. B., & Cambria, E. (2023). Survey on Sentiment Analysis: Evolution
of Research Methods and Topics. In Artificial Intelligence Review (Vol. 56, Issue 8).
Springer Netherlands. https://doi.org/10.1007/s10462-022-10386-z
Ghatora, P. S., Hosseini, S. E., Pervez, S., Iqbal, M. J., & Shaukat, N. (2024). Sentiment
Analysis of Product Reviews Using Machine Learning and Pre -Trained LLM. Big
Data and Cognitive Computing, 8(12), 1–18. https://doi.org/10.3390/bdcc8120199
Grande-Ramírez, J. R., Roldán -Reyes, E., Aguilar -Lasserre, A. A., & Juárez -Martínez, U.
(2022). Integration of Sentiment Analysis of Social Media in the Strategic Planning
Process to Generate the Balanced Scorecard. Applied Sciences (Switzerland), 12(23),
1–19. https://doi.org/10.3390/app122312307
Hamed, T., & Madanchian, M. (2023). Artificial Intelligence and Sentiment Analysis : A
Review in Competitive Research. Computers 2023, 12, 37. , 12(37), 1 –15.
https://doi.org/https:// doi.org/10.3390/computers12020037
Herrera-Poyatos, D., Peláez -González, C., Zuheros, C., Herrera -Poyatos, A., Tejedor, V.,
Herrera, F., & Montes, R. (2025). An Overview of Model Uncertainty and Variability
in LLM-based Sentiment Analysis: Challenges, Mitigation Strategies, and the Rof
Explainability. Frontiers in Artificial Intelligence , 8(August), 1 –24.
https://doi.org/10.3389/frai.2025.1609097
Hua, Y. C., Denny, P., Wicker, J., & Taskova, K. (2024). A Systematic Review of Aspect -
based Sentiment Analysis: Domains, Methods, and Trends. In Artificial Intelligence

Peran Sentiment Analysis dalam Business Intelligence dan Pengambilan Keputusan Berbasis Data

329        JUPITER – VOLUME 3, NOMOR 4. JULI 2025

Review (Vol. 57, Issue 11). Springer Netherlands. https://doi.org/10.1007/s10462 -
024-10906-z
Hurbean, L., Militaru, F., Munteanu, V. P., Danaiata, D., Fotache, D., & Muntean, M. (2025).
Assessing the Influence of Business Intelligence and Analytics and Data -Driven
Culture on Managerial Performance: Evidence from Romania. Systems, 13(1), 1–20.
https://doi.org/10.3390/systems13010002
Iqbal, A., Amin, R., Iqbal, J., Alroobaea, R., Binmahfoudh, A., & Hussain, M. (2022).
Sentiment Analysis of Consumer Reviews Using Deep Learning. Sustainability
(Switzerland), 14(17), 1–19. https://doi.org/10.3390/su141710844
Kahya Özyirmidokuz, E., Molu Elmas, B., & Stoica, E. A. (2025). AI -Based Sentiment
Analysis of E-Commerce Customer Feedback: A Bilingual Parallel Study on the Fast
Food Industry in Turkish and English. Journal of Theoretical and Applied Electronic
Commerce Research , 20(4), 1–34. https://doi.org/10.3390/jtaer20040294
Karasenko, A., & Baier, D. (2025). Beyond Sentiment Analysis of Online Customer Reviews:
an Approach to Automated Measurement of Technology Acceptance from Online
Customer Reviews. In Journal of Business Economics  (Vol. 95, Issue 7). Springer
Berlin Heidelberg. https://doi.org/10.1007/s11573-025-01232-z
Kauffmann, E., Peral, J., Gil, D., Ferrández, A., Sellers, R., & Mora, H. (2019). Managing
Marketing Decision -making with Sentiment Analysis: An Evaluation of the Main
Product Features Using Text Data Mining. Sustainability (Switzerland), 11(15), 1–19.
https://doi.org/10.3390/su11154235
Lee, C. Y., & Anderl, E. (2025). Does Business News Sentiment Matter in the Energy Stock
Market? Adopting Sentiment Analysis for Short-term Stock Market Prediction in the
Energy Industry. Frontiers in Artificial Intelligence , 8(July), 1 –6.
https://doi.org/10.3389/frai.2025.1559900
Ligthart, A., Catal, C., & Tekinerdogan, B. (2021). Systematic Reviews in Sentiment Analysis:
a Tertiary Study. In Artificial Intelligence Review  (Vol. 54, Issue 7). Springer
Netherlands. https://doi.org/10.1007/s10462-021-09973-3
Mekimah, S., Zighed, R., Mili, K., & Bengana, I. (2024). Business Intelligence in
Organizational Decision -making: a Bibliometric Analysis of Research Trends and
Gaps (2014 –2024). Discover Sustainability , 5(1), 1 –18.
https://doi.org/10.1007/s43621-024-00692-7
Moleong, L. J. (2017). Metodologi Penelitian Kualitatif. Remaja Rosdakarya.
Nichifor, E., Brătucu, G., Chițu, I. B., Lupșa -Tătaru, D. A., Chișinău, E. M., Todor, R. D.,
Albu, R. G., & Bălășescu, S. (2023). Utilising Artificial Intelligence to Turn Reviews
into Business Enhancements through Sentiment Analysis. Electronics (Switzerland),
12(21), 1–19. https://doi.org/https://doi.org/10.3390/electronics12214538
Rokade, P. P., & Aruna Kumari, D. (2019). Business Intelligence Analytics Using Sentiment
Analysis-a Survey. International Journal of Electrical and Computer Engineering ,
9(1), 613–620. https://doi.org/10.11591/ijece.v9i1.pp613-620
Saleh, L., & Semaan, S. (2024). The Potential of AI in Performing Financial Sentiment
Analysis for Predicting Entrepreneur Survival. Administrative Sciences, 14(9), 1–12.
https://doi.org/10.3390/admsci14090220
Saura, J. R., Palos -Sanchez, P., & Grilo, A. (2019). Detecting indicators for startup business

e-ISSN: 3031-349X; p-ISSN: 3031-500X, Hal 310-330

success: Sentiment analysis using text data mining. Sustainability (Switzerland) ,
11(3), 1–14. https://doi.org/10.3390/su11030917
Shafiezad, O., & Mostofi, H. (2024). Sentiment Analysis of Berlin Tourists’ Food Quality
Perception Through Artificial Intelligence. Tourism and Hospitality, 5(4), 1396–1417.
https://doi.org/10.3390/tourhosp5040078
Solechan, A., & Abidin, R. (2024). Implementasi Teknologi Blockchain dalam Digital
Marketing. Jurnal Informatika Upgris , 10(2), 23 –28.
https://doi.org/10.26877/jiu.v10i2.21002
Solechan, A., Wijanarko, T. A., & Hartono, B. (2023). Transformasi Digital Pada UMKM
Dalam Meningkatkan Daya Saing Pasar. Jurnal Informatika UPGRIS, 9(1), 7–12.
Sugiyono. (2019). Metodelogi Penelitian Kuantitatif dan Kualitatif Dan R&D. Alfabeta.
Susanto, H., Omar, A. S., Shafa Susanto, A. K., Setiana, D., Fang-Yie, L., Shaikh, J. M., Insani,
A., Khusni, U., Hidayat, R., Akbari, I., & Basuki, I. (2025). Toward Robust Social
Media Sentiment for SMEs: a Comparative Study of Dictionary -based and Machine
Learning Approaches with Insights for Hybrid Methodologies. Frontiers in Big Data,
8(April), 1–21. https://doi.org/10.3389/fdata.2025.1594374
Wangsa, J. I. P., Agung, Y. J., Rahmi, S. R., Murfi, H., Hariadi, N., Nurrohmah, S., Satria, Y.,
& Za’in, C. (2025). Large Language Model -Based Topic-Level Sentiment Analysis
for E-Grocery Consumer Reviews. Big Data and Cognitive Computing , 9(8), 1–19.
https://doi.org/10.3390/bdcc9080194
Wen, Z., Chen, Y., Liu, H., & Liang, Z. (2024). Text Mining Based Approach for Customer
Sentiment and Product Competitiveness Using Composite Online Review Data.
Journal of Theoretical and Applied Electronic Commerce Research , 19(3), 1776 –
1792. https://doi.org/10.3390/jtaer19030087
Yang, M., Jiang, B., Wang, Y., Hao, T., & Liu, Y. (2022). News Text Mining-Based Business
Sentiment Analysis and Its Significance in Economy. Frontiers in Psychology ,
13(July), 1–7. https://doi.org/10.3389/fpsyg.2022.918447
