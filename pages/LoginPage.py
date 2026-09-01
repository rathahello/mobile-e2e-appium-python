import json
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from appium.webdriver.extensions.android.nativekey import AndroidKey
from pages.Custom import CustomPage


class TestLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.custom_page = CustomPage(self.driver)

    def signInBtn(self, label):
        self.custom_page.customAccessibleClick(label)

    def enterLoginForm(self, username, password):
        enter_username = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(0)'
        )
        enter_username.click()
        enter_username.clear()
        enter_username.send_keys(username)

        enter_password = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").instance(1)'
        )
        enter_password.click()
        enter_password.send_keys(password)
        self.driver.press_keycode(AndroidKey.BACK)
        self.driver.find_element( AppiumBy.XPATH, '//android.widget.Button[@content-desc="Sign in"]').click()

    def userLoginSuccessful(self, username, password):
        try:
            self.enterLoginForm(username, password)
            time.sleep(3)
            actual_msg = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, 'Home'
            )
            assert actual_msg.is_displayed()
            print("Login Successful")
        except Exception as error:
            print("Login Failed", error)

    def userLoginInvalidCred(self, username, password, expected_msg):
        try:
            self.enterLoginForm(username, password)
            time.sleep(3)
            response_message = self.driver.find_element(
                AppiumBy.XPATH,
                f'//android.view.View[@content-desc="{expected_msg}"]'
            )
            actual_msg = response_message.get_attribute("content-desc")
            assert expected_msg == actual_msg, f"Expected: '{expected_msg}', but got: '{actual_msg}'"
            print(f"User Login: '{expected_msg}', Actual Result: '{actual_msg}'")
            self.custom_page.generate_screenshot(expected_msg)
        except Exception as error:
            print(error)

    def userLogout(self):
        try:
            self.custom_page.customScrollView("Sign Out")
            confirm_msg = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, '//android.view.View[@content-desc="Are you sure you want to logout?"]')
                )
            )
            if confirm_msg.is_displayed():
                print(confirm_msg.get_attribute("content-desc"))
                self.custom_page.customXpathClick("android.widget.Button", "Logout")
            time.sleep(1)
            self.driver.press_keycode(AndroidKey.BACK)
            msg = "Best Property Sale"
            expected_msg = self.wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, f'{msg}'))
            )
            assert expected_msg.is_displayed()
            print(f"Logout Successful")
        except Exception as error:
            print(error)