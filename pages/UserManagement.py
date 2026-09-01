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
        self.custom_page.customXpathClickLabel("View Profile")
        self.custom_page.customAccessibleClick("Settings")

    def userRejection(self, userId):
        try:
            self.navigateToSetting()
            self.custom_page.customXpathClickLabel("User Management")
            check_user = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, f'//android.widget.ImageView[contains(@content-desc, "{userId}")]')
                )
            )
            contain_desc = check_user.get_attribute("content-desc")
            if userId in contain_desc:
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

    def userApproval(self, user_id, user_role):
        try:
            self.navigateToSetting()
            self.custom_page.customXpathClickLabel("User Management")
            check_user = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, f'//*[contains(@content-desc, "{user_id}")]')
                )
            )
            content_desc = check_user.get_attribute("content-desc")
            if user_id in content_desc:
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Approve").instance(0)')
                    )
                ).click()
                self.custom_page.customXpathClickLabel(user_role)
                enter_cmt = self.wait.until(
                    EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText'))
                )
                enter_cmt.click()
                enter_cmt.send_keys("Approved")
                self.custom_page.customXpathClickLabel("Approve")
                confirm_msg = self.wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.XPATH, '//*[contains(@content-desc, "approved successfully")]')
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

    def userRequestDelete(self, user_id):
        try:
            self.navigateToSetting()
            self.custom_page.customXpathClickLabel("User Management")
            self.verifyUser(user_id, "Delete Requests")
            self.custom_page.customAccessibleClick("Approve Deletion")
            confirm_msg = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, '//*[contains(@content-desc, "Approve account deletion")]')
                )
            )
            if confirm_msg.is_displayed():
                print("Confirm Message: ", confirm_msg.get_attribute("content-desc"))
                self.custom_page.customAccessibleClick("Approve")
                success_msg = self.wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.XPATH, '//*[contains(@content-desc, "account deletion has been approved")]')
                    )
                )
                content_desc = success_msg.get_attribute("content-desc")
                if success_msg.is_displayed():
                    self.custom_page.generate_screenshot(content_desc)
                    self.custom_page.customAccessibleClick("OK")
        except Exception as error:
            print(error)

    def verifyUser(self, user_id, tab):
        try:
            self.custom_page.customXpathClick("android.view.View", f"{tab}")
            user_rejected = self.driver.find_element(
                AppiumBy.XPATH, f'//*[contains(@content-desc, "{user_id}")]'
            )
            contain_desc = user_rejected.get_attribute("content-desc")
            assert user_id in contain_desc
            print(f"Expected: '{user_id}' in '{contain_desc}'")
            self.custom_page.generate_screenshot("user_" + tab )
        except Exception as error:
            print(error)