import threading
import cv2 as cv
import keyboard
import pyautogui
from pynput.mouse import Controller


__JETT__ = "agents/jett.png"
mouse = Controller()

def __get_resolution() -> [int,int]:
    """This function gets the screen resolution of the primary display"""
    screenWidth, screenHeight = pyautogui.size()
    return screenWidth, screenHeight


def Thread_instalock(agent_filepath):
    """This wrapper function creates a new thread to handle button clicks for tkinter"""
    print(agent_filepath + " selected")
    threading.Thread(target=__instalock_Agent, args=(agent_filepath,)).start()


def __instalock_Agent(agent_filepath: str):
    """This function handles agent selection by recognizing the portrait with cv.imread, moving mouse cursor to it
    and then locks in the agent with pyautogui.click()"""
    # Pass agent image filepath into cv.imread
    image = cv.imread(agent_filepath)
    lock_in_img = cv.imread("lock_in.png")
    resolution = __get_resolution()
    # Press q on keyboard to break out of loop once agent has been locked in, in order to regain mouse control.
    while not keyboard.is_pressed('q'):
        agent = pyautogui.locateCenterOnScreen(image, region=(0, 0, resolution[0], resolution[1]), grayscale=False, confidence=0.65)
        if agent is not None:
            pyautogui.moveTo(agent)
            pyautogui.click()
            lock_in = pyautogui.locateCenterOnScreen(lock_in_img, region=(0, 0, resolution[0], resolution[1]), grayscale=False, confidence=0.5)
            pyautogui.moveTo(lock_in)
            pyautogui.click()



        

            

    

