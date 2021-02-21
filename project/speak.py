
import pyttsx3
import os
import pygame as p


class Speak:
    @staticmethod
    def speak():
        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('rate', 170)
        speak.setProperty('voice', voices[1].id)
        speak.say("A warm welcome Dear, My name is LARA the chess engine, Created by Shahid Ansari from Attain U "
                  "Subrahmanyan Batch, Hope you will like my welcome greeting and will enjoy LARA the chess engine "
                  "with background music")
        speak.runAndWait()
        speak.stop()

    @staticmethod
    def sound():  # extra work
        p.mixer.music.load(os.path.join("sounds", "background.ogg"))
        p.mixer.music.play(-1)
