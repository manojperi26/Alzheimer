import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model("alzheimer_model.h5")

class_names = ["NonDemented", "VeryMildDemented", "MildDemented", "ModerateDemented"]

st.title("Alzheimer MRI Classifier")

uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).resize((224,224))
    
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)

    # IMPORTANT preprocessing
    img_array = tf.keras.applications.vgg16.preprocess_input(img_array)

    prediction = model.predict(img_array)
    pred_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.image(image)
    st.write(f"Prediction: {pred_class}")
    st.write(f"Confidence: {confidence*100:.2f}%")