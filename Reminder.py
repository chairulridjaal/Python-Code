import pyautogui
import time
import schedule
        
def do_remind():
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")

schedule.every(30).seconds.do(do_remind)

while 1:
    schedule.run_pending()
    time.sleep(1)
