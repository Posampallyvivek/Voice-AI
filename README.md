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

#Features

Speech-to-Text: Recognize user speech and convert it into text using the speech_recognition library.
Fuzzy Matching: Match the user's input with the dataset using fuzzy string matching and return the most relevant response.
Hinglish Responses: The bot responds in Hinglish without translating or explaining the meanings.
Text-to-Speech: Converts the chatbot’s response into speech using pyttsx3, making the interaction more natural.
Voice or Text Input: Users can choose between typing their question or speaking to the chatbot.
