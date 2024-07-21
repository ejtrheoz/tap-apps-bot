import cv2
from PIL import ImageGrab
import pytesseract
import pyautogui
from PIL import Image
import os
import subprocess
import time
import clicker


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



