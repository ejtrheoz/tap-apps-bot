import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import time
import keyboard
import pytesseract
import random



def farm_points():

    start_time = time.time()
    while True:
                

        if time.time() - start_time > 40:
            result = click_on_text("Play")

            screen = np.array(ImageGrab.grab())
            screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

            data = pytesseract.image_to_data(screen_gray, lang='eng', output_type=pytesseract.Output.DATAFRAME)
            data = data[data.text.notnull()]
            play_data = data[data.text == 'Play']

            if play_data.empty == False:
                pyautogui.click(play_data['left'].iloc[0], play_data['top'].iloc[0])
                start_time = time.time()
            else:
                break
            

        click_with_screens_pyautogui(9)



def click_on_text(text):
    screen = np.array(ImageGrab.grab())
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    data = pytesseract.image_to_data(screen_gray, lang='eng', output_type=pytesseract.Output.DATAFRAME)
    data = data[data.text.notnull()]
    play_data = data[data.text == text]

    if not play_data.empty:
        pyautogui.click(play_data['left'].iloc[-1], play_data['top'].iloc[-1])
        time.sleep(1)
    
    return not play_data.empty


def click_with_screens_pyautogui(num):
    for i in range(9):
        pos = pyautogui.locateCenterOnScreen(f'Screenshot_{i+1}.png', grayscale=True, region=(720, 80, 500, 950), confidence=0.8)
        pyautogui.click(pos)
        pyautogui.press('esc')


def click_with_screens_opencv(num):
    for i in range(num):

        screen = np.array(ImageGrab.grab())
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(f'Screenshot_{i+1}.png', 0)


        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_loc != (0, 0) and not (max_loc[0] >= 300 and max_loc[0] <= 400):
            pyautogui.click(max_loc)
            pyautogui.press('esc')