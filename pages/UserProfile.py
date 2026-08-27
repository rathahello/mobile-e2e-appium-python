from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Custom import CustomPage
from pages.UserManagement import UserManagementPage


class UserProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.custom_page = CustomPage(self.driver)
        self.user_mg = UserManagementPage(self.driver)
    def navigateToUserProfile(self):
        self.custom_page.customAccessibleClick("Profile")

    def accountDeletion(self):
        try:
            self.user_mg.navigateToProfile()
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Edit Profile\nUpdate your Profile")')
                )
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, 'Delete Account')
                )
            ).click()
            confirm_msg = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH,
                     '//android.view.View[contains(@content-desc, "Are you sure you want to delete your account?")]')
                )
            )
            content_desc = confirm_msg.get_attribute('content-desc')
            if "delete your account" in content_desc:
                print(content_desc)
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Delete Account"]')
                    )
                ).click()
                self.custom_page.generate_screenshot("account_deletion_successful")
                self.custom_page.customAccessibleClick("OK")
        except Exception as error:
            self.custom_page.generate_screenshot("account_deletion_failed")
            print(error)