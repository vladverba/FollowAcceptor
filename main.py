from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closebrowser(self):from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closebrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)

        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

        # click 'not now' when asked to turn on notifications
        ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

        # "//a[@href'accounts/login']"
        # "//input[@name='username']"
        # "//input[@name='password']"

        # driver.get('https://www.instagram.com/accounts/activity/')
        # time.sleep(2)

        driver.get('https://www.instagram.com/accounts/activity/?followRequests')
        time.sleep(5)

        timedelay = random.randrange(0.69, 4.20)

        buttons = driver.find_elements_by_xpath('//button[text() = "Confirm"]')

        print(len(buttons))

        for btn in buttons:
            time.sleep(timedelay)
            btn.click()

# username and password are entered below
instagramIG = InstagramBot("USERNAMEHERE", "PASSWORDHERE")
instagramIG.login()
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)

        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

        # click 'not now' when asked to turn on notifications
        ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

        # "//a[@href'accounts/login']"
        # "//input[@name='username']"
        # "//input[@name='password']"

        # driver.get('https://www.instagram.com/accounts/activity/')
        # time.sleep(2)

        driver.get('https://www.instagram.com/accounts/activity/?followRequests')
        time.sleep(5)

        timedelay = random.randrange(0.69, 4.20)

        buttons = driver.find_elements_by_xpath('//button[text() = "Confirm"]')

        print(len(buttons))

        for btn in buttons:
            time.sleep(timedelay)
            btn.click()

#username and password are entered here
instagramIG = InstagramBot("USERNAMEHERE", "PASSWORDHERE")
instagramIG.login()



