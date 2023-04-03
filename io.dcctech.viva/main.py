#  Copyright © 2022 - 2023, DCCTech. All Rights Reserved.
#  This copyright notice is the exclusive property of DCCTech and is hereby granted to users
#  for use of DCCTech's intellectual property.
#  Any reproduction, modification, distribution, or other use of DCCTech's intellectual property without prior written
#  consent is strictly prohibited.


import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

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
            print(f"You said: {text}")
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
                    reminder = "Okay, I'll remind you to {reminder_text} at {reminder_time}"
                    speak(f"Okay, I'll remind you to {reminder_text} at {reminder_time}")
                    save_to_file("reminder", reminder)
                else:
                    speak("Sorry, that time has already passed.")
            except:
                speak("Sorry, I didn't understand the time you said.")


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


# Define a function to search Wikipedia
def search_wikipedia():
    speak("What do you want to search for on Wikipedia?")
    search_text = recognize_speech()
    if search_text:
        try:
            speak(f"Here's what I found on Wikipedia about {search_text}")
            summary = wikipedia.summary(search_text, 2)
            speak(summary)
            save_to_file("Wikipedia", summary)

        except:
            speak("Sorry, I couldn't find any information on that.")


# Define a function to search the web
def search_web():
    speak("What do you want to search for on the web?")
    search_text = recognize_speech()
    if search_text:
        url = f"https://www.google.com/search?q={search_text}"
        webbrowser.open_new_tab(url)
        speak(f"Here's what I found on the web about {search_text}")


def file_name(name):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{name}_{now}.txt"


def save_to_file(name, text):
    with open(file_name(name), 'w') as f:
        f.write(text)


# Main loop
while True:
    speak("How can I help you?")
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
        elif "quit" or "none" or "nothing" or "exit" in command:
            break
