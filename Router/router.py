import time
import Router.constants as const
from Router.autogui import Auto_Gui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = Options()
#debug line if you want driver to quit after setting everything just comment it
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#wait for 30s in cant find element it is setup for whole project ;)
driver.implicitly_wait(30)

class Router():
    auto_gui = Auto_Gui()
    #open starting site
    def open_starting_site(self):
        driver.get(const.starting_site)
        self.auto_gui.login_to_site()

        self.switch_to_navbar()


    #Seek for navbar than change to his frame
    def switch_to_navbar(self):
        driver.switch_to.default_content()
        frame = driver.find_element(By.XPATH, '/html/frameset/frame[2]')
        driver.switch_to.frame(frame)


    #switch to frame and go to interface setup
    def go_and_set_interface(self):
        interface = driver.find_element(By.XPATH, '//*[@id="mainnavibar"]/td[1]/a')
        interface.click()

