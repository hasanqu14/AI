import speech_recognition as sr
import os
import webbrowser
from openai import OpenAI
from config import apikey
import datetime
import random
import pyttsx3



# Initialize OpenAI client
client = OpenAI(api_key=apikey)

# Initialize text-to-speech engine
engine = pyttsx3.init()

chatStr = ""

def speak(text):
    print(f"Hash AI: {text}")
    engine.say(text)
    engine.runAndWait()

def chat(query):
    global chatStr
    chatStr += f"Hasan: {query}\nHash AI: "

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Hash AI, a helpful assistant."},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
        )
        reply = response.choices[0].message.content.strip()
        speak(reply)
        chatStr += reply + "\n"
        return reply
    except Exception as e:
        speak("Sorry, I ran into an error while connecting to OpenAI.")
        print(e)
        return "Error"

def ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        reply = response.choices[0].message.content.strip()

        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        filename = f"Openai/{''.join(prompt.split()[:5])}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Prompt: {prompt}\n\nResponse:\n{reply}")
        speak("AI response saved successfully.")
    except Exception as e:
        speak("There was an error processing the AI request.")
        print(e)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"Hasan: {query}")
            return query
        except Exception as e:
            speak("Sorry, I didn't catch that.")
            return ""

if __name__ == '__main__':
    speak("Hello, I am Hash AI.")
    while True:
        query = takeCommand().lower().strip()

        if "open youtube" in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif "open wikipedia" in query:
            speak("Opening Wikipedia...")
            webbrowser.open("https://www.wikipedia.com")

        elif "open search" in query:
            speak("Opening AI...")
            webbrowser.open("https://chatgpt.com/?model=auto")

        elif "open portfolio" in query:
            speak("Opening Portfolio...")
            webbrowser.open("https://hasanqu14.github.io/portfolio/")
        elif "the time" in query:
            now = datetime.datetime.now()
            speak(f"The time is {now.strftime('%I:%M %p')}")

        #elif "using artificial intelligence" in query:
         #   ai(query)

        elif "reset chat" in query:
            chatStr = ""
            speak("Chat history has been reset.")

        elif "exit" in query or "stop" in query:
            speak("Goodbye sir.")
            break

        elif query != "":
            chat(query)
