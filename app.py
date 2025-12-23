import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
import os

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input as mobilenet_preprocess
from tensorflow.keras.applications.efficientnet import preprocess_input as efficientb0_preprocess

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Klasifikasi Buah",
    layout="wide"
)

# =====================================================
# LOAD MODELS
# =====================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_resource
def load_models():
    models = {
        "CNN Base": tf.keras.models.load_model(
            os.path.join(BASE_DIR, "models", "cnn_base_96.h5")
        ),
        "MobileNetV2": tf.keras.models.load_model(
            os.path.join(BASE_DIR, "models", "mobilenet_small_96.h5")
        ),
        "EfficientNetB0": tf.keras.models.load_model(
            os.path.join(BASE_DIR, "models", "efficientnetb0_96.h5")
        ),
    }

    CLASSES = ["apple", "banana", "grapes", "orange", "strawberry"]
    return models, CLASSES

# Load models
try:
    models, CLASSES = load_models()
except FileNotFoundError as e:
    st.error(f"❌ Model tidak ditemukan: {e}")
    st.stop()

# =====================================================
# HEADER
# =====================================================
st.markdown(
    "<h1 style='text-align: center;'>🍎 Sistem Klasifikasi Buah</h1>",
    unsafe_allow_html=True
)

st.markdown(
    f"<p style='text-align: center;'>Kelas Buah: {', '.join(CLASSES)}</p>",
    unsafe_allow_html=True
)

# =====================================================
# SIDEBAR - MODEL SELECTION
# =====================================================
st.sidebar.header("🔧 Pilih Model")

model_cnn = st.sidebar.checkbox("CNN Base (Non-Pretrained)", value=True)
model_mobilenet = st.sidebar.checkbox("MobileNetV2 (Pretrained)")
model_efficientb0 = st.sidebar.checkbox("EfficientNetB0 (Pretrained)")
compare_all = st.sidebar.checkbox("Bandingkan Semua Model")

selected_models = {}

if compare_all:
    selected_models = models
else:
    if model_cnn:
        selected_models["CNN Base"] = models["CNN Base"]
    if model_mobilenet:
        selected_models["MobileNetV2"] = models["MobileNetV2"]
    if model_efficientb0:
        selected_models["EfficientNetB0"] = models["EfficientNetB0"]

# =====================================================
# SIDEBAR - SYSTEM INFO
# =====================================================
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    ### ℹ️ Tentang Sistem
    Aplikasi ini merupakan **sistem klasifikasi citra buah**
    berbasis **Deep Learning** yang membandingkan:

    - **CNN Base** (Non-Pretrained)
    - **MobileNetV2** (Transfer Learning)
    - **EfficientNetB0** (Transfer Learning)
    """
)

# =====================================================
# MAIN - SYSTEM DESCRIPTION
# =====================================================
st.markdown(
    """
    ## 🧠 Deskripsi Sistem

    Sistem ini dikembangkan untuk **Ujian Akhir Praktikum (UAP) Pembelajaran Mesin**
    dengan tujuan mengimplementasikan dan membandingkan
    **model CNN non-pretrained dan pretrained**
    pada permasalahan **klasifikasi citra buah**.

    ### 🔍 Alur Kerja Sistem
    1. Pengguna memilih model pembelajaran mesin pada menu sidebar.
    2. Pengguna mengunggah gambar buah (JPG / PNG).
    3. Sistem menyesuaikan ukuran citra sesuai model.
    4. Preprocessing dilakukan sesuai arsitektur model.
    5. Model memprediksi kelas buah dan probabilitasnya.
    6. Hasil prediksi divisualisasikan dalam bentuk grafik.

    ### 🍎 Kelas Buah
    - Apple
    - Banana
    - Grapes
    - Orange
    - Strawberry
    """
)

# =====================================================
# IMAGE UPLOAD
# =====================================================
uploaded = st.file_uploader(
    "📤 Upload Gambar Buah",
    type=["jpg", "jpeg", "png"]
)

# =====================================================
# MAIN CONTENT
# =====================================================
if uploaded:

    if len(selected_models) == 0:
        st.warning("⚠️ Pilih minimal satu model terlebih dahulu.")
        st.stop()

    left_col, right_col = st.columns([1, 2])

    # -------------------------------
    # LEFT : IMAGE
    # -------------------------------
    with left_col:
        img = Image.open(uploaded).convert("RGB")

        # AUTO RESIZE SESUAI MODEL
        sample_model = list(selected_models.values())[0]
        h, w = sample_model.input_shape[1], sample_model.input_shape[2]

        img = img.resize((w, h))
        st.image(
            img,
            caption=f"Gambar Input ({w}x{h})",
            use_container_width=True
        )

    img_array = np.expand_dims(np.array(img), axis=0)

    # -------------------------------
    # RIGHT : RESULT
    # -------------------------------
    with right_col:
        if st.button("🔍 Prediksi"):
            st.subheader("📊 Hasil Prediksi & Probabilitas")

            if not compare_all:
                for name, model in selected_models.items():

                    if name == "CNN Base":
                        input_data = img_array / 255.0
                    elif name == "MobileNetV2":
                        input_data = mobilenet_preprocess(img_array.copy())
                    else:
                        input_data = efficientb0_preprocess(img_array.copy())

                    pred = model.predict(input_data, verbose=0)[0]
                    idx = np.argmax(pred)
                    conf = pred[idx] * 100

                    st.success(
                        f"**{name}** → **{CLASSES[idx]}** ({conf:.2f}%)"
                    )

                    df = pd.DataFrame({
                        "Kelas": CLASSES,
                        "Probabilitas (%)": pred * 100
                    })

                    st.bar_chart(df.set_index("Kelas"), height=300)

            else:
                cols = st.columns(len(selected_models))

                for col, (name, model) in zip(cols, selected_models.items()):
                    with col:

                        if name == "CNN Base":
                            input_data = img_array / 255.0
                        elif name == "MobileNetV2":
                            input_data = mobilenet_preprocess(img_array.copy())
                        else:
                            input_data = efficientb0_preprocess(img_array.copy())

                        pred = model.predict(input_data, verbose=0)[0]
                        idx = np.argmax(pred)
                        conf = pred[idx] * 100

                        st.markdown(f"### 🔹 {name}")
                        st.success(
                            f"{CLASSES[idx]} ({conf:.2f}%)"
                        )

                        df = pd.DataFrame({
                            "Kelas": CLASSES,
                            "Probabilitas (%)": pred * 100
                        })

                        st.bar_chart(
                            df.set_index("Kelas"),
                            height=250
                        )

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption(
    "by Revinda Visma Novatalia | UAP Machine Learning | CNN Base • MobileNetV2 • EfficientNetB0"
)
