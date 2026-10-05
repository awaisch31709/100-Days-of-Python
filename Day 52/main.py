from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


USERNAME = "******"
PASSWORD = "*********"

LOGIN_URL = "https://www.instagram.com/accounts/login/"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Edge()
        self.wait = WebDriverWait(self.driver, 10)

        self.username = USERNAME
        self.password = PASSWORD

    def login(self):
        self.driver.get(LOGIN_URL)

        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='text']")
            )
        )

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='password']")
            )
        )

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        password_input.send_keys(Keys.ENTER)

        input("Press Enter to close the browser...")

bot = InstaFollower()
bot.login()