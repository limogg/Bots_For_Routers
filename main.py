from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



driver.get("https://www.saucedemo.com/?ref=hackernoon.com")

#wait for 30s in cant find element it is setup for whole project ;)
driver.implicitly_wait(30)

user_id = driver.find_element(By.ID, 'user-name')
user_password = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')

user_id.send_keys('standard_user')
user_password.send_keys('secret_sauce')
login_button.click()