from Brain.AiBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Sal : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting The Sal : Wait For Few Seconds More.")


def MainExecution():

    Speak("Hello Master.")
    Speak("I'm Sal.. I'm Now On Your Service.")
    while True:

        Data = MicExecution()
        Data = str(Data)
       
        if "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
             Reply = QuestionsAnswer(Data)

        else:
               Reply = ReplyBrain(Data)
               Speak(Reply)

def ClapDetect():
        query = Tester()
        if "True-Mic" in query:
             print("")
             print(">> Clap Detected!! >>")
             print("")
             MainExecution()
        else:
             pass
        
ClapDetect()       