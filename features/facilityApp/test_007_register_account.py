import json
from appium.webdriver.common.appiumby import AppiumBy

from utils.facility_app import get_driver_app
from pages.Custom import parentPath, CustomPage, getCredentials
from pages.Register import RegisterPage
from pages.LoginPage import TestLoginPage
from pages.UserManagement import UserManagementPage

def test_register_validation():
    driver = get_driver_app()
    register = RegisterPage(driver)
    register_path = parentPath("data/register_test_data.json")
    custom_page = CustomPage(driver)
    with open(register_path) as json_file:
        data = json.load(json_file)
        register.registerSuccessful(
            data['staffId'],
            data['userId'],
            data['phoneNumber'],
            data['dateOfBirth'],
            data['email'],
            data['password']
        )
        # driver.press_keycode(AndroidKey.BACK)
        custom_page.customAccessibleClick("Guest Mode")
        register.verifyExistingUser(
            data['staffId'],
            data['userId'],
            data['phoneNumber'],
            data['dateOfBirth'],
            data['email'],
            data['password']
        )
        custom_page.customAccessibleClick("Back")
        custom_page.customAccessibleClick("Guest Mode")
        register.registerInvalidInfo(
            "001",
            data['userId'],
            data['phoneNumber'],
            data['dateOfBirth'],
            data['email'],
            data['password']
        )
    user_cred = getCredentials()
    login = TestLoginPage(driver)
    login.test_login_successful(user_cred['username'], user_cred['password'])
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Profile').click()
    user_mg = UserManagementPage(driver)
    user_data = parentPath("data/register_test_data.json")
    with open(user_data) as json_file:
        data = json.load(json_file)
        user_mg.userRejection(data['staffId'])