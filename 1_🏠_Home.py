import streamlit as st

st.set_page_config(
    page_title="Multipurpose App",
    page_icon="🤖",
)

st.title("Welcome to the MP-RAG App")

# Introduction
st.write("""
Explore the possibilities, unleash your creativity, and enjoy the seamless journey through the realms of text, images, and audio with our Multipurpose RAG Web app.

## **Features:**

##### PDF Chatbot: Document Queries and Intelligent Q&A
         
         Extract text from PDFs for instant intelligent answers.
         

##### Story Board: Image-to-Audio Transformation
         
         Transform images into immersive audio narratives with ease.
""")
st.sidebar.success("Select an option above")
