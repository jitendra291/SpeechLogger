"""
This program will run on python 3.3+
dependency: 
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio
pip install SpeechRecognition
"""

import speech_recognition as sr
from .writer import WorksheetWriter


class SpeechRecognizer:

    def __init__(self):
        super().__init__()
        self.recognizer = sr.Recognizer()
        self.writer = WorksheetWriter()

    def recognize(self):
        with sr.Microphone() as source:                # using the default microphone as the audio source
            audio = self.recognizer.listen(source)
        return self.recognizer.recognize_google(audio)

    def __call__(self):
        while True:
            print("Speak:$ ")
            try:
                audio_string = self.recognize()
                print("You Spoke: {0}".format(audio_string))
                if audio_string == "goodbye":
                    break
                # TODO: Can do Some NLP processing on audio_string to do some smart processing
                # writing in the worksheet
                self.writer.write(audio_string)
            except Exception:
                print("Sorry, Could not understand audio!!")
