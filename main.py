from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

#wait for 10s
driver.implicitly_wait(10)

element = driver.find_element(By.ID, 'downloadButton')
element.click()