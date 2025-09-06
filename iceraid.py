from pynput import keyboard
import pyautogui
import time
import threading

x = True
p = "Listener"

def on_activate_p():
    global click_thread
    click_thread = threading.Thread(target=raid_script)
    click_thread.daemon = True 
    click_thread.start()


def raid_script():
    global x
    pyautogui.keyDown('s')
    time.sleep(0.9)
    pyautogui.keyUp('s')
    pyautogui.keyDown('d')
    time.sleep(0.3)
    pyautogui.keyUp('d')
    pyautogui.keyDown('e')
    time.sleep(0.5)
    pyautogui.keyUp('e')
    pyautogui.click(511, 352)
    pyautogui.typewrite('ice', interval=0.1)
    time.sleep(1)
    pyautogui.moveTo(1229, 490)
    time.sleep(0.5)
    pyautogui.click(1228, 490, clicks= 4, interval= 0.1, button='left')
    time.sleep(30)
    pyautogui.press(['r', 't', 'h'])
    pyautogui.press('3')
    time.sleep(18)
    pyautogui.keyDown('s')
    time.sleep(0.3)
    pyautogui.keyUp('s')
    pyautogui.click(1030, 550, clicks=70, interval=0.2, button='left')
    time.sleep(23)
    pyautogui.moveTo(1000, 730)
    pyautogui.click(1000, 730, clicks=2, interval=0.2, button='left')
    time.sleep(5)
    while x:
        pyautogui.keyDown('a')
        time.sleep(0.9)
        pyautogui.keyUp('a')
        pyautogui.keyDown('e')
        time.sleep(0.5)
        pyautogui.keyUp('e')
        pyautogui.click(511, 352)
        pyautogui.typewrite('ice', interval=0.2)
        time.sleep(1)
        pyautogui.moveTo(1229, 490)
        time.sleep(0.5)
        pyautogui.click(1228, 490, clicks= 4, interval= 0.1, button='left')
        time.sleep(30)
        pyautogui.press(['r', 't', 'h'])
        pyautogui.press('3')
        time.sleep(18)
        pyautogui.keyDown('s')
        time.sleep(0.3)
        pyautogui.keyUp('s')
        pyautogui.click(1030, 550, clicks=80, interval=0.2, button='left')
        time.sleep(23)
        pyautogui.moveTo(1000, 730)
        pyautogui.click(1000, 730, clicks=2, interval=0.2, button='left')
        time.sleep(5)
    print("Exhale")

def on_activate_l():
    global p
    p.stop()

with keyboard.GlobalHotKeys({
    'p': on_activate_p,
    'l': on_activate_l}) as p:
   p.join()

