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
            self.custom_page.customXpathClick("android.view.View", "Personal Information")
            self.custom_page.customAccessibleClick("Delete Account")
            self.custom_page.customAccessibleClick("No longer need the app")
            self.custom_page.customAccessibleClick("Submit")
            confirm_msg = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH,
                     '//android.view.View[contains(@content-desc, "Are you sure you want to delete your account?")]')
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
                if success_msg.is_displayed():
                    print("Success message: ", success_msg.get_attribute('content-desc'))
                    self.custom_page.generate_screenshot("account_deleted_successfully")
                    self.custom_page.customAccessibleClick("OK")
        except Exception as error:
            self.custom_page.generate_screenshot("account_deletion_failed")
            print(error)