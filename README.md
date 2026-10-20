# Studi Kasus 5: Human Computer Interaction and Data Visualization

## Deskripsi
Evaluasi usability aplikasi dengan System Usability Scale (SUS) pada 12 responden sintetis, rata-rata skor sekitar 67, sedikit di bawah benchmark 68. Visualisasi memakai palet Okabe-Ito yang aman untuk buta warna, judul berupa temuan, dan garis acuan, sesuai prinsip HCI: kurangi beban kognitif dan jangan mengandalkan warna saja.

## Cara menjalankan
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
Grafik tersimpan di folder `outputs/`.

## Catatan
Data pada proyek ini sintetis atau bawaan library agar bisa dijalankan tanpa dataset eksternal. Kesimpulan substantif perlu divalidasi dengan data nyata.
