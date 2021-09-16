import requests
import speech_recognition as sr 
from botspeak import BotSpeak as bs
from facecapture import FaceCapture as fc

"""
The function ask_bot use mic as source to take user audio as input 
and perform speech recognition to convert the input audio into text formant and return it.
"""

def ask_bot():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        audio = r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        print("Listening...")
        audio = r.listen(source)        
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return "Try again"
    
"""
The function chat take user's name as a parameter then take user query(message)
and pass it to the rasa server to perform NLU using the request module to query the RASA API for a response.
"""

def chat(sender):
    bot_message=""
    while bot_message != "Bye":
        print('=' * 80)
        message=ask_bot()
        if("Try again" in message):
            print("Sorry didn't catch that. Please try again.")
            continue
        print(sender+": "+message)
        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})
        for i in r.json():
            bot_message = i['text']
            if("name" in bot_message):
                message=sender
                r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})
                for i in r.json():
                    bot_message = i['text']
                    print("Bot: "+f"{i['text']}")
                    bs.speak(i['text'])
            else:
                print("Bot: "+f"{i['text']}")
                bs.speak(i['text'])

if __name__ == "__main__":
    sender=fc.capAndRec()
    bs.speak("Welcome.")
    chat(sender)
