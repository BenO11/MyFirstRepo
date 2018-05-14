import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak(".")




"""speak.Speak("What's your favorite color.")

answer = pg.prompt("Enter your favorite color.")

if answer == "orange":
    speak.Speak("My favorite color is orange too!")

elif answer == "blue":
    speak.Speak("Blue is for nerds.")

else:
    speak.Speak("You like the color " + answer)



speak.Speak("What kind of video should we watch")

video = pg.prompt("Enter video below.")

speak.Speak("OK, let's look for " + video + " on YouTube and see what we find.")

wb.open("https://www.youtube.com/results?search_query=" + video)
"""
