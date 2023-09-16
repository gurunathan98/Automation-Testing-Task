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

    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().log_in_button).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().username_input_box).send_keys(Guru_Data().username)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().password_input_box).send_keys(Guru_Data().password)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().click_log_in_button).click()
        time.sleep(5)
        print("User Login is successful")
   
    def logout(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().log_out_button).click()
        time.sleep(5)
        print("Logout successful")
        self.driver.save_screenshot("Logout Screenshot.png")

g = Guru(Guru_Data().url)

g.login()

g.logout()