import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognisor = sr.Recognizer()
engine = pyttsx3.init()
newsapi=""
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    #  speak("i am fine ")
     if(c.lower()=="open google"):
            webbrowser.open("https://google.com")
     elif(c.lower()=="open youtube"):
            webbrowser.open("https://youtube.com")
     elif(c.lower()=="open facebook"):
            webbrowser.open("https://facebook.com")
     elif(c.lower()=="open instagram"):
            webbrowser.open("https://instagram.com")
     elif(c.lower()=="open linkdin"):
            webbrowser.open("https://linkdin.com")
     elif(c.lower().startswith("play")):
            song=c.lower().split(" ")[1]
            link=musiclibrary.music[song]
            webbrowser.open(link)
     elif (c.lower()=="game"):
            response=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
      # Check if the request was successful (status code 200)   
            if response.status_code == 200:
        # Parse JSON response
              data = response.json()

        # Extract and print headlines
            
              articles = data.get("articales",[])
              for article in articles:
                   speak(article["title"])  


     else:
          # further open ai handle the request
          pass
            
if __name__ ==  "__main__":
      speak("Initializing harshal assistant..")

      recognizer = sr.Recognizer()
while(True):

    try:
        # Use the microphone as the source of input
          with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source,2)
            print("Recognizing....")
        # Recognize speech using Google Speech Recognition
            word = recognizer.recognize_google(audio)
            if(word.lower()=="harshal"):
                speak("yes")
                # command
          with sr.Microphone() as source:
                  print("Harshal activate")
                  audio = recognizer.listen(source)
                  command=recognizer.recognize_google(audio)

                  processcommand(command)

    except sr.UnknownValueError:
         print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
