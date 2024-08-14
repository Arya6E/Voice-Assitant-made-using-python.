import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice' , voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Aftenoon")
    else:
        speak("Good Evening")
    
    speak(" I am Jack Assistant  , How can i help u today ? ")

def takeCommand():
    #it take microfobic input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        r.pause_threshold = 1 
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
       # print(e)
        print("Say that again please...")
        return "None" 
    return query   



if __name__ == "__main__":
    speak("hi arya ")
    wishme()
    query = takeCommand().lower()

    #Logic for executing based on query 
    if 'wikipedia' in query :
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia' , '', 1)
        results = wikipedia.summary(query , sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query :
        webbrowser.open("Youtube.com")
    elif 'open google' in query :
        webbrowser.open("Google.com")    
    elif 'open stackoverflow' in query :
        webbrowser.open("Stackoverflow.com")
    elif 'open spotify' in query :
        webbrowser.open("Spotify.com")
    elif 'open spotify' in query :
        webbrowser.open("Spotify.com")    
    elif 'open maps' in query:
        webbrowser.open("google maps.com")   
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f" Sir , The time is {strTime}")
   #// elif'open code' in query:
        #//codePath = "C:\Users\\Arya Biswas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
        #os.startfile(codePath)
    elif 'open email':
         webbrowser.open("Gmail.com")