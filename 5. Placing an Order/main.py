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
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().log_in_button).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().username_input_box).send_keys(Guru_Data().username)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().password_input_box).send_keys(Guru_Data().password)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().click_log_in_button).click()
        time.sleep(5)
        print("User Login is successful")

    def place_order(self):
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().cart_button).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().place_order_button).click()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=Guru_Locators().name_input_box).send_keys(Guru_Data().name)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=Guru_Locators().country_input_box).send_keys(Guru_Data().country)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=Guru_Locators().city_input_box).send_keys(Guru_Data().city)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=Guru_Locators().credit_card_input_box).send_keys(Guru_Data().credit_card)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=Guru_Locators().month_input_box).send_keys(Guru_Data().month)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=Guru_Locators().year_input_box).send_keys(Guru_Data().year)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().purchase_button).click()
        time.sleep(5)
        self.driver.save_screenshot("Placing an Order Screenshot.png")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().ok_button).click()
        time.sleep(5)
        print("Item is purchase successful")

g = Guru(Guru_Data().url)

g.login()

g.place_order()