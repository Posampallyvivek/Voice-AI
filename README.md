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

# Why I Used ChatGroq Instead of OpenAI
## Speed 🚀:
ChatGroq is optimized for super-fast response times compared to standard OpenAI APIs, especially when working with large models like LLaMA 3-70B.

## Model Choice 🧠:
ChatGroq offers Meta’s LLaMA 3 models (like llama3-70b-8192), which are highly capable, open-weight alternatives to OpenAI’s GPT models. I wanted to explore the latest LLaMA models for better Hinglish understanding and casual chatting.

## Cost Efficiency 💸:
Groq’s API can be more affordable for heavy use compared to OpenAI pricing, especially when scaling applications or during frequent user interactions like in a chatbot.

## Experimentation and Learning 📚:
Using ChatGroq allows experimenting with different providers and different architectures, giving more flexibility and learning experience rather than sticking only to OpenAI.

## Open Ecosystem 🌐:
ChatGroq promotes working with open models, which aligns with the vision of using open, accessible AI instead of closed systems.

# Features

Speech-to-Text: Recognize user speech and convert it into text using the speech_recognition library.
Fuzzy Matching: Match the user's input with the dataset using fuzzy string matching and return the most relevant response.
Hinglish Responses: The bot responds in Hinglish without translating or explaining the meanings.
Text-to-Speech: Converts the chatbot’s response into speech using pyttsx3, making the interaction more natural.
Voice or Text Input: Users can choose between typing their question or speaking to the chatbot.

# How It Works
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
Configure your **Groq API Key** for LLM responses in the code 
groq_api_key="YOUR_GROQ_API_KEY"



