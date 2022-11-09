import pyautogui
import time
import os
time.sleep(1)
pyautogui.alert('Open chrome! click ok once you opened it.')
pyautogui.hotkey('ctrl', 't')
pyautogui.typewrite('images.google.com')
pyautogui.hotkey('enter')
time.sleep(1.5)
pyautogui.typewrite('bored ape nft', interval=0.07)
pyautogui.hotkey('enter')
time.sleep(1.5)
pyautogui.screenshot('NFTS.png')
pyautogui.alert('Successfully screenshotted NFTs!')
