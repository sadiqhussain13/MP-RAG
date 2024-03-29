import os
import logging
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
from PIL import Image
import io

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Function to convert image to text
def img2text(file):
    # Check if file is uploaded
    if file is not None:
        # Read the image file
        img = Image.open(io.BytesIO(file.read()))

        # Convert image to text
        image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
        text = image_to_text(img)[0]["generated_text"]

        return text
    else:
        return "No image uploaded"

# Function to generate a story based on a scenario
def generate_story(scenario):
    #API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

    headers = {
        "Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"
    }

    data = {
        "scenario": scenario,
    }

    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        story = response.json()["generated_text"]
        return story
    else:
        return "Failed to generate story"
    

# Function to convert text to speech
def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payloads = {
        "inputs": message
    }   

    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)

def main():
    st.header("Turn Image into Audio Story")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        st.image(uploaded_file, caption='Uploaded image.', use_column_width=True)
        scenario = img2text(uploaded_file)
        story = generate_story(scenario)
        text2speech(story)

        with st.expander("Scenario"):
            st.write(scenario)
        with st.expander("Story"):
            st.write(story)

        st.audio("audio.flac")

if __name__ == "__main__":
    main()
