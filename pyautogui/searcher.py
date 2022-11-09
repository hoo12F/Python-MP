import pyautogui
import time


def search():
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite(searchPrompt)
    pyautogui.hotkey('enter')


pyautogui.alert('Please open chrome. Click "OK" Once you have opened chrome.')
pyautogui.hotkey('ctrl', 't')
searchPrompt = str(pyautogui.prompt('What do you want to search?'))
search()
