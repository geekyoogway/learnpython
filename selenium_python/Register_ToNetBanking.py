import time
from threading import Thread

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service()

try:
    driver = webdriver.Chrome(service= service_obj)

    driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    driver.find_element(By.LINK_TEXT,"Register").click()
    driver.find_element(By.ID,"customer.firstName").send_keys("Pintusmann")
    driver.find_element(By.ID,"customer.lastName").send_keys("Pintu")
    driver.find_element(By.ID,"customer.address.street").send_keys("Hoodi")
    driver.find_element(By.ID,"customer.address.city").send_keys("bangalore")
    driver.find_element(By.ID,"customer.address.state").send_keys("karnataka")
    driver.find_element(By.ID,"customer.address.zipCode").send_keys("560048")
    driver.find_element(By.ID,"customer.phoneNumber").send_keys("8310565382")
    driver.find_element(By.ID,"customer.ssn").send_keys("9876543210")
    driver.find_element(By.ID,"customer.username").send_keys("Pintu")
    driver.find_element(By.ID,"customer.password").send_keys("kill@8080")
    driver.find_element(By.ID,"repeatedPassword").send_keys("kill@8080")
    time.sleep(3)
    driver.find_element(By.XPATH,'//input[@type="submit"]').click()


    '''Login with the newly created user'''
    driver.find_element(By.NAME,'username').send_keys("Pintu")
    driver.find_element(By.NAME, 'password').send_keys("kill@8080")
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="loginPanel"]/form/div[3]/input').click()




except:
    print("error")
