# pip3 install pyautogui
# pip3 install Image
# pip3 install pywinauto


import pyautogui
import time
import pyperclip


# kakao = pyautogui.locateOnScreen('/Users/sangjin/Desktop/osj/Algorithm-Practice/hobby/kakao.png')
# print(kakao)
#
# pyautogui.click(kakao)
# pyautogui.click(kakao)

pyautogui.click()
time.sleep(0.5)
pyautogui.hotkey('command', 'space')
pyautogui.hotkey('backspace')
time.sleep(0.5)
pyperclip.copy('kakao')
pyautogui.hotkey("command", "v")
time.sleep(0.5)
pyautogui.hotkey('enter')
time.sleep(0.5)
pyautogui.hotkey('command', "2")
time.sleep(0.5)
pyautogui.hotkey('command', 'f')
pyautogui.hotkey('backspace')
time.sleep(1)
pyperclip.copy('오상진')
pyautogui.hotkey("command", "v")
time.sleep(0.5)
pyautogui.hotkey('down')
time.sleep(0.5)
pyautogui.hotkey('enter')
time.sleep(0.5)
ham = pyautogui.locateOnScreen('/Users/sangjin/Desktop/osj/Algorithm-Practice/hobby/kakao.png')
pyautogui.click(ham)


