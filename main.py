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

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

#wait for 30s in cant find element it is setup for whole project ;)
driver.implicitly_wait(30)

element = driver.find_element(By.ID, 'downloadButton')
element.click()

progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
print(f"{progress_element.text == 'Complete!'}")