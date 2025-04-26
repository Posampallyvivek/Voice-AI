import streamlit as st
import json
import sounddevice as sd
import numpy as np
import pyttsx3
import speech_recognition as sr
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from fuzzywuzzy import fuzz

# -------- Load JSONL Dataset --------
def load_jsonl(filename):
    examples = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            examples.append(json.loads(line))
    return examples

# -------- Text-to-Speech --------
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# -------- Speech Recognition --------
def recognize_speech():
    st.info("Listening... Speak now!")

    duration = 5  # seconds
    samplerate = 16000
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(audio.tobytes(), samplerate, 2)

    try:
        text = recognizer.recognize_google(audio_data, language="en-IN")
        return text
    except sr.UnknownValueError:
        try:
            text = recognizer.recognize_google(audio_data, language="hi-IN")
            return text
        except (sr.UnknownValueError, sr.RequestError):
            return ""
    except sr.RequestError:
        return ""

# -------- Check if input matches dataset --------
def check_dataset(user_input, dataset, threshold=85):
    best_score = 0
    best_response = None

    for example in dataset:
        prompt = example['prompt']
        response = example['completion']

        score = fuzz.token_set_ratio(prompt.lower(), user_input.lower())
        if score > best_score:
            best_score = score
            best_response = response

    if best_score >= threshold:
        return best_response
    else:
        return None

# -------- Generate Bot Response --------
def generate_response(user_input):
    if user_input.strip() == "":
        st.warning("No input detected.")
        return

    # 1. Check dataset first
    dataset_response = check_dataset(user_input, examples)
    if dataset_response:
        st.success(dataset_response)
        speak(dataset_response)
        return

    # 2. If no dataset match, use LLM
    prompt_template = PromptTemplate(
        input_variables=["user_input"],
        template="""You are a friendly Hinglish chatbot. 
Always reply casually in Hinglish without explaining the meaning or translating. 
Be short, friendly and natural.

User: {user_input}
Assistant:"""
    )
    final_prompt = prompt_template.format(user_input=user_input)

    try:
        response_obj = llm.invoke(final_prompt)

        if hasattr(response_obj, "content"):
            output_text = response_obj.content
        else:
            output_text = str(response_obj)

        st.success(output_text)
        speak(output_text)
    except Exception as e:
        st.error("Something went wrong. Please try again.")

# -------- Initialize LLM --------
llm = ChatGroq(
    temperature=0.2,
    groq_api_key="",  # <<< PUT your GROQ API key
    model_name="llama3-70b-8192"
)

# Load dataset examples
examples = load_jsonl("dataset.jsonl")  # <<< Make sure file is present

# -------- Streamlit App UI --------
st.title("🎙️ Hinglish Voice Chatbot 🤖")

# Sidebar Examples
if st.sidebar.button("Show Example Prompt"):
    example = st.sidebar.selectbox("Example Questions:", [ex["prompt"] for ex in examples])
    st.sidebar.write(example)

# Choice: Text or Voice Input
input_mode = st.radio("Choose Input Mode:", ["Type Text ✍️", "Speak 🎤"])

user_input = ""

if input_mode == "Type Text ✍️":
    user_input = st.text_input("Type your question (in Hinglish):")
    if st.button("Generate Response"):
        generate_response(user_input)

else:
    if st.button("Start Recording 🎙️"):
        user_input = recognize_speech()
        if user_input.strip() != "":
            st.success(f"You said: {user_input}")
            generate_response(user_input)
        else:
            st.warning("No valid speech input recognized.")
