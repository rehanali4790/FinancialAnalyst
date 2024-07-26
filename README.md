# FinancialAnalyst

FinancialAnalystGPT: News Research Tool 📈
Project by Rehan Ali
Contact: rehanalikhan4790@gmail.com

## Overview
FinancialAnalystGPT is a robust news research tool designed to analyze and summarize news articles from multiple URLs. The application leverages Langchain's retrieval-based question-answering capabilities and FAISS indexing to provide accurate and sourced responses to user queries. The user interface is built with Streamlit, ensuring an interactive and user-friendly experience.

## Features
1. URL Input: Users can input multiple news article URLs.
2. Vector Store Creation: Creates a vector store from the content of the provided URLs.
3. Data Retrieval: Uses FAISS for efficient similarity search and retrieval.
4. Question Answering: Provides answers to user queries based on the content of the processed URLs.
5. Chat History: Maintains a history of user questions and bot answers.
6. Offline Operation: Operates fully offline once URLs are processed, ensuring no risk of data leakage as no external APIs are used.
7. Customizable: While primarily designed for financial news, the application can be customized for other business cases and text analysis tasks.

## **Setup and Usage**
**Prerequisites**
1. Python 3.8 or higher
2. Streamlit
3. Langchain
4. FAISS
5. OpenAI API key

## Installation
Clone the repository:
git clone https://github.com/rehanali4790/FinancialAnalyst.git
cd FinancialAnalyst

## Install the required packages:


1. pip install streamlit langchain faiss-cpu openai python-dotenv
2. Set up your OpenAI API key:
3. Create a .env file in the project directory and add your OpenAI API key:
4. OPENAI_API_KEY=your_openai_api_key

## Run the Streamlit app:

streamlit run app.py

**Usage**

1. Open the Streamlit app in your web browser.
2. Input the number of URLs you wish to process.
3. Enter the URLs in the provided input fields.
4. Click "Process URLs" to create the vector store.
5. Ask questions related to the content of the processed URLs.
6. View the responses and sources, if available, displayed in the chat history.

## Application in the Government Sector
The FinancialAnalystGPT application can be a valuable tool in the government sector for various applications, including but not limited to:

1, Policy Analysis: Summarizing and analyzing news articles related to policy changes and government actions.
2. Public Relations: Monitoring and responding to news about government initiatives and public perception.
3. Security and Intelligence: Analyzing news for security threats and intelligence gathering.
4. Regulatory Compliance: Keeping track of news related to regulatory changes and compliance requirements.
5. Research and Development: Gathering information on technological advancements and global trends.

By integrating the RockyBot application into various government departments, efficiency in information processing and decision-making can be significantly improved.

## Beyond Financial News
The capabilities of RockyBot are not limited to financial news. The underlying technology can be adapted for various other purposes, such as:

1. Market Research: Analyzing and summarizing market trends and business news.
2. Healthcare: Keeping track of medical research, health news, and policy changes.
3. Education: Gathering information on educational trends, policies, and research.
4. Legal: Summarizing legal news and case studies for quick reference.

This versatility makes FinancialAnalystGPT a powerful tool for numerous text analysis and data extraction tasks across different domains.

For any queries or further assistance, please contact at rehanalikhan4790@gmail.com.

for demo video please visit this link https://www.linkedin.com/posts/rehan-ali-6a725924a_ai-financialresearch-innovation-activity-7219711951243800583-urYp?utm_source=share&utm_medium=member_desktop
