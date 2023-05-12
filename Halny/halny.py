import Halny.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



#wait for 30s in cant find element it is setup for whole project ;)
driver.implicitly_wait(30)


class Halny():
    def open_starting_site(self):
        driver.get(const.starting_site)

    def login(self):
        pass

    def go_to_advanced_settings(self):
        driver.implicitly_wait(30)
        go_to_internet = driver.find_element(By.XPATH(()))

