import pickle

from selenium import webdriver
from selenium.webdriver import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver.v2 as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from urllib.parse import urlparse
import re
import random
import requests
from bs4 import BeautifulSoup
import time
import os
import warnings
import json, base64
from fake_useragent import UserAgent
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# options.add_argument('--proxy-server=%s' % pr)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-popup-blocking")
options.add_argument(f"user-agent={userAgent}")
options.add_argument("--disable-notifications")
from pprint import pformat
driver = uc.Chrome()


# def captcha():
#     element = browser.find_element_by_css_selector('#px-captcha')
#     action = ActionChains(browser)
#     click = ActionChains(browser)
#     action.click_and_hold(element)
#     action.perform()
#     time.sleep(10)
#     action.release(element)
#     action.perform()
#     time.sleep(0.2)
#     action.release(element)


def signin():  # Only use this function if you are using new instances of your browser each time

    driver.get('https://www.chegg.com/auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2F')



    cookies = pickle.load(open(r"cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
        # print(cookie)
    time.sleep(2)
    driver.get('https://www.chegg.com/auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2F')
    time.sleep(2)
    driver.get('https://www.chegg.com/homework-help/Electric-Circuits-10th-edition-chapter-8-problem-5P-solution-9780133760033')

    # while True:
    #     try:
    #         time.sleep(2)
    #         email_elem = browser.find_element_by_id('emailForSignIn')
    #
    #         email_elem.send_keys('s.m.d.bro.100@gmail.com')
    #
    #         time.sleep(2)
    #
    #         password_elem = browser.find_element_by_id('passwordForSignIn')
    #
    #         password_elem.send_keys('John155!')
    #
    #
    #         browser.find_element_by_name('login').click()
    #         while True:
    #          try:
    #              captcha()
    #          except:
    #              print()
    #          time.sleep(20)
    #
    #         break
    #
    #
    #     except:
    #         # captcha()
    #
    #         print()
    #     time.sleep(1)

    # from bs4 import BeautifulSoup as bs
    # import requests
    #
    # EMAIL = "s.m.d.bro.100@gmail.com"
    # PASSWORD = "John155!"
    #
    # URL = 'https://www.chegg.com/'
    # LOGIN_ROUTE = 'auth?action=login&redirect=https%3A%2F%2Fwww.chegg.com%2F'
    #
    # HEADERS = {'User-Agent': f'{userAgent}',
    #            'origin': URL, 'referer': URL + LOGIN_ROUTE, 'Connection': 'keep-alive'}
    #
    # s = requests.session()
    #
    # login_payload = {
    #     'email': EMAIL,
    #     'password': PASSWORD,
    # }
    #
    # login_req = s.post(URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)
    #
    # print(login_req.status_code)
    #
    # cookies = login_req.cookies
    #
    # soup = bs(s.get(URL).text, 'html.parser')
    #
    # answer = 'answer.html'
    # with open(answer, "w") as file:
    #     file.write(str(soup))



if __name__ == '__main__':

    signin()
    # client.run(bot_token)
    # test comment
