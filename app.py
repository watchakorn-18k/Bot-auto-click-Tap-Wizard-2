from ast import keyword
import pyautogui
import time
import keyboard


        
def check_eye():
    while True:
        if pyautogui.pixelMatchesColor(x=2431,y=700,expectedRGBColor=(156,36,41)):
            pyautogui.click(x=2431,y=700)
            time.sleep(0.5)
            pyautogui.click(x=2435,y=263)
            pyautogui.click(2491,111)



def Check_Pos_Color():
    while keyboard.is_pressed('-') == False:
        x, y = pyautogui.position()
        r,g,b = pyautogui.pixel(2431,700)
        print(f"r,g,b = {r},{g},{b}")
        print(f"x,y = {x},{y}")
        # if keyboard.is_pressed('k'):
        #     open('log.txt','a').write(f"set kkkkk-{x},{y}\n")
            

# Check_Pos_Color()
check_eye()

# s = 0
# for i in range(5):
#     pyautogui.moveTo(x=2156+s,y=266)
#     s += 59
#     time.sleep(0.5)

# x,y = pyautogui.position()
# print(pyautogui.onScreen(x,y))