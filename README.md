# Multipurpose RAG Web App
![Version](https://img.shields.io/badge/Version-%5E1.0.0-blue.svg?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-%5E1.10.0-green.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Conda](https://img.shields.io/badge/Conda-%5E4.10.2-orange.svg?style=for-the-badge&logo=conda&logoColor=white)

## About
This project is a Multipurpose RAG Web app that enables users to explore the possibilities of text, images, and audio. The app features three main components: PDF Chatbot, Story Board, and Image-to-Text.

## Installation
#### 1. Clone the repository
Clone the repository using the following command:
```bash
git clone "https://github.com/sadiqhussain13/MP-RAG.git"
cd MP-RAG
```
#### 2. Install dependencies
Install the necessary dependencies using the following command:
```bash
conda env create -f environment.yml
conda activate MP-RAG
```
#### 3. Set up environment variables
Create a `.env` file in the root of the project and add the following environment variables:
```bash
GROQ_API_KEY=YOUR_GROQ_API_KEY
HUGGINGFACEHUB_API_TOKEN=YOUR_HUGGINGFACEHUB_API_TOKEN
```
Replace `YOUR_GROQ_API_KEY` and `YOUR_HUGGINGFACEHUB_API_TOKEN` with your actual API keys.

## Running the Application
#### 1. Start the app
Start the app using the following command:
```bash
streamlit run 1_🏠_Home.py
```
This will start the Streamlit app on port 8501.

#### 2. Access the app
Open the app in your web browser by navigating to http://localhost:8501.

## Technologies Used

| Technology | Description |
|------------|-------------|
| ![Streamlit](https://img.shields.io/badge/Streamlit-%5E1.10.0-green.svg?style=for-the-badge&logo=streamlit&logoColor=white) | Web app framework |
| ![Conda](https://img.shields.io/badge/Conda-%5E4.10.2-orange.svg?style=for-the-badge&logo=conda&logoColor=white) | Package manager |
| ![GROQ](https://img.shields.io/badge/GROQ-%5E1.0.0-yellow.svg?style=for-the-badge&logo=groq&logoColor=white) | Question answering API |
| ![Hugging Face API](https://img.shields.io/badge/Hugging%20Face%20API-%5E3.1.0-orange.svg?style=for-the-badge&logo=huggingface&logoColor=white) | AI image generation API |
| ![PyPDF2](https://img.shields.io/badge/PyPDF2-%5E1.26.0-purple.svg?style=for-the-badge&logo=pyPDF2&logoColor=white) | PDF parsing library |
| ![Transformers](https://img.shields.io/badge/Transformers-%5E4.10.2-pink.svg?style=for-the-badge&logo=transformers&logoColor=white) | Natural language processing library |
| ![FAISS](https://img.shields.io/badge/FAISS-%5E1.7.3-blue.svg?style=for-the-badge&logo=faiss&logoColor=white) | Vector store library |
| ![dotenv](https://img.shields.io/badge/dotenv-%5E16.4.5-pink.svg?style=for-the-badge&logo=dotenv&logoColor=white) | Environment variable management library |
