# VIVA - Virtual Intelligent Voice Assistant

VIVA is a virtual voice assistant that can be used to carry out simple tasks, like placing orders or 
scheduling appointments. This project provides the tools and resources you need to build your own virtual assistant 
using advanced natural language processing techniques.

The application begins by greeting the user and asking how it can be of assistance. It then enters a loop that 
listens for user input through speech recognition.

If the user's input is the phrase "remind me," the function will create a reminder. If the input is the
phrase "create a to-do list," the function will create a to-do list. If the input is the word "Wikipedia," the
function will search for Wikipedia. If the input contains the phrase "search the web," the function will perform 
a web search. If the input is the word "GPT," the function will perform a task related to GPT. To use this function,
you can talk to ChatGPT by speaking to it and giving it commands. The function will continue to listen for your input 
and respond accordingly until you say the word "stop" to end the application.

  To create an OpenAI API key, first sign up for an account on the OpenAI website. Once you have an account, navigate to
  the API page and click "Create API Key". You will then be prompted to provide a name for your API key and select 
  which API endpoints you would like the key to have access to. Once you have done this, click "Create API Key" 
  again to generate your new key. You can then copy and paste the key into your code or save it in a secure location 
  for future use.

If the input does not match any of these options, the function will inform the user that it cannot find a 
suitable option and ask the user to repeat their input.

The loop will continue until the user says "quit" or "exit," at which point the function will end.
## Features

- Easy-to-use voice interface
- Customizable commands and responses

In the future, the integration with popular APIs and services within this project will provide users with a 
wide range of capabilities, from setting reminders to placing orders, making their daily lives more convenient and
productive. Additionally, the built-in machine learning algorithms for natural language processing will enhance 
the voice assistant's ability to interpret and respond to user commands, 
improving its accuracy and effectiveness over time.

## Getting Started
To get started with VIVA, you'll need to have some knowledge of programming and natural language processing. 

## Installation
To install VIVA, follow these steps:

#### Installing Python:
- Go to the official Python website at https://www.python.org/downloads/
- Choose the appropriate version of Python for your operating system and download the installer.
- Run the installer and follow the on-screen instructions to complete the installation process. Make sure to add 
Python to your system PATH during the installation process.
- Once the installation is complete, open the command prompt and type python to verify that Python has been installed correctly.

#### Installing PortAudio:

- On Windows:
  - Download the pre-built PortAudio binary from the official website: http://www.portaudio.com/download.html
  - Extract the downloaded zip file to a desired location on your computer.
  - Add the path of the extracted folder to your environment variables, specifically to your PATH variable. This can be done by following these steps:
  - Open the Start menu and search for "Environment Variables".
  - Click on "Edit the system environment variables".
  - Click on the "Environment Variables" button.
  - Under "System Variables", find the "Path" variable and click "Edit".
  - Click "New" and add the path of the extracted PortAudio folder.
  - Click "OK" on all windows to save the changes.
  
- On Mac:
  - Install Homebrew
  - Once Homebrew is installed, run the command ```brew install portaudio``` in your terminal.

- On Linux:
  - Run the command ```sudo apt-get install portaudio19-dev``` in your terminal if you are using Debian/Ubuntu.
  - Run the command ```sudo dnf install portaudio-devel``` in your terminal if you are using Fedora/CentOS.

After completing the above steps, you should be able to use PortAudio in your Python projects.



### Installing FLAC:
- Open the terminal on your machine.
- Run the appropriate command for your operating system to install FLAC:
  - On Ubuntu/Debian: ```sudo apt-get install flac```
  - On Fedora: ```sudo dnf install flac```
  - On macOS with Homebrew: ```brew install flac```
  - On Windows: Download the FLAC installer from https://xiph.org/flac/download.html and run the installer.
- Once the installation is complete, you can verify that FLAC has been installed correctly by running the flac command in the terminal.

### Install VIVA
- Clone this repository:
```sh
git clone https://github.com/timoterik/viva.git
```
- Install the required packages: 
```sh
pip install -r io.dcctech.viva/requirements.txt
```
- Run the main.py file to start the virtual assistant:
```sh
python io.dcctech.viva/main.py
```

## Usage
To use VIVA, simply speak into your computer's microphone and ask it to carry out a task. VIVA will use natural 
language processing techniques to understand your command and execute the appropriate action.
You can customize the commands and responses in the config.py file. This file contains a dictionary of command phrases 
and their corresponding actions. You can add your own commands and responses to the dictionary to customize VIVA's behavior.