# Klasifikasi Penyakit Kuku (Nail Disease Classification)

Proyek ini adalah aplikasi web berbasis Flask yang memanfaatkan model *Deep Learning* (TensorFlow/Keras) untuk mengklasifikasikan kondisi atau penyakit pada kuku manusia berdasarkan unggahan gambar. 

Aplikasi ini mampu mendeteksi dan mengklasifikasikan 3 kondisi kuku, yaitu:
1. **Healthy** (Kuku Sehat)
2. **Onychomycosis** (Infeksi Jamur Kuku)
3. **Psoriasis** (Psoriasis Kuku)

## Fitur
* **Antarmuka Web Sederhana**: Pengguna dapat mengunggah gambar kuku langsung melalui browser untuk dianalisis.
* **Prediksi Real-time**: Memproses gambar dan memberikan hasil prediksi beserta persentase tingkat kepercayaan (*confidence score*).
* **REST API Endpoint**: Menyediakan endpoint API (`/predict`) sehingga dapat diintegrasikan dengan aplikasi klien lainnya (seperti Mobile App atau platform pihak ketiga).

## Teknologi yang Digunakan
* **Backend**: Python 3, Flask
* **Machine Learning**: TensorFlow & Keras (Model dalam format `.keras`)
* **Image Processing**: Pillow (PIL), NumPy
* **Frontend**: HTML, CSS, JavaScript (berada di dalam direktori `templates`)

## Persyaratan (Prerequisites)
Pastikan komputer/sistem Anda sudah memiliki:
* [Python 3.8+](https://www.python.org/downloads/)
* `pip` (Python package manager)

## Panduan Instalasi & Persiapan

1. **Unduh atau Clone Repositori Ini:**
   Buka terminal atau command prompt, lalu masuk ke direktori proyek ini.
   ```bash
   cd "Klasifikasi Penyakit Kuku"
   ```

2. **Buat Virtual Environment (Sangat Disarankan):**
   ```bash
   python -m venv venv
   
   # Aktivasi di Windows:
   venv\Scripts\activate
   
   # Aktivasi di macOS/Linux:
   source venv/bin/activate
   ```

3. **Instal Library/Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Pastikan koneksi internet stabil karena proses pengunduhan package TensorFlow memakan cukup banyak data).*

## Cara Menjalankan Aplikasi

1. Pastikan Anda berada di root direktori proyek.
2. Jalankan skrip utama `app.py`:
   ```bash
   python app.py
   ```
3. Jika berhasil, server lokal Flask akan berjalan. Buka browser web Anda dan kunjungi URL berikut:
   ```
   http://127.0.0.1:5000/
   ```

## Struktur Direktori

```text
Klasifikasi Penyakit Kuku/
├── app.py                      # Script utama server Flask dan logika backend
├── nail_disease_model.keras    # Model deep learning (TensorFlow/Keras) yang siap pakai
├── requirements.txt            # Daftar pustaka Python yang dibutuhkan
├── README.md                   # File dokumentasi (file ini)
└── templates/
    └── index.html              # Template halaman web frontend
```

## Dokumentasi API

Anda dapat melakukan inferensi langsung tanpa melalui tampilan web dengan memanggil endpoint API secara *programmatic* (misalnya menggunakan Postman atau modul `requests` di Python).

**Endpoint URL:** `/predict`
**Method:** `POST`
**Body (form-data):** `file` (Isi dengan file gambar berupa JPG/PNG/JPEG)

**Contoh Response Sukses:**
```json
{
  "class": "onychomycosis",
  "confidence": 99.4523
}
```

**Contoh Response Gagal:**
```json
{
  "error": "Tidak ada file yang diunggah"
}
```

## Catatan
* Model akan melakukan *resize* gambar secara otomatis menjadi `224x224` pixel sebelum proses inferensi.
* Untuk tingkat akurasi yang lebih optimal, usahakan mengunggah foto dengan fokus pencahayaan dan resolusi yang jelas pada area kuku.
