# Football Analysis

Project analisis video pertandingan sepak bola menggunakan computer vision. Pipeline ini mendeteksi dan melacak pemain, wasit, serta bola, kemudian menambahkan informasi tim, penguasaan bola, pergerakan kamera, posisi lapangan, kecepatan, dan jarak pemain ke video keluaran.

## Fitur

- Deteksi objek menggunakan model YOLO dari Ultralytics.
- Pelacakan pemain dan objek menggunakan ByteTrack melalui `supervision`.
- Pengelompokan pemain menjadi dua tim berdasarkan warna jersey.
- Estimasi pemain yang sedang menguasai bola.
- Interpolasi posisi bola yang tidak terdeteksi pada frame tertentu.
- Estimasi pergerakan kamera.
- Transformasi posisi ke koordinat lapangan.
- Perhitungan kecepatan dan jarak pemain.
- Penambahan anotasi ke video hasil analisis.

## Persyaratan

- Windows, macOS, atau Linux
- Python 3.10 atau lebih baru
- Model YOLO yang kompatibel dengan kelas `player`, `referee`, dan `ball`
- Dependensi Python:

```text
ultralytics
supervision
opencv-python
numpy
pandas
scikit-learn
```

## Instalasi

Buat dan aktifkan virtual environment. Contoh pada Windows PowerShell:

```powershell
python -m venv cv_env
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\cv_env\Scripts\Activate.ps1
```

Install dependensi:

```powershell
python -m pip install --upgrade pip
pip install ultralytics supervision opencv-python numpy pandas scikit-learn
```

Jika virtual environment sudah tersedia di folder `cv_env`, cukup aktifkan environment tersebut dan pastikan dependensinya sudah terpasang.

## Struktur Project

```text
football_analysis/
├── main.py                         # Entry point pipeline analisis
├── yolo_inference.py               # Inferensi YOLO sederhana
├── models/
│   ├── best.pt                     # Model utama yang digunakan main.py
│   └── last.pt                     # Model alternatif/checkpoint
├── input_videos/                   # Video input
├── output_videos/                  # Video hasil analisis
├── stubs/                          # Cache hasil tracking/pergerakan kamera
├── trackers/                       # Deteksi, tracking, dan anotasi
├── team_assigner/                  # Identifikasi tim berdasarkan warna jersey
├── player_ball_assigner/           # Penentuan pemain yang menguasai bola
├── camera_movement_estimator/      # Estimasi pergerakan kamera
├── view_transformer/               # Transformasi posisi ke bidang lapangan
├── speed_and_distance_estimator/   # Estimasi kecepatan dan jarak
└── utils/                          # Fungsi baca dan simpan video
```

## Menjalankan Analisis

1. Letakkan video input di `input_videos/`.
2. Pastikan file model tersedia di `models/best.pt`.
3. Sesuaikan nama video pada `main.py` jika nama file berbeda dari `08fd33_4.mp4`.
4. Jalankan pipeline:

```powershell
python main.py
```

Video hasil akan disimpan sebagai:

```text
output_videos/output.avi
```

### Menggunakan Inferensi YOLO Saja

Untuk menjalankan prediksi YOLO tanpa pipeline tracking dan anotasi lengkap:

```powershell
python yolo_inference.py
```

Hasil prediksi akan dibuat oleh Ultralytics di dalam folder `runs/`.

## Stub dan Cache

`main.py` dapat membaca hasil tracking dan estimasi pergerakan kamera dari folder `stubs/` agar proses berikutnya lebih cepat. Jika stub tidak tersedia, pipeline akan menghitung ulang hasil tersebut dan menyimpannya ketika path stub diberikan.

Stub harus sesuai dengan video input yang sedang diproses. Menggunakan stub dari video berbeda dapat menghasilkan anotasi yang tidak akurat.

## Catatan

- Folder `models/`, `input_videos/`, dan `output_videos/` harus berada di root project ketika menjalankan `python main.py`.
- Model `models/best.pt` harus memiliki nama kelas yang diharapkan oleh tracker: `player`, `goalkeeper`, `referee`, dan `ball`.
- Pemrosesan video dapat membutuhkan waktu dan memori cukup besar, terutama ketika stub belum tersedia.
