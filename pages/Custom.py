import json
import random
import string
from pathlib import Path

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

def parentPath(path):
    return Path(__file__).resolve().parent.parent / path

def randomString(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def randomNumbers(length):
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(length))

def getCredentials():
    cred_path = parentPath("data/credentials.json")
    with open(cred_path) as json_file:
        creds = json.load(json_file)
        username = creds["facility_app"]["username"]
        password = creds["facility_app"]["password"]
        return {"username": username, "password": password}

def getCurrentDate():
    current_date = datetime.now().strftime("%d-%m-%y")
    print("Current Date", current_date)
    return current_date

def getCurrentDateTime():
    current_datetime = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    print("Current Date and Time", current_datetime)
    return current_datetime

class CustomPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def generate_screenshot(self, filename):
        path = "screenshots/" + filename + ".png"
        image = parentPath(path)
        self.driver.save_screenshot(image)

    def scrollDown(self, left, top, width, height, percent):
        self.driver.execute_script("mobile: scrollGesture", {
            "left": left,
            "top": top,
            "width": width,
            "height": height,
            "direction": "down",
            "percent": percent,
        })
    def customScrollToEnd(self, scroll):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd({scroll})'
        )
    def customScrollToBegin(self, scroll):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning({scroll})'
        )
    def customScrollView(self, selector):
        element = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().descriptionContains("{selector}"))'
        )
        element.click()
    def customAccessibleClick(self, value):
        self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, value)
            )
        ).click()
    def customUiAutoIndexValue(self, index, value):
        element = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().className("android.widget.EditText").instance({index}))'
        )
        element.click()
        element.send_keys(value)
    def customXpathContain(self, contain, value):
        xpath = f'//android.widget.ScrollView/android.widget.EditText[contains(@hint, "{contain}")]'
        element = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, xpath)
            )
        )
        element.click()
        element.clear()
        element.send_keys(value)
    def customXpathBtnClick(self, label):
        element = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, f'//android.widget.Button[contains(@content-desc, "{label}")]')
            )
        )
        element.click()
    def customXpathClick(self, xpath, label):
        element = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, f'//{xpath}[contains(@content-desc, "{label}")]')
            )
        )
        element.click()