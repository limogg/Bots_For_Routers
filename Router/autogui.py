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

    #used to save when cant find xpath or dont work but pressing enter work
    def save(self):
        time.sleep(1)
        pyautogui.press('enter')

    #used to change wan options other dont work
    def change_wan(self, wan_to_set):
        wan_to_set = wan_to_set
        pyautogui.press(wan_to_set)
        time.sleep(0.2)
        pyautogui.press('enter')

    #send key to input when nothing else works
    def send_keys_to_input(self, text):
        text = text
        #select all to delete
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.2)
        # clear old input
        pyautogui.press('delete')
        pyautogui.typewrite(text)
        time.sleep(0.2)


