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
    def go_and_set_interface(self, PPpoE, password, vlan):
        pppoe = PPpoE
        password = password
        vlan = vlan

        interface = driver.find_element(By.XPATH, '//*[@id="mainnavibar"]/td[1]/a')
        interface.click()

        self.switch_to_main()

        choose_pppoe = driver.find_element(By.XPATH, '/html/body/form/div/div[2]/table[1]/tbody/tr[4]/td[5]/input')
        time.sleep(0.2)
        choose_pppoe.click()

        choose_vlan = driver.find_element(By.XPATH, '//*[@id="div_8021q"]/table/tbody/tr[2]/td[5]/input[1]')
        time.sleep(0.2)
        choose_vlan.click()

        pass_vlan = driver.find_element(By.XPATH, '//*[@id="div_8021q"]/table/tbody/tr[3]/td[5]/input')
        pass_vlan.clear()
        time.sleep(0.2)
        pass_vlan.send_keys(vlan)

        pass_username = driver.find_element(By.XPATH, '//*[@id="div_isp2"]/table/tbody/tr[2]/td[5]/input')
        pass_username.clear()
        time.sleep(0.2)
        pass_username.send_keys(pppoe)

        pass_pasword = driver.find_element(By.XPATH, '//*[@id="div_isp2"]/table/tbody/tr[4]/td[5]/input')
        pass_pasword.clear()
        time.sleep(0.2)
        pass_pasword.send_keys(password)

        set_ip_adress = driver.find_element(By.XPATH, '//*[@id="div_ipv4getip"]/table/tbody/tr[2]/td[5]/input[2]')
        time.sleep(0.2)
        set_ip_adress.click()

        save = driver.find_element(By.XPATH, '/html/body/form/div/div[2]/table[3]/tbody/tr/td[3]/input[1]')
        save.click()

    #set second interface for tv
    def set_interface_for_tv(self, tv_vlan):
        tv_vlan = tv_vlan
        wan_number = '2'

        interface = driver.find_element(By.XPATH, '//*[@id="mainnavibar"]/td[1]/a')
        interface.click()
        self.switch_to_main()

        change_wan = driver.find_element(By.XPATH, '/html/body/form/div/table/tbody/tr[5]/td[5]/select')
        change_wan.click()
        self.auto_gui.change_wan(wan_number)

        make_active = driver.find_element(By.XPATH, '/html/body/form/div/table/tbody/tr[6]/td[5]/input[1]')
        make_active.click()

        select_tag = driver.find_element(By.XPATH, '//*[@id="div_8021q"]/table/tbody/tr[2]/td[5]/input[1]')
        select_tag.click()

        type_vlan = driver.find_element(By.XPATH, '//*[@id="div_8021q"]/table/tbody/tr[3]/td[5]/input')
        type_vlan.get_attribute('text')
        type_vlan.clear()
        time.sleep(0.2)
        type_vlan.click()
        #type_vlan.clear()
        #self.wait_for_allert_than_click()
        self.auto_gui.send_keys_to_input(tv_vlan)


        save_wan = driver.find_element(By.XPATH, '/html/body/form/div/div[2]/table[3]/tbody/tr/td[3]/input[1]')
        save_wan.click()

    #set port binding for tv
    def set_port_binding(self):
        go_to_advanced = driver.find_element(By.XPATH, '//*[@id="mainnavibar"]/td[2]/a')
        go_to_advanced.click()

        go_to_port_binding = driver.find_element(By.XPATH, '//*[@id="subnavibar"]/td[5]/a')
        go_to_port_binding.click()

        self.switch_to_main()

    def set_wifi(self, client_id, password, GHz, Xpath):
        Xpath = Xpath
        GHz = GHz
        client_id = client_id
        password = password

        if GHz == True:
            wifi_name = 'siec_' + client_id+'_5Ghz'
        else:
            wifi_name = 'siec_'+client_id

        wifi = driver.find_element(By.XPATH, Xpath)
        wifi.click()
        self.switch_to_main()

        set_wifi_name = driver.find_element(By.XPATH, '/html/body/form/div/table[2]/tbody/tr[3]/td[5]/input[3]')
        set_wifi_name.clear()
        set_wifi_name.send_keys(wifi_name)

        set_wifi_password = driver.find_element(By.XPATH, '//*[@id="WPAPSKWPA2PSK_div"]/table/tbody/tr[3]/td[5]/input')
        set_wifi_password.clear()

        #wait for error window than accept it
        wait = WebDriverWait(driver,20)
        alert = wait.until(EC.alert_is_present())
        time.sleep(1)
        alert.accept()
        time.sleep(1)

        set_wifi_password.send_keys(password)

        self.auto_gui.save()

    #set Acl
    def set_ACL(self):
        acl = driver.find_element(By.XPATH, '//*[@id="mainnavibar"]/td[3]/a')
        acl.click()

        acl_navbar = driver.find_element(By.XPATH, '//*[@id="subnavibar"]/td[5]/a')
        acl_navbar.click()

        self.switch_to_main()

        acl_click = driver.find_element(By.XPATH, '/html/body/table[1]/tbody/tr[3]/td[5]/input[4]')
        acl_click.click()

        acl_pass_port = driver.find_element(By.XPATH, '//*[@id="idWebMgmtWanPort"]')
        acl_pass_port.clear()
        acl_pass_port.send_keys(const.port)

        acl_set = driver.find_element(By.XPATH,'/html/body/table[1]/tbody/tr[8]/td[3]/input[2]')
        time.sleep(1)
        acl_set.click()

    #wait for alert than click it
    def wait_for_allert_than_click(self):
        # wait for error window than accept it
        wait = WebDriverWait(driver, 20)
        alert = wait.until(EC.alert_is_present())
        time.sleep(1)
        alert.accept()
        time.sleep(1)






