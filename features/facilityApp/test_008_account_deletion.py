import json

from pages.Register import RegisterPage
from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.Custom import parentPath, CustomPage, getCredentials
from pages.UserProfile import UserProfilePage
from appium.webdriver.common.appiumby import AppiumBy
from pages.UserManagement import UserManagementPage

driver = get_driver_app()
# register = RegisterPage(driver)
userData = parentPath("data/register_test_data.json")
custom_page = CustomPage(driver)
login = TestLoginPage(driver)
user = getCredentials()
with open(userData) as json_file:
    data = json.load(json_file)
    # register.registerSuccessful(
    #     data['staffId'],
    #     data['userId'],
    #     data['phoneNumber'],
    #     data['dateOfBirth'],
    #     data['email'],
    #     data['password']
    # )
    # custom_page.customAccessibleClick("Guest Mode")
    # login.loginSuccessful(data['userId'], data['password'])
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Profile').click()
    # # Account Deletion
    user_profile = UserProfilePage(driver)
    # user_profile.accountDeletion()
    #Login again to verify validation message
    expected_msg = "This account no longer exists"
    login.test_sign_in_btn("Sign in") # Example
    login.test_login_in_valid_cred(data['userId'], data['password'], expected_msg)
    #Verify record after user deleted
    login.test_login_successful(user['username'], user['password'])
    user_mg = UserManagementPage(driver)
    user_profile.navigateToUserProfile()
    user_mg.navigateToSetting()
