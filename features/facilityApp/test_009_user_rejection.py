from appium.webdriver.extensions.android.nativekey import AndroidKey

from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.Register import RegisterPage
from pages.Custom import getCredentials, parentPath, CustomPage
import json
from pages.UserManagement import UserManagementPage

driver = get_driver_app()
login = TestLoginPage(driver)
user_cred = getCredentials()
register = RegisterPage(driver)
custom_page = CustomPage(driver)
user_mg = UserManagementPage(driver)
user_data = parentPath("data/register_test_data.json")
validate_msg = parentPath("data/validation_message_test_data.json")

def test_user_register_successful():
    with open(user_data) as json_file:
        data = json.load(json_file)
        register.registerSuccessful(
            data['staffId'],
            data['userId'],
            data['phoneNumber'],
            data['dateOfBirth'],
            data['email'],
            data['password']
        )
def user_login_validation(expect_msg):
    with open(user_data) as json_file:
        data = json.load(json_file)
        login.test_sign_in_btn("Sign in to Continue")
        login.test_login_in_valid_cred(data['userId'], data['password'], expect_msg)

def test_user_login_not_verified():
    with open(validate_msg) as json_file:
        data = json.load(json_file)
        message = data['message']['user_not_verify']
        user_login_validation(message)

def test_user_rejection():
    driver.press_keycode(AndroidKey.BACK)
    login.test_sign_in_btn("Sign in to Continue")
    login.test_login_successful(user_cred['username'], user_cred['password'])
    custom_page.customAccessibleClick("Profile")
    with open(user_data) as json_file:
        data = json.load(json_file)
        user_mg.userRejection(data['staffId'])
        custom_page.customAccessibleClick("Back")
        login.test_logout()

def test_user_login_after_rejected():
    with open(validate_msg) as json_file:
        data = json.load(json_file)
        message = data['message']['invalid_cred']
        user_login_validation(message)