# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1esc38moSYhqdjqeWI7OQiQ05cCQR2-Ze

### **Creating Streamlit Application**
"""

import tensorflow as tf
import streamlit as st
from PIL import Image
import numpy as np

#Crearting a function for prediction
def predict_img(image):
    class_names = ["Early_Blight","Healthy","Late_Blight"]
    model = tf.keras.models.load_model("potatoe_disease_classifier.h5")

    image_array = np.array(image)
    img_batch = np.expand_dims(image_array, 0)

    prediction = model.predict(img_batch)
    predicted_class = class_names[np.argmax(prediction[0])]
    confidence = round(np.max(prediction[0]),2)

    stage = st.subheader(f"Stage: {predicted_class}")
    conf_score = st.subheader(f"Confidence: {confidence}")

    return stage

st.title("Potato Disease Classifier")
upload_image = st.file_uploader(label="Upload Potato leaf Image",type=["png","jpg","jpeg"])

if upload_image is not None:
    image = Image.open(upload_image)
    image_show = st.image(image, caption='Uploaded Image.', width=256)

    predict_img(image)




footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: blue;
text-align: center;
}
</style>
<div class="footer">
<p><a style='display: block; text-align: center;' target="_blank">Built by Ramesh Kumar S</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)







