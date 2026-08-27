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
        self.custom_page.customXpathBtnClick("User Management")

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
                    self.custom_page.customXpathBtnClick("Reject")
                    print("User is rejected successfully")
                    self.custom_page.generate_screenshot("user_rejected_successfully")
                self.custom_page.customAccessibleClick("OK")
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
            contain_desc = check_user.get_attribute("content-desc")
            if staffId in contain_desc:
                print("Contain Description: ", contain_desc)
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Approve").instance(0)')
                    )
                ).click()
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Administrator Full Management")')
                    )
                ).click()
                enter_cmt = self.wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
                    )
                )
                enter_cmt.click()
                enter_cmt.send_keys("Approved")
                approve_btn = self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Approve")')
                    )
                )
                approve_btn.click()
                message = self.wait.until(
                    EC.visibility_of_element_located(
                        (AppiumBy.XPATH, f'//android.view.View[contains(@content-desc, "approved successfully")]')
                    )
                )
                resp_msg = message.get_attribute("content-desc")
                if "approved successfully" in resp_msg:
                    print(resp_msg)
                    self.custom_page.generate_screenshot("Approved_successfully")
                    self.custom_page.customAccessibleClick("OK")
        except Exception as error:
            self.custom_page.generate_screenshot("Approved_failed")
            print(error)

    def userDeletion(self, staffId):
        self.navigateToEachTabs("Delete Requests", 4)

    def verifyUserApproved(self, staffId):
        try:
            self.navigateToUserManagement()
            self.navigateToEachTabs("Approved", 2)
            # User approved should be displaying
            check_user = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, f'//android.widget.ImageView[contains(@content-desc, "{staffId}")]')
                )
            )
            contain_desc = check_user.get_attribute("content-desc")
            if staffId in contain_desc:
                print("Contain Description: ", contain_desc)
                self.custom_page.generate_screenshot("verify_user_approved_success")
        except Exception as error:
            print(error)

    def verifyUserRejected(self, staffId):
        try:
            self.navigateToUserManagement()
            self.navigateToEachTabs("Rejected", 3)
            # User rejected should be displaying
            check_user = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, f'//android.widget.ImageView[contains(@content-desc, "{staffId}")]')
                )
            )
            contain_desc = check_user.get_attribute("content-desc")
            if staffId in contain_desc:
                print("Contain Description: ", contain_desc)
                self.custom_page.generate_screenshot("verify_user_rejected_success")
        except Exception as error:
            print(error)

    def verifyUserDeleted(self, staffId):
        try:
            self.navigateToUserManagement()
            self.navigateToEachTabs(4)
            # User deleted should be displaying
            check_user = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, f'//android.widget.ImageView[contains(@content-desc, "{staffId}")]')
                )
            )
            contain_desc = check_user.get_attribute("content-desc")
            if staffId in contain_desc:
                print("Contain Description: ", contain_desc)
                self.custom_page.generate_screenshot("verify_user_deleted_success")

            # self.login_page.enterLoginForm(username, password)
            # time.sleep(3)
            # response_message = self.driver.find_element(
            #     AppiumBy.XPATH,
            #     '//android.view.View[@content-desc="This account no longer exists"]'
            # )
            # expected_msg = "This account no longer exists"
            # actual_msg = response_message.get_attribute("content-desc")
            # assert expected_msg == actual_msg, f"Expected: '{expected_msg}', but got: '{actual_msg}'"
            # print(f"Expected Result: '{expected_msg}', Actual Result: '{actual_msg}'")
        except Exception as error:
            self.custom_page.generate_screenshot("verify_user_deleted_failed")
            print(error)
