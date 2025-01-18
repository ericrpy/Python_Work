import pyautogui as py
import time
import schedule

py.PAUSE = 3

def testegeral ():
    for _ in range(2):
        py.press('win')
        py.press('enter')
        py.write('calc')
        py.press('enter')
        py.click(x=1143, y=179)
    py.doubleClick(x=37, y=42)    
    time.sleep(3)
    py.click(x=1894, y=8)
    time.sleep(3)

schedule.every(5).seconds.do(testegeral)
while True:
    schedule.run_pending()
    time.sleep(3)