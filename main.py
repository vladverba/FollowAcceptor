
# Accept Instagram followers through Selenium & Chrome

import time
import random
import pickle
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Progress bar helps visualize how much of task is complete


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    print('[%s] %s%s %s\r' % (bar, percents, '%', status))
    return percents


class InstagramBot:

    def __init__(self, username=None, password=None, cookies=None, proxy=None):
        """
        Login using cookies or login info (email+pw)
        :param cookies: cookies pickle file (probably on Cookies folder!) e.g. 'Cookies/cookies2.pkl'
        :param login: (email, password) string tuple
        """

        chrome_options = webdriver.ChromeOptions()

        if proxy:
            chrome_options.add_argument('--proxy-server=%s' % proxy)
            print("Using proxy = {}".format(proxy))

        # paste your path for webdriver here
        self.driver = webdriver.Chrome('YOUR/WEBDRIVER/PATH')

        # if cookies saved, log in with cookies
        if cookies:
            print("Using cookie = " + cookies)
            self.driver.get("http://www.instagram.com/")
            cookies2 = pickle.load(open(cookies, "rb"))
            for cookie in cookies2:
                self.driver.add_cookie(cookie)

        elif username and password:
            self.username = username
            self.password = password
            self.driver.get('https://www.instagram.com/accounts/login/')

            time.sleep(2)
            user_name_elem = self.driver.find_element_by_xpath("//input[@name='username']")
            user_name_elem.clear()
            user_name_elem.send_keys(username)

            password_elem = self.driver.find_element_by_xpath("//input[@name='password']")
            password_elem.clear()
            password_elem.send_keys(password)

            password_elem.send_keys(Keys.RETURN)

        else:
            raise Exception("Wrong parameters for InstagramBot - either use cookies or email+password")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.closebrowser()

    def closebrowser(self):
        self.driver.close()

    def acceptFollows(self):

        driver = self.driver

        try:
            # click 'not now' when asked to turn on notifications
            ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
        except:
            print("Turn ON Notifications Dialog not found")

        driver.get('https://www.instagram.com/accounts/activity/?followRequests')
        time.sleep(15)

        buttons = driver.find_elements_by_xpath('//button[text() = "Confirm"]')

        print(len(buttons))

        for index, btn in enumerate(buttons):
            time.sleep(0.69+round(random.random()*3, 3))
            progress(index, len(buttons))
            btn.click()


# enter username and password here
with InstagramBot(username="USERNAME", password="PASSWORD") as bot:
    bot.acceptFollows()
