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
   
    def registration(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().sign_up_button).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().username_input_box).send_keys(Guru_Data().username)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().password_input_box).send_keys(Guru_Data().password)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().click_sign_up_button).click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        print("Registration is successful")
        self.driver.save_screenshot("Registration with valid data Screenshot.png")

g = Guru(Guru_Data().url)

g.registration()