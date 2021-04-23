import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia


listener = sr.Recognizer()
alexa = pyttsx3.init()

voices = alexa.getProperty('voices')
alexa.setProperty('voice', 'english')

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    for cmd in ['a.wav', 'c.wav', 'd.wav']:
        with sr.AudioFile(cmd) as source:
            print('Device is listening, please speak...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
        yield command

def run_alexa():

    for command in take_command():
        talk(command)

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            talk('Current time is ' + time)
        elif 'how are you' in command:
            info = "I am Fine."
            print(info)
            talk(info)
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'tell me about' in command:
            wiki = command.replace('tell me about', '')
            info = wikipedia.summary(wiki, 2)
            print(info)
            talk(info)
        else:
            talk('Sorry I didnot get your question, I can search it from google')
            pywhatkit.search(command)

run_alexa()
