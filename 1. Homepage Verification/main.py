# main

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Test_Data.data import Guru_Data
from Test_Locators.locators import Guru_Locators
import time

class Guru:
   
    def __init__(self, url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)
   
    def homepage_verification(self):
        self.driver.implicitly_wait(10)
        print("Homepage loads successfully")
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().home_button).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().website_logo).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().categories).click()
        time.sleep(5)
        print("Select & Check for the presence of Home button, Website logo, and categories")
        self.driver.save_screenshot("Homepage Verification Screenshot.png")

g = Guru(Guru_Data().url)

g.homepage_verification()