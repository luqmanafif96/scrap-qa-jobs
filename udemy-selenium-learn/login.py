# first learn the python for automation test
# Open browser
# version selenium 4

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# set the browser to chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# to stop 


#  Go to webpage

driver.get("https://practicetestautomation.com/practice-test-login/")

#  


time.sleep(5)
print("driver closes")