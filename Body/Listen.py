from playsound import playsound
import speech_recognition as sr
from googletrans import Translator

#Listen languages
def Listen():


    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="si") #input voice sinhala

    except:
        return ""

    query = str(query).lower()
    return query

#Translation
def TranslationToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = (result.text)
    print(f"You : {data}.")
    return data

#connect
def MicExecution():
    query = Listen()
    data = TranslationToEng(query)
    return data
