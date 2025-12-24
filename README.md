# FRUIT IMAGE CLASSIFICATION 🍎🍌🍇

<p align="center">
  <img src="asets/fruit_banner.png.png" alt="Fruit Banner" width="400"/>
</p>

---

## 📌 PROJECT OVERVIEW

This repository contains a **Fruit Image Classification** system built using Deep Learning. The project compares the performance of three models:

1. **CNN Base (Non-Pretrained)**
2. **EfficientNetB0 (Pretrained)**
3. **ResNet50 (Pretrained)**

The best-performing model is deployed as an interactive **Streamlit web application** for real-time fruit image classification.

---

## 🎯 OBJECTIVES

* Build an image classification model for fruit images
* Compare non-pretrained and pretrained deep learning models
* Evaluate model performance using accuracy, precision, recall, and F1-score
* Deploy an interactive web-based demo using Streamlit

---

## 📊 DATASET

**Classes:**

* Apple
* Banana
* Grapes
* Orange
* Strawberry

**Preprocessing Steps:**

* Image resizing

  * 96×96 (CNN Base)
  * 224×224 (Pretrained Models)
* Pixel normalization (0–1)
* Data augmentation (rotation, flip, zoom, brightness)

---

## 🧠 MODELS USED

### 1️⃣ CNN BASE (96×96)

* Built from scratch using Keras
* Lightweight and fast training
* Suitable for small datasets

**Pros:**

* Fast training
* Simple architecture

**Cons:**

* Lower accuracy compared to pretrained models

---

### 2️⃣ EFFICIENTNETB0 (PRETRAINED)

* Pretrained on ImageNet
* Transfer learning applied

**Pros:**

* Efficient architecture
* Potential for high accuracy

**Cons:**

* Poor performance due to training/preprocessing issues
* Requires further tuning

---

### 3️⃣ RESNET50 (PRETRAINED)

* Pretrained on ImageNet
* Fine-tuned for fruit classification

**Pros:**

* Highest accuracy
* Stable and reliable performance

**Cons:**

* Larger model size
* Higher computational cost

---

## 📈 MODEL PERFORMANCE

| Model          | Accuracy |
| -------------- | -------- |
| CNN Base       | 0.90     |
| EfficientNetB0 | 0.21     |
| ResNet50       | **0.98** |

**Conclusion:**
ResNet50 achieves the best performance and is selected for deployment.

---

## 🖼️ TRAINING VISUALIZATION

### Loss & Accuracy

<p align="center">
  <img src="asets/loss_acc_cnn.png.png" width="220"/>
  <img src="asets/loss_acc_effnet.png.png" width="220"/>
  <img src="asets/loss_acc_resnet.png.png" width="220"/>
</p>

### Confusion Matrix

<p align="center">
  <img src="asets/confusion_cnn.png.png" width="220"/>
  <img src="asets/confusion_effnet.png.png" width="220"/>
  <img src="asets/confusion_resnet.png.png" width="220"/>
</p>

---

## 🚀 RUN LOCALLY (STREAMLIT)

### 1. Clone Repository

```bash
git clone https://github.com/username/fruit-image-classification.git
cd fruit-image-classification
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Environment

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Application

```bash
streamlit run app.py
```

---

## 🌐 LIVE DEMO

👉 [LINK-DASHBOARD_FRUIT_IMAGE_CLASSIFICATION](https://fruit-image-classification-raq749yzbxxknmpnc9gwfl.streamlit.app/)

---

## 👤 AUTHOR

**Name:** Revinda Visma Novatalia
**Student ID:** 202210370311176
**Program:** Informatics Engineering
**University:** Universitas Muhammadiyah Malang

---

## 📄 VERSION

* Version: **1.0**
* Last Update: **December 2025**
