from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.Custom import CustomPage

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.custom_page = CustomPage(self.driver)
    def enterRegisterForm(self, staffId, userId, phoneNumber, dob, email, password):
        try:
            self.custom_page.customAccessibleClick("Don't have an account?")
            self.custom_page.customUiAutoIndexValue(0, staffId)
            self.custom_page.customUiAutoIndexValue(1, userId)
            self.custom_page.customUiAutoIndexValue(2, phoneNumber)
            self.driver.press_keycode(AndroidKey.BACK)
            self.driver.find_element(
                AppiumBy.XPATH,
                '//android.widget.ScrollView/android.view.View[3]/android.view.View[contains(@hint, "Date of Birth")]'
            ).click()
            self.custom_page.customAccessibleClick("Switch to input")
            element = self.driver.find_element(
                AppiumBy.CLASS_NAME, 'android.widget.EditText'
            )
            element.click()
            element.clear()
            element.send_keys(dob)
            self.custom_page.customAccessibleClick("OK")
            self.custom_page.customUiAutoIndexValue(3, email)
            self.custom_page.customUiAutoIndexValue(4, password)
            confirm_pwd = password
            enter_pwd = self.driver.find_element(
                AppiumBy.XPATH,
                '//android.widget.ScrollView/android.view.View/android.widget.EditText[contains(@hint, "Confirm Password")]'
            )
            enter_pwd.click()
            enter_pwd.send_keys(confirm_pwd)
            self.driver.press_keycode(AndroidKey.BACK)
            self.custom_page.customAccessibleClick("Create Account")
            self.custom_page.customAccessibleClick("Submit")
        except Exception as error:
            print(error)
    def registerSuccessful(self, staffId, userId, phoneNumber, dob, email, password):
        try:
            self.custom_page.customAccessibleClick("Sign in")
            self.driver.press_keycode(AndroidKey.BACK)
            self.enterRegisterForm(staffId, userId, phoneNumber, dob, email, password)
            confirm_msg = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, '//*[contains(@content-desc, "Your account is currently pending approval")]')
                )
            )
            content_desc = confirm_msg.get_attribute('content-desc')
            if confirm_msg.is_displayed():
                print("Response message: ", content_desc)
                self.custom_page.generate_screenshot("register_success")
                self.custom_page.customAccessibleClick("OK")
        except Exception as error:
            self.custom_page.generate_screenshot("register_failed")
            print(error)
    def verifyExistingUser(self, staffId, userId, phoneNumber, dob, email, password):
        try:
            self.wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Sign in"))
            ).click()
            self.driver.press_keycode(AndroidKey.BACK)
            self.enterRegisterForm(staffId, userId, phoneNumber, dob, email, password)
            confirm = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID,
                     'User already exists')
                )
            )
            actual_msg = confirm.get_attribute('content-desc')
            expected_msg = "User already exists"
            assert expected_msg == actual_msg, f"Expected: '{expected_msg}', but got: '{actual_msg}'"
            print(f"Expected Result: '{expected_msg}', Actual Result: '{actual_msg}'")
            self.custom_page.generate_screenshot(actual_msg)
            self.custom_page.customAccessibleClick("OK")
        except Exception as error:
            print(error)
    def registerInvalidInfo(self, staffId, userId, phoneNumber, dob, email, password):
        try:
            self.wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Sign in"))
            ).click()
            self.driver.press_keycode(AndroidKey.BACK)
            self.enterRegisterForm(staffId, userId, phoneNumber, dob, email, password)
            confirm = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID,
                     'Employee is not available')
                )
            )
            print(confirm.get_attribute('content-desc'))
            actual_msg = confirm.get_attribute('content-desc')
            expected_msg = "Employee is not available"
            assert expected_msg == actual_msg, f"Expected: '{expected_msg}', but got: '{actual_msg}'"
            print(f"Expected Result: '{expected_msg}', Actual Result: '{actual_msg}'")
            self.custom_page.generate_screenshot(actual_msg)
            self.custom_page.customAccessibleClick("OK")
        except Exception as error:
            self.custom_page.generate_screenshot("register_failed")
            print(error)
