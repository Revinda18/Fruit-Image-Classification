<h1 align="center">Fruit Image Classification 🍎🍌🍇</h1>

<p align="center">
  <img src="assets/fruit_banner.jpg" alt="Fruit Banner" width="400"/>
</p>

---

## 🎯 Deskripsi Proyek
Proyek ini bertujuan untuk membangun sistem klasifikasi gambar buah menggunakan tiga model:  
1. **CNN Base (Non-Pretrained)**  
2. **Pretrained Model 1 (EfficientNetB0)**  
3. **Pretrained Model 2 (ResNet50)**  

Tujuan: membandingkan performa ketiga model dan membuat demo aplikasi interaktif dengan Streamlit.

---

## 📊 Dataset dan Preprocessing
- Dataset: gambar buah dari beberapa kelas: Apple, Banana, Grapes, Orange, Strawberry.  
- Preprocessing:  
  - Resize gambar (96x96 untuk CNN Base, sesuai model pretrained)  
  - Normalisasi pixel ke rentang 0–1  
  - Data augmentation: rotation, flipping, zoom, brightness adjustment

---

## 🧠 Model yang Digunakan
1. **CNN Base (96x96)** – CNN sederhana tanpa pretrained weights  
2. **Pretrained Model 1 (EfficientNetB0)** – transfer learning dari ImageNet  
3. **Pretrained Model 2 (ResNet50)** – transfer learning dari ImageNet, fine-tuning beberapa layer terakhir  

---

## 📈 Evaluasi Model

### 1️⃣ CNN Base (96x96)
| Class       | Precision | Recall | F1-score | Support |
|------------|-----------|--------|----------|--------|
| Apple      | 0.91      | 0.84   | 0.87     | 434    |
| Banana     | 0.88      | 0.94   | 0.91     | 461    |
| Grapes     | 0.86      | 0.86   | 0.86     | 434    |
| Orange     | 0.97      | 0.91   | 0.94     | 394    |
| Strawberry | 0.92      | 0.98   | 0.95     | 406    |
| **Accuracy** |         |        | 0.90     | 2129   |

**Analisis:**  
- Akurasi keseluruhan: 0.90  
- Recall Apple lebih rendah (0.84) → model kadang salah mengklasifikasikan Apple.  
- Cocok untuk dataset kecil, training cepat.

---

### 2️⃣ Pretrained Model 1 (EfficientNetB0)
| Class       | Precision | Recall | F1-score | Support |
|------------|-----------|--------|----------|--------|
| Apple      | 0.93      | 0.90   | 0.91     | 434    |
| Banana     | 0.91      | 0.95   | 0.93     | 461    |
| Grapes     | 0.89      | 0.88   | 0.88     | 434    |
| Orange     | 0.98      | 0.93   | 0.95     | 394    |
| Strawberry | 0.94      | 0.99   | 0.96     | 406    |
| **Accuracy** |         |        | 0.92     | 2129   |

**Analisis:**  
- Akurasi meningkat dibanding CNN Base (0.92).  
- Transfer learning membantu model mengenali fitur buah lebih baik.  
- F1-score merata di semua kelas.

---

### 3️⃣ Pretrained Model 2 (ResNet50)
| Class       | Precision | Recall | F1-score | Support |
|------------|-----------|--------|----------|--------|
| Apple      | 0.94      | 0.92   | 0.93     | 434    |
| Banana     | 0.92      | 0.96   | 0.94     | 461    |
| Grapes     | 0.90      | 0.90   | 0.90     | 434    |
| Orange     | 0.99      | 0.94   | 0.96     | 394    |
| Strawberry | 0.95      | 0.99   | 0.97     | 406    |
| **Accuracy** |         |        | 0.94     | 2129   |

**Analisis:**  
- Akurasi tertinggi (0.94) dan F1-score terbaik.  
- Model lebih besar → training lebih lambat tapi performa sangat baik.  
- Cocok untuk implementasi nyata.

---

### Grafik Loss & Accuracy
![Loss & Accuracy](notebooks/plots/loss_acc.png)  
*(Contoh: grafik diambil dari notebook evaluasi)*

---

### Confusion Matrix
![Confusion Matrix CNN Base](notebooks/plots/confusion_cnn.png)  
![Confusion Matrix Pretrained 1](notebooks/plots/confusion_effnet.png)  
![Confusion Matrix Pretrained 2](notebooks/plots/confusion_resnet.png)  

---

## 🚀 Panduan Menjalankan Sistem Website (Streamlit)
1. Install dependencies:
```bash
pip install -r requirements.txt
