from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Custom import CustomPage, randomString
from pages.UserManagement import UserManagementPage


class UserProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.custom_page = CustomPage(self.driver)
        self.user_mg = UserManagementPage(self.driver)

    def accountDeletion(self, reason):
        try:
            self.custom_page.customXpathClickLabel("View Profile")
            self.custom_page.customXpathClickLabel("Personal Information")
            self.custom_page.customAccessibleClick("Delete Account")
            if reason == "Other":
                value = randomString(25)
                self.custom_page.customAccessibleClick(reason)
                comment = self.wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.CLASS_NAME, "android.widget.EditText")
                    )
                )
                comment.click()
                comment.send_keys(value)
                self.driver.press_keycode(AndroidKey.BACK)
            else:
                self.custom_page.customAccessibleClick(reason)

            self.custom_page.customAccessibleClick("Submit")
            confirm_msg = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH,
                     '//*[contains(@content-desc, "Are you sure you want to delete your account?")]')
                )
            )
            if confirm_msg.is_displayed():
                print("Confirm Message: ", confirm_msg.get_attribute('content-desc'))
                self.custom_page.customXpathClick("android.widget.Button", "Delete Account")
                success_msg = self.wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.ACCESSIBILITY_ID, "User is deleted successfully")
                    )
                )
                content_desc = success_msg.get_attribute('content-desc')
                if success_msg.is_displayed():
                    print("Success message: ", content_desc)
                    self.custom_page.generate_screenshot(content_desc)
                    self.custom_page.customAccessibleClick("OK")
        except Exception as error:
            self.custom_page.generate_screenshot("account_deletion_failed")
            print(error)