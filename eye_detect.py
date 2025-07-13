import pyttsx3
import winsound
# import urllib.request

engine = pyttsx3.init()


class Myclass:
    def __int__(self):
        pass

    def Blink(self):
        if self == 1:
            engine.say("turning Light on")
            engine.runAndWait()
            print("Light on")
            winsound.Beep(2500, 500)  # 2500 Hz frequency for 1 second


        if self == 2:
            engine.say("Turning Light off")
            engine.runAndWait()
            print("Light off")
            winsound.Beep(2500, 500)  # 2500 Hz frequency for 1 second

        if self == 3:
            engine.say("Turning Fan on")
            engine.runAndWait()
            print("Fan on")
            winsound.Beep(2500, 500)  # 2500 Hz frequency for 1 second


        if self == 4:
            engine.say("Turning Fan off")
            engine.runAndWait()
            print("Fan off")
            winsound.Beep(2500, 500)  # 2500 Hz frequency for 1 second


        if self == 5:
            engine.say("Turning bed lamp on")
            engine.runAndWait()
            print("Bed lamp on")
            winsound.Beep(2500, 500)  # 2500 Hz frequency for 1 second


        if self == 6:
            engine.say("Turning Bed lamp off")
            engine.runAndWait()
            print("Bed lamp off")
            winsound.Beep(2500, 500)  # 2500 Hz frequency for 1 second

        if self == 7:
            engine.say("Invalid")
            engine.runAndWait()
            print("Invalid Input")
            winsound.Beep(2500, 200)  # 2500 Hz frequency for 1 second
            winsound.Beep(2500, 200)  # 2500 Hz frequency for 1 second

