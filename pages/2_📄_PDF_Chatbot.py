import streamlit as st
import os
from dotenv import find_dotenv, load_dotenv
from langchain_groq import ChatGroq
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Get the GROQ API key from the environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    print("Error: GROQ_API_KEY is not set in the environment.")

else:
    print("GROQ_API_KEY loaded successfully:", GROQ_API_KEY)

def main():
    st.title("Chat with your PDF")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

    # Extract the text if file is uploaded
    if file is not None:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Break text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            separators="\n",
            chunk_size=1000,
            chunk_overlap=150,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Generating embeddings
        embeddings = OllamaEmbeddings(model="nomic-embed-text")

        # Generating vector store - FAISS
        vector_store = FAISS.from_texts(chunks, embeddings)

        # Get user questions
        user_question = st.text_input("Type your question here")

        # Do similarity search
        if user_question:
            match = vector_store.similarity_search(user_question)

            # Define the LLM
            llm = ChatGroq(
                groq_api_key=GROQ_API_KEY,
                temperature=1,
                max_tokens=1000,
                model_name="mixtral-8x7b-32768"
            )

            # Output results
            # Chain → take the question, get relevant document, pass it to the LLM, generate the output
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=match, question=user_question)
            st.write(response)

if __name__ == "__main__":
    main()
