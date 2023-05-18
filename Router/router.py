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
    def open_starting_site(self, default_ip):
        default_ip = default_ip
        driver.get(default_ip)
        self.auto_gui.login_to_site()


    #Seek for navbar than change to his frame
    def switch_to_navbar(self):
        driver.switch_to.default_content()
        frame = driver.find_element(By.XPATH, '/html/frameset/frame[2]')
        driver.switch_to.frame(frame)

        #switch to main content for all actions
    def switch_to_main(self):
        driver.switch_to.default_content()
        frame = driver.find_element(By.XPATH, '/html/frameset/frame[3]')
        driver.switch_to.frame(frame)



    #switch to frame and go to interface setup
    def go_and_set_interface(self, PPoE, password, vlan):
        ppoe = PPoE
        password = password
        vlan = vlan

        interface = driver.find_element(By.XPATH, '//*[@id="mainnavibar"]/td[1]/a')
        interface.click()

        self.switch_to_main()

        choose_ppoe = driver.find_element(By.XPATH, '/html/body/form/div/div[2]/table[1]/tbody/tr[4]/td[5]/input')
        choose_ppoe.click()

        choose_vlan = driver.find_element(By.XPATH, '//*[@id="div_8021q"]/table/tbody/tr[2]/td[5]/input[1]')
        choose_vlan.click()

        pass_vlan = driver.find_element(By.XPATH, '//*[@id="div_8021q"]/table/tbody/tr[3]/td[5]/input')
        pass_vlan.send_keys(vlan)

        pass_username = driver.find_element(By.XPATH, '//*[@id="div_isp2"]/table/tbody/tr[2]/td[5]/input')
        pass_username.send_keys(ppoe)

        pass_pasword = driver.find_element(By.XPATH, '//*[@id="div_isp2"]/table/tbody/tr[4]/td[5]/input')
        pass_pasword.send_keys(password)

        set_ip_adress = driver.find_element(By.XPATH, '//*[@id="div_ipv4getip"]/table/tbody/tr[2]/td[5]/input[2]')
        set_ip_adress.click()

        #comented for easier work
        # save_interface = driver.find_element(By.XPATH, '/html/body/form/div/div[2]/table[3]/tbody/tr/td[3]/input[1]')
        # save_interface.click()



