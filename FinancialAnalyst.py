import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

# Set the temporary directory to a dynamically created one
load_dotenv()  # take environment variables from .env (especially openai api key)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }
        .stSidebar {
            background-color: #001f3f;
            color: white;
        }
        .stTitle, .stHeader {
            color: #007acc;
        }
        .stButton > button {
            background-color: #007acc;
            color: white;
        }
        .chat-box {
            background-color: white;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }
        .user-question {
            color: #007acc;
        }
        .bot-answer {
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

st.title("FinancialAnalystGPT: News Research Tool 📈")
st.sidebar.title("News Article URLs")

# Input for the number of URLs
number_of_urls = st.sidebar.number_input(label="Number of URLs", min_value=0, max_value=20, value=1)
urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(number_of_urls)]
process_url_clicked = st.sidebar.button("Process URLs")

# Specify a directory path for FAISS index
faiss_dir = "faiss_index"

main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)
embeddings = OpenAIEmbeddings()

text_splitter = RecursiveCharacterTextSplitter(
    separators=['\n\n', '\n', '.', ','],
    chunk_size=1000
)

def create_vector_store_from_urls(urls, embeddings):
    loader = WebBaseLoader(web_paths=urls)
    data = loader.load()
    docs = text_splitter.split_documents(data)
    vectorstore_urls = FAISS.from_documents(docs, embeddings)
    return vectorstore_urls

def save_faiss_index(vectorstore, faiss_dir):
    if not os.path.exists(faiss_dir):
        os.makedirs(faiss_dir)
    vectorstore.save_local(faiss_dir)

def response_of_llm_for_url(faiss_dir, query, embeddings, llm):
    vectorstore = FAISS.load_local(faiss_dir, embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=retriever)
    result = chain({"question": query}, return_only_outputs=True)
    return result

if process_url_clicked:
    if all(urls):
        try:
            pro = st.progress(0)
            main_placeholder.text("Processing URLs...")

            # Create vector store from URLs
            vectorstore_urls = create_vector_store_from_urls(urls, embeddings)
            pro.progress(50)
            
            # Save the FAISS index to a directory
            save_faiss_index(vectorstore_urls, faiss_dir)
            pro.progress(100)
            time.sleep(1)
            pro.empty()
            st.session_state.option = "URLS"
            main_placeholder.text("URLs processed successfully.")
        except Exception as e:
            main_placeholder.error(f"An error occurred: {e}")
    else:
        main_placeholder.error("Please enter all URLs.")

# Chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Question: ")
if query:
    if os.path.exists(faiss_dir):
        main_placeholder.text("Fetching response...")

        try:
            # Get response using LLM for the URL data
            result = response_of_llm_for_url(faiss_dir, query, embeddings, llm)
            answer = result["answer"]

            # Save question and answer to chat history
            st.session_state.chat_history.append({"question": query, "answer": answer})

            main_placeholder.empty()

            # Display chat history
            for chat in st.session_state.chat_history:
                st.markdown(f'<div class="chat-box"><p class="user-question"><b>User:</b> {chat["question"]}</p><p class="bot-answer"><b>RockyBot:</b> {chat["answer"]}</p></div>', unsafe_allow_html=True)

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")
                for source in sources_list:
                    st.write(source)
        except Exception as e:
            main_placeholder.error(f"An error occurred while fetching the response: {e}")
    else:
        main_placeholder.error("The FAISS index does not exist. Please process the URLs first.")
