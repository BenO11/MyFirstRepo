import webbrowser
import pyautogui as pg








answer = pg.prompt(
"""
Which Team site would you like to go to?
a) Golf
b) Tenns b Team

"""
    )

if answer == "Golf":
    webbrowser.open("www.gcds.net/tiger-athletics/schedule/team-page/~athletics-team-id/56")

elif answer == "Tennis b Team":
    webbrowser.open("www.gcds.net/tiger-athletics/schedule/team-page/~athletics-team-id/113")
    
