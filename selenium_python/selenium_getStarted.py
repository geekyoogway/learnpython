from selenium import webdriver
from selenium.webdriver.chrome.service import Service

'''Chrome Driver
Driver needs to be added . Because its acts as a middle layer for communication from code to Chrome server
Responsible to start the chrome browser
A Service class that is responsible for the starting and stopping of `chromedriver`.
If system doesn't have chrome driver. Service automatically get the latest '''
service_obj = Service()

'''What if I want to select the older version 
place the chrome driver in local and give that path in 
Service("/path/to/chrome/driver")
Download chrome driver from google'
'''

driver = webdriver.Chrome(service=service_obj)

driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")


"just to keep to open"
while(True):
    pass