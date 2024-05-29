import streamlit as st
from clarifai.client.auth import create_stub
from clarifai.client.auth.helper import ClarifaiAuthHelper
from clarifai.client.user import User
from clarifai.modules.css import ClarifaiStreamlitCSS
from google.protobuf import json_format, timestamp_pb2

import streamlit as st
from PIL import Image
import requests
import io
import os
import base64

# Clarifai API key and model ID
CLARIFAI_API_KEY = '7e2b5b718f274810a8bd1f08a28d4236'
MODEL_ID = '75c5d7b06855413a93fb3dbe96a3f4fd'  # Specify your model ID here

# Set the API key in the environment variable
os.environ['CLARIFAI_API_KEY'] = CLARIFAI_API_KEY

# Function to classify image using Clarifai
def classify_image(image):
    url = f"https://clarifai.com/victor_g/Victor_Img_class/models/victor-tl-classifier"
    headers = {
        "Authorization": f"Key {CLARIFAI_API_KEY}",
        "Content-Type": "application/json"
    }
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')
    img_str = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    
    data = {
        "inputs": [
            {
                "data": {
                    "image": {
                        "base64": img_str
                    }
                }
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Streamlit app
st.title('Image Classification App with Clarifai')
st.write('Upload an image for classification')

# File uploader
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Classify the image
    st.write('Classifying the image...')
    result = classify_image(image)
    
    # Display the results
    if result:
        concepts = result['outputs'][0]['data']['concepts']
        st.write('Predicted concepts:')
        for concept in concepts:
            st.write(f"{concept['name']}: {concept['value']:.2f}")
    else:
        st.write('Unable to classify the image. Please try again.')
