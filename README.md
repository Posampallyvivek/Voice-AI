# 🎙️ Hinglish Voice Chatbot 🤖

This project is a **Hinglish Voice Chatbot** that uses speech recognition, fuzzy string matching, and a Groq-based Large Language Model (LLM) to understand and generate responses in Hinglish (a mix of Hindi and English). The chatbot can respond to both **text** and **speech** inputs and speaks back the responses to the user.

## 📦 Requirements

- Python 3.x
- Streamlit
- sounddevice
- numpy
- pyttsx3
- speech_recognition
- langchain
- langchain_groq
- fuzzywuzzy

## Features

Speech-to-Text: Recognize user speech and convert it into text using the speech_recognition library.
Fuzzy Matching: Match the user's input with the dataset using fuzzy string matching and return the most relevant response.
Hinglish Responses: The bot responds in Hinglish without translating or explaining the meanings.
Text-to-Speech: Converts the chatbot’s response into speech using pyttsx3, making the interaction more natural.
Voice or Text Input: Users can choose between typing their question or speaking to the chatbot.

## How It Works
## 1. Load JSONL Dataset
The dataset, stored in JSONL format, contains a list of prompts and corresponding responses. It is loaded using the load_jsonl() function.

## 2. Speech Recognition
The app records the user’s voice input for 5 seconds and converts the speech into text using the speech_recognition library.

## 3. Dataset Matching
The user input is compared with the pre-defined dataset using fuzzy string matching (fuzzywuzzy). If a match is found, the response is retrieved from the dataset.

## 4. LLM-based Response
If no dataset match is found, the chatbot generates a Hinglish response using the Groq-based LLM. The langchain_groq package is used to invoke the LLM and get the response.

## 5. Text-to-Speech
Once the response is generated, it is read aloud using the pyttsx3 library.

## Note 
Configure your **Groq API Key** for LLM responses in the code given below:/n
llm = ChatGroq(
    temperature=0.2,
    groq_api_key="YOUR_GROQ_API_KEY",  # Replace with your Groq API key
    model_name="llama3-70b-8192"
)

