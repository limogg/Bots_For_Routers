import Router.constants as const
import pyautogui
import time



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