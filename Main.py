import pyautogui
import time
from pynput import keyboard
import threading


def runyes():  
    imageBoxGreen = pyautogui.locateOnScreen('FindAndClickZoom\GreenCheck.PNG')
    imageBoxGreen2 = pyautogui.locateOnScreen('FindAndClickZoom\GreenCheck2.PNG')
    if( imageBoxGreen != None):
        pyautogui.click(imageBoxGreen.left + imageBoxGreen.width/2,imageBoxGreen.top + imageBoxGreen.height/2)
    elif( imageBoxGreen2 != None):
        pyautogui.click(imageBoxGreen2.left + imageBoxGreen2.width/2,imageBoxGreen2.top + imageBoxGreen2.height/2)
    else:
        print('There is no yes key on current monitor')

def runno():
    imageBoxRed = pyautogui.locateOnScreen('FindAndClickZoom\RedCheck.PNG')
    imageBoxRed2 = pyautogui.locateOnScreen('FindAndClickZoom\RedCheck2.PNG')
    if( imageBoxRed != None):
        pyautogui.click(imageBoxRed.left + imageBoxRed.width/2,imageBoxRed.top + imageBoxRed.height/2)
    elif(imageBoxRed2 != None):
        pyautogui.click(imageBoxRed2.left + imageBoxRed2.width/2,imageBoxRed2.top + imageBoxRed2.height/2)
    else:
        print('There is no yes key on current monitor')

def runexit():
    exit()

# Hotkeys
with keyboard.GlobalHotKeys({
        '1': runyes,
        '2': runno,
        '3': runexit}) as h:
    h.join()
