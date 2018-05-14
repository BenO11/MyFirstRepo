# Helps people who are sad become happy

import pyautogui as pg
import webbrowser
import time

answer = pg.confirm(text="How are you feeling today?", title="Choose your mood", buttons=['Happy', 'Indifferent', 'Sad', 'Mad', 'Afraid'])

if answer == "Happy":
    webbrowser.open("https://www.google.com/search?q=good+for+you+thumbs+up+pics&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjCoMH1w63aAhXLjVkKHX_KBt0Q_AUICigB&biw=1366&bih=637#imgrc=3sb-iDjrvRikvM:")

elif answer == "Indifferent":
        webbrowser.open("https://www.google.com/search?q=cool&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwimn6rNkL_aAhWSVt8KHUAQB7cQ_AUICigB&biw=1366&bih=637#imgrc=I7ou0iBEX_Fz3M:")
        
elif answer == "Sad":
    webbrowser.open("https://www.google.com/search?q=victory+royale&rlz=1C1GCEA_enUS752US752&tbm=isch&source=lnt&tbs=itp:animated&sa=X&ved=0ahUKEwiApIOQkb_aAhVEwlkKHSUwByYQpwUIHg&biw=1366&bih=637&dpr=1#imgrc=RMFTfOC5S-a94M:")

elif answer == "Mad":
    webbrowser.open("https://www.google.com/search?q=funny+falling+gifs&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj02I3foeLaAhUsw1kKHRRcBBEQ_AUICigB&biw=1707&bih=796&dpr=0.8#imgrc=328dPyNpFf_1xM:")

elif answer == "Afraid":
    webbrowser.open("https://www.google.com/search?q=memes+that+won%27t+make+you+afraid&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjFtKeiouLaAhXCx1kKHRQRCSQQ_AUICigB&biw=1707&bih=796#imgrc=2HFdwRwWRXDd1M:")
