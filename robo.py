##C:\Users\Cinthia\Desktop\chromedriver_t
#chromedriver.exe
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
def document_initialised(driver):
    return driver.execute_script("return initialised")
driver = webdriver.Chrome( )
driver.get("https://www.google.com/search?q=euro&oq=euro&aqs=chrome..69i57j0i512l2j46i512j0i512j46i512j46i199i465i512l2j0i512j46i199i465i512.1242j0j15&sourceid=chrome&ie=UTF-8")
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[3]/div/div[1]/input").send_keys(2113)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[3]/div/div[2]/input").clear()
sleep(6)
