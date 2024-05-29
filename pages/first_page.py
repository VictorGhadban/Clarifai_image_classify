import streamlit as st
from clarifai.client.auth import create_stub
from clarifai.client.auth.helper import ClarifaiAuthHelper
from clarifai.client.user import User
from clarifai.modules.css import ClarifaiStreamlitCSS
from google.protobuf import json_format, timestamp_pb2

st.set_page_config(layout="wide")
ClarifaiStreamlitCSS.insert_default_css(st)

# This must be within the display() function.
auth = ClarifaiAuthHelper.from_streamlit(st)
stub = create_stub(auth)
userDataObject = auth.get_user_app_id_proto()
model_url = (
    "https://clarifai.com/victor_g/Victor_Img_class/models/victor-tl-classifier"
)
st.title('Image Classification App')
st.write('Upload an image for classification')

# File uploader
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess the image
    img = preprocess_image(image)



if submitted:
  if mtotal is None or mtotal == 0:
    st.warning("Number of inputs must be provided.")
    st.stop()
  else:
    st.write("Number of inputs in table will be: {}".format(mtotal))

# Predict the class
    predictions = model.predict(img)
    predicted_class = class_names[np.argmax(predictions[0])]
    model_prediction = Model(url=model_url, pat="edd5180d73a64b30b4fbc2085f775ef4").predict_by_url(
    image_url, input_type="image"
)

    # Display the prediction
    st.write(f'Predicted Class: {predicted_class}')
