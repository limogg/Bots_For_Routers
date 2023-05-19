import Router.constants as const
import pyautogui
import time
import os
from PIL import Image


class Auto_Gui:
    #Use autogui to login to site without web elements
    def login_to_site(self):
        time.sleep(1)
        pyautogui.typewrite(const.admin_login)
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.typewrite(const.admin_password)
        time.sleep(1)
        pyautogui.press('enter')

    def save(self):
        time.sleep(1)
        pyautogui.press('enter')
