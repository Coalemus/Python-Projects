#!/bin/zsh
# source: youtube.com/watch?v=jBxRGcDmfWA

# pain.txt
# /home/joey/Joey-Repositories/Python-Projects/completed/spambot/pain.txt

# navyspam.txt
# /home/joey/Joey-Repositories/Python-Projects/completed/spambot/navyspamtext.txt

import pyautogui, time
time.sleep(5)
f = open("/home/joey/Joey-Repositories/Python-Projects/completed/spambot/pain.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")


