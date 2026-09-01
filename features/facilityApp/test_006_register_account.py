import json

from utils.facility_app import get_driver_app
from pages.Custom import parentPath, CustomPage, getCredentials, dataPath
from pages.Register import RegisterPage
from pages.LoginPage import TestLoginPage
from pages.UserManagement import UserManagementPage
from appium.webdriver.common.appiumby import AppiumBy

driver = get_driver_app()
register = RegisterPage(driver)
custom_page = CustomPage(driver)
register_path = dataPath("facility_app", "register_test_data.json")
user_cred = getCredentials()
login = TestLoginPage(driver)
user_mg = UserManagementPage(driver)

def test_register_successful():
    with open(register_path) as file:
        data = json.load(file)
        register.registerSuccessful(
            data['staffId'],
            data['userId'],
            data['phoneNumber'],
            data['dateOfBirth'],
            data['email'],
            data['password']
        )
def test_user_already_registered():
    custom_page.customAccessibleClick("Guest Mode")
    with open(register_path) as file:
        data = json.load(file)
        register.verifyExistingUser(
            data['staffId'],
            data['userId'],
            data['phoneNumber'],
            data['dateOfBirth'],
            data['email'],
            data['password']
        )
def test_user_invalid_info():
        custom_page.customAccessibleClick("Back")
        custom_page.customAccessibleClick("Guest Mode")
        with open(register_path) as file:
            data = json.load(file)
            register.registerInvalidInfo(
                "001",
                data['userId'],
                data['phoneNumber'],
                data['dateOfBirth'],
                data['email'],
                data['password']
            )

        login.userLoginSuccessful(user_cred['username'], user_cred['password'])
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Profile').click()
        with open(register_path) as json_file:
            get_data = json.load(json_file)
            user_mg.userRejection(get_data['staffId'])