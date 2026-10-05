from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PROMISED_DOWN = 150
PROMISED_UP = 200


TWITTER_EMAIL = "awaisch31709@gmail.com"
TWITTER_PASSWORD = "Asjdcnfgt@3132AS"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Edge()
        self.wait = WebDriverWait(self.driver, 30)

        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Start Speedtest
        start_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[aria-label='start speed test']")
            )
        )

        start_button.click()

        print("Speed test started...")

        # Give Speedtest enough time to complete
        time.sleep(90)

        # Download speed
        download_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='download-speed']")
            )
        )

        # Upload speed
        upload_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='upload-speed']")
            )
        )

        self.down = float(download_element.text)
        self.up = float(upload_element.text)

        print(f"Download speed: {self.down} Mbps")
        print(f"Upload speed: {self.up} Mbps")

    def tweet_at_provider(self):

        self.driver.get("https://x.com/i/flow/login")

        print("Opening X login...")

        # Email / username
        email_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "text")
            )
        )

        email_input.send_keys(TWITTER_EMAIL)

        next_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='Next']")
            )
        )

        next_button.click()

        # Password
        password_input = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "password")
            )
        )

        password_input.send_keys(TWITTER_PASSWORD)

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='Log in']")
            )
        )

        login_button.click()

        print("Logged into X.")

        time.sleep(5)

        # Open post composer
        post_box = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[contenteditable='true']")
            )
        )

        tweet = (
            f"Hey Internet Provider, my internet speed is slower than promised. "
            f"My download speed is {self.down:.2f} Mbps and my upload speed is "
            f"{self.up:.2f} Mbps. My promised speeds are "
            f"{PROMISED_DOWN} Mbps download and "
            f"{PROMISED_UP} Mbps upload."
        )

        post_box.send_keys(tweet)

        print("Tweet composed.")

        # Post tweet
        post_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']")
            )
        )

        post_button.click()

        print("Tweet posted successfully!")

        time.sleep(5)


speed = InternetSpeedTwitterBot()

speed.get_internet_speed()
speed.tweet_at_provider()