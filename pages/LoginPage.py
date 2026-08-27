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

    def test_sign_in_btn(self, label):
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

    def test_login_successful(self, username, password):
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

    def test_login_in_valid_cred(self, username, password, expected_msg):
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

    def test_logout(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.view.View[@content-desc="Profile"]')
                )
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "View Profile")]')
                )
            ).click()
            element = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().descriptionContains("Sign Out"))'
            )
            element.click()
            # validate message
            confirm_msg = self.driver.find_element(
                AppiumBy.XPATH,
                '//android.view.View[@content-desc="Are you sure you want to logout?"]'
            )
            print(confirm_msg.get_attribute("content-desc"))
            if confirm_msg.is_displayed():
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Logout"]')
                    )
                ).click()
            print(f"Logout Successful")
            self.driver.press_keycode(AndroidKey.BACK)
            msg = "Best Property Sale"
            expected_msg = self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, f'{msg}'
            )
            assert expected_msg.is_displayed()
        except Exception as error:
            print(error)