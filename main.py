from ast import keyword
import pyautogui
import time
import keyboard
import threading

def GetpositionMouse():
    x,y = pyautogui.position()
    # print(x,y)
    return x,y
def FixAFK():
    while True:
        a = GetpositionMouse()
        b = a
        if pyautogui.pixelMatchesColor(2455,630, (119, 0, 112)):
            pyautogui.mouseDown(x=2455, y=630,button='left')
            pyautogui.mouseUp(x=2455, y=630,button='left')
            pyautogui.moveTo(b)

def checkResearch():
    while keyboard.is_pressed('-') == False:
        a = GetpositionMouse()
        b = a
        if pyautogui.pixelMatchesColor(x=2157,y=786,expectedRGBColor=(33,138,19)) or pyautogui.pixelMatchesColor(x=2157,y=786,expectedRGBColor=(35,127,133)):
            pyautogui.click(x=2190,y=761)
            time.sleep(0.5)
            count = 0
            try:
                for i in range(5):
                    while True:
                        if pyautogui.pixelMatchesColor(x=2156+count,y=266,expectedRGBColor=(29,39,99)) or pyautogui.pixelMatchesColor(x=2156+count,y=266,expectedRGBColor=(33,138,19)):
                            pyautogui.click(x=2156+count,y=266)
                            time.sleep(0.5)
                            if count == 236:
                                if not pyautogui.pixelMatchesColor(x=2332,y=439,expectedRGBColor=(127,127,127)):
                                    pyautogui.click(2306,440)
                                else:
                                    pyautogui.click(2491,111)
                            else:
                                if not pyautogui.pixelMatchesColor(x=2332,y=437,expectedRGBColor=(127,127,127)):
                                    pyautogui.click(2305,429)
                        count += 59
                pyautogui.click(2491,111)
            except:
                pass
            pyautogui.click(2491,111)
            pyautogui.moveTo(b)
            # time.sleep(60*10)


def Check_Pos_Color():
    while keyboard.is_pressed('-') == False:
        x, y = pyautogui.position()
        r,g,b = pyautogui.pixel(2168,-46)
        print(f"r,g,b = {r},{g},{b}")
        print(f"x,y = {x},{y}")

def Check_Shard():
    while True:
        pyautogui.click(2228,749)
        time.sleep(0.5)
        pyautogui.click(2301,396)
        time.sleep(1800)

def check_eye():
    while True:
        if pyautogui.pixelMatchesColor(x=2431,y=700,expectedRGBColor=(156,36,41)):
            pyautogui.click(x=2431,y=700)
            time.sleep(0.5)
            pyautogui.click(x=2435,y=263)
            pyautogui.click(2491,111)
        time.sleep(1800)
        

t1 = threading.Thread(target=FixAFK).start()
t3 = threading.Thread(target=check_eye).start()
time.sleep(2)
t2 = threading.Thread(target=Check_Shard).start()
time.sleep(2)
t2 = threading.Thread(target=checkResearch).start()
