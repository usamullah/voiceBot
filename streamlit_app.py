import streamlit as st
import speech_recognition as sr
import pyttsx3
import textwrap
import google.generativeai as genai

# Set up Google API key
GOOGLE_API_KEY = "AIzaSyCAs8iZi85LZXasXxaezRjQ9PvdRO-sTQk"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.0-pro-latest")

# Function to display text in Markdown format
def text_show(text):
    text = text.replace('>', '')
    return textwrap.indent(text, '>')

# Function to get answer from GPT-3 model
def get_answer(question):
    prompt = f"""
        You are a question answering bot. Your work is to answer questions in a concise way and provide responses in plain text. Do not provide answers in Markdown format.
        ```
        Question : {question}
        ```
    """
    response = model.generate_content(prompt)
    return response.text

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Streamlit app
def main():
    st.title("Question Answering Bot")

    # Initialize speech recognizer
    r = sr.Recognizer()

    # Add a button to start listening
    if st.button("Start Listening"):
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = r.listen(source)

        try:
            st.write("Processing...")
            query = r.recognize_google(audio)
            st.write(f"You asked: {query}")

            # Get answer
            answer = get_answer(query)
            st.write("Answer:", answer)

            # Convert answer to speech
            text_to_speech(answer)

        except sr.UnknownValueError:
            st.write("Sorry, I couldn't understand the audio.")
        except sr.RequestError:
            st.write("Sorry, there was an issue with the speech recognition service.")

if __name__ == "__main__":
    main()
