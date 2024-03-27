
GOOGLE_API_KEY = "AIzaSyCAs8iZi85LZXasXxaezRjQ9PvdRO-sTQk"
from bardapi import Bard
import os
import time
import speech_recognition as sr
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
# import pygame
# from gtts import gTTS
import tempfile
import pyttsx3
import os

def textShow(text):
  text = text.replace('>', '')
  return Markdown(textwrap.indent(text, '>' ))

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.0-pro-latest")

def ansG(a):
    #    while True:
            # a = input("Enter your query: ")
        prompt= f"""
              You are question answer bot . your work is to answer question in a concise way and provide response in plan text , do not provide answer in markdown form.
              ```
              Question : {a}
              ```
        """
        response = model.generate_content(prompt)
        markdown_text = textShow(response.text)
        print(markdown_text.data)
        return  response.text # Print the text stored in the Markdown object


r = sr.Recognizer()
while True:
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.3)
        print("speak now")
        audio = r.listen(source)
    speak = r.recognize_google(audio)
    print("speaker",speak) 
    a = ansG(speak)
    engine = pyttsx3.init()
    # convert this text to speech
    
    engine.say(a)
# play the speech
    engine.runAndWait()


       