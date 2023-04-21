#  Copyright © 2022 - 2023, DCCTech. All Rights Reserved.
#  This copyright notice is the exclusive property of DCCTech and is hereby granted to users
#  for use of DCCTech's intellectual property.
#  Any reproduction, modification, distribution, or other use of DCCTech's intellectual property without prior written
#  consent is strictly prohibited.
import datetime
import os
import webbrowser

import openai
import pyttsx3
import speech_recognition as sr
import wikipedia

# Set up the API key for GPT-3
openai.api_key = "sk-efel87z6t5r4eedwdwdwdwdKtTPkyGYT9FajE30Ekxq"  # TODO you must regenerate this API key

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Define a function to speak text aloud
def speak(text):
    # voiceChange()
    engine.say(text)
    engine.runAndWait()


def voiceChange():
    # Get a list of available voices
    voice = engine.getProperty('voices')  # get the available voices

    # Set the desire voice
    # the voice to index 0 for male voice
    # the voice to index 1 for female voice
    engine.setProperty('voice', voice[1].id)  # changing voice to index 1 for female voice


# Define a function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Speak now...")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
        except Exception as e:
            print("Oops, something went wrong.")
            print(e)
            return None


# Define a function to create reminders
def create_reminder():
    speak("What do you want me to remind you about?")
    reminder_text = recognize_speech()
    if reminder_text:
        speak("When do you want to be reminded?")
        reminder_time = recognize_speech()
        if reminder_time:
            try:
                reminder_time_obj = datetime.datetime.strptime(reminder_time, "%H:%M")
                current_time_obj = datetime.datetime.now().time()
                if reminder_time_obj.time() > current_time_obj:
                    reminder = f"Okay, I'll remind you to {reminder_text} at {reminder_time}"
                    speak(reminder)
                    save_to_file("reminder", reminder)
                else:
                    speak("Sorry, that time has already passed.")
            except:
                speak("Sorry, I didn't understand the time you said.")
    restart_main()


# Define a function to create a to-do list
def create_todo_list():
    speak("What are the tasks you want to add to the to-do list?")
    tasks = []
    while True:
        task = recognize_speech()
        if "stop" in task:
            break
        tasks.append(task)
    speak("Here's your to-do list:")
    for i, task in enumerate(tasks):
        speak(f" {i + 1}. {task};")

    if tasks is not None:
        save_to_file("task", "\n".join(tasks))

    restart_main()


# Define a function to search Wikipedia
def search_wikipedia():
    speak("What do you want to search for on Wikipedia?")
    search_text = recognize_speech()
    if search_text:
        try:
            speak(f"Here's what I found on Wikipedia about {search_text}")
            summary = wikipedia.summary(search_text, 2)
            speak(summary)
            save_to_file("wikipedia", summary)
        except:
            speak("Sorry, I couldn't find any information on that.")
    restart_main()


# Define a function to search the web
def search_web():
    speak("What do you want to search for on the web?")
    search_text = recognize_speech()
    if search_text:
        url = f"https://www.google.com/search?q={search_text}"
        webbrowser.open_new_tab(url)
        speak(f"Here's what I found on the web about {search_text}")
    restart_main()


def file_name(name):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{name}_{now}.txt"


def save_to_file(name, text):
    abspath = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(abspath, f"../var/{name}/{file_name(name)}")
    with open(path, 'w') as f:
        f.write(text)


def restart_main():
    speak("How can I help you")


def ask_gpt():
    speak("What do you want to ask ChatGPT")
    # speak(f"You asked ChatGPT this: {question}")
    whole_script = ""
    while True:
        question = recognize_speech()
        if "stop" in question:
            save_to_file("gpt", whole_script)
            restart_main()
            break
        elif question:
            whole_script += f"You: {question}\n"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=question,
                temperature=0.4,
                max_tokens=150
            )
            answer = response.choices[0].text
            whole_script += f"GPT: {answer.strip()}\n"
            speak(answer)


# Main loop
speak("Hello, how can I help you")
while True:
    command = recognize_speech()
    if command:
        if "remind me" in command:
            create_reminder()
        elif "create a to-do list" in command:
            create_todo_list()
        elif "Wikipedia" in command:
            search_wikipedia()
        elif "search the web" in command:
            search_web()
        elif "GPT" in command:
            ask_gpt()
        elif "quit" in command or "exit" in command:
            break
        else:
            speak("Unfortunately, I can't find such an option. Could you repeat that?")
