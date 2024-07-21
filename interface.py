from pattern import *
import cv2
from PIL import ImageGrab
import pytesseract
import pyautogui
from PIL import Image
import os
import subprocess
import time
import clicker

result = input("Choose one of variants (enter number):\n1)Simple clicker\n2)Pattern writer (RandomClicker)\n3)Pattern writer (ForwardClicker)\n4)Pattern writer (FrequencyClusterClicker)")

try:
    variant = int(result)
except:
    print("You entered something wrong")


if variant == 1:
    screen_width, screen_height = pyautogui.size()


    for i in range(8):
        proc = subprocess.Popen([rf"C:\Users\Илья\Desktop\telegrams\{i+1}\Telegram.exe"])
        time.sleep(5)


        clicker.click_on_text('Blum')
        clicker.click_on_text('Claim')
        clicker.click_on_text('Claim')
        time.sleep(7)
        clicker.click_on_text('Continue')
        clicker.click_on_text('Claim')

        pyautogui.moveTo(screen_width / 2, screen_height / 2)
        time.sleep(1)
        pyautogui.scroll(-100)

        clicker.click_on_text('Start')
        loc = pyautogui.locateCenterOnScreen('play.png', grayscale=True, region=(720, 80, 500, 950), confidence=0.7)
        if loc is not None:
            pyautogui.click(loc[0]+10, loc[1])
            clicker.farm_points()

        proc.terminate()
else:
    try:
        delay = int(input("Enter clicking delay"))
    except:
        print("You entered clicking delay wrong")
    else:
        pattern_writer = None
        if variant == 2:
            pattern_writer = RandomClicker(delay)
        if variant == 3:
            pattern_writer = ForwardClicker(delay)
        if variant == 4:
            pattern_writer = FrequencyClusterClicker(delay)
        
        try:
            clicking_time = input("Enter recording time")
        except:
            print("You entered delay wrong")
        else:
            input("Enter any key to start recording ")
            pattern_writer.record_positions(clicking_time)
            input("Enter any key to play recorded pattern")
            pattern_writer.play_clicks(clicking_time)
    
