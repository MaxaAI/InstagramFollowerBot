from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


CHROME_DRIVER_PATH = "FILE Path"
SIMILAR_ACCOUNT = 'Account you want to follow the follower from'
USERNAME = 'Your Username'
PASSWORD = 'Your Password'
driver = webdriver.Chrome()

class InstaFollower:
    def __init__(self, path):
        s = Service(path)
        self.driver = webdriver.Chrome(service=s)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        email = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        email.send_keys(USERNAME)

        password = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password.send_keys(PASSWORD)

        time.sleep(2)

        password.send_keys(Keys.ENTER)

        time.sleep(5)

        print(self.driver.page_source)  # Print the page HTML

        time.sleep(3)

    def find_followers(self):
        time.sleep(3)

        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(3)

        try:
            followers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers'))
            )
            followers.click()
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")

    def follow(self):
        # Find all the follow buttons in the modal
        follow_button = self.driver.find_elements(By.XPATH, value="//*[text()='Follow']")
        for button in follow_button:
            button.click()
            time.sleep(2)  # Wait for a while


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
