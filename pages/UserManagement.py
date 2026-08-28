from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from pages.Custom import CustomPage
from selenium.webdriver.support import expected_conditions as EC
from pages.LoginPage import TestLoginPage

class UserManagementPage:
    def __init__(self, driver):
        self.driver = driver
        self.custom_page = CustomPage(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        self.login_page = TestLoginPage(self.driver)

    def navigateToSetting(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "View Profile")]')
            )
        ).click()
        self.custom_page.customAccessibleClick("Settings")

    def navigateToUserManagement(self):
        self.custom_page.customXpathClick("android.widget.Button", "User Management")

    def navigateToEachTabs(self, desc, numOfTabs):
        self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{desc}\nTab {numOfTabs} of 4")')
            )
        ).click()

    def userRejection(self, staffId):
        try:
            self.navigateToSetting()
            self.navigateToUserManagement()
            check_user = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, f'//android.widget.ImageView[contains(@content-desc, "{staffId}")]')
                )
            )
            contain_desc = check_user.get_attribute("content-desc")
            if staffId in contain_desc:
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Reject").instance(0)')
                    )
                ).click()
                confirm_msg = self.wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "Are you sure you want to reject")]')
                    )
                )
                if confirm_msg.is_displayed():
                    print(confirm_msg.get_attribute("content-desc"))
                    comment = self.wait.until(
                        EC.element_to_be_clickable(
                            (AppiumBy.XPATH, '//android.widget.EditText')
                        )
                    )
                    comment.click()
                    comment.send_keys("Rejected")
                    self.custom_page.customXpathClick("android.widget.Button", "Reject")
                success_msg = self.wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "has been rejected")]')
                    )
                )
                if success_msg.is_displayed():
                    self.custom_page.generate_screenshot("user_rejected_successfully")
                    self.custom_page.customAccessibleClick("OK")
                    print("User is rejected successfully")
        except Exception as error:
            self.custom_page.generate_screenshot("rejected_failed")
            print(error)

    def userApproval(self, staffId):
        try:
            self.navigateToSetting()
            self.navigateToUserManagement()
            check_user = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, f'//android.widget.ImageView[contains(@content-desc, "{staffId}")]')
                )
            )
            content_desc = check_user.get_attribute("content-desc")
            if staffId in content_desc:
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Approve").instance(0)')
                    )
                ).click()
                self.custom_page.customXpathClick("android.view.View", "Administrator")
                enter_cmt = self.wait.until(
                    EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText'))
                )
                enter_cmt.click()
                enter_cmt.send_keys("Approved")
                self.custom_page.customXpathClick("android.widget.Button", "Approve")
                confirm_msg = self.wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "approved successfully")]')
                    )
                )
                if confirm_msg.is_displayed():
                    print("Confirm Message: ", confirm_msg.get_attribute("content-desc"))
                    self.custom_page.generate_screenshot("user_approved_successfully")
                    self.custom_page.customAccessibleClick("OK")
                    print("User is approved successfully")
        except Exception as error:
            self.custom_page.generate_screenshot("user_approves_failed")
            print(error)

    def userDeletion(self, staffId):
        self.navigateToEachTabs("Delete Requests", 4)
