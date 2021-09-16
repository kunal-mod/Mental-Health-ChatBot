from gtts import gTTS
import playsound
import random
"""
Enter anything in the function speak to make the program say it
"""
def speak(text):
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)
    randfile = "botspeak\\sounds\\"+str(r2)+"randomtext"+str(r1) +".mp3"
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(randfile)
    playsound.playsound(randfile)

if __name__ == "__main__":
    speak("Hello World")
