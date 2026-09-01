import json
from appium.webdriver.extensions.android.nativekey import AndroidKey

from pages.Register import RegisterPage
from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.Custom import CustomPage, getCredentials, randomString, dataPath
from pages.UserProfile import UserProfilePage
from appium.webdriver.common.appiumby import AppiumBy
from pages.UserManagement import UserManagementPage

driver = get_driver_app()
register = RegisterPage(driver)
user_data = dataPath("facility_app", "register_test_data.json")
validate_msg = dataPath("facility_app", "validation_message_test_data.json")
user_reason_path = dataPath("facility_app", "delete_reason_test_data.json")
custom_page = CustomPage(driver)
login = TestLoginPage(driver)
user_cred = getCredentials()
user_id = randomString(10)
user_profile = UserProfilePage(driver)
user_mg = UserManagementPage(driver)

def test_user_register_successfully():
    with open(user_data) as json_file:
        data = json.load(json_file)
        register.registerSuccessful(
            data['staffId'],
            user_id,
            data['phoneNumber'],
            data['dateOfBirth'],
            data['email'],
            data['password']
        )
def validation_error_message(expect_msg):
    with open(user_data) as json_file:
        data = json.load(json_file)
        login.signInBtn("Sign in to Continue")
        login.userLoginInvalidCred(user_id, data['password'], expect_msg)
def test_user_login_not_verified():
    with open(validate_msg) as json_file:
        data = json.load(json_file)
        message = data['message']['user_not_verify']
        validation_error_message(message)
def test_user_approved_successfully():
    driver.press_keycode(AndroidKey.BACK)
    login.signInBtn("Sign in to Continue")
    login.userLoginSuccessful(user_cred['username'], user_cred['password'])
    custom_page.customAccessibleClick("Profile")
    with open(user_reason_path) as json_file:
        data = json.load(json_file)
        user_role = data['user_role'][2]
        user_mg.userApproval(user_id, user_role)
        user_mg.verifyUser(user_id, "Approved")
        custom_page.customAccessibleClick("Back")
        login.userLogout()
def test_user_account_deleted_successfully():
    login.signInBtn("Sign in to Continue")
    with open(user_data) as json_file:
        user = json.load(json_file)
        login.userLoginSuccessful(user_id, user['password'])
        custom_page.customAccessibleClick("Profile")
        with open(user_reason_path) as reason_file:
            get_obj = json.load(reason_file)
            reason = get_obj['delete_reason'][2]
            user_profile.accountDeletion(reason)
        with open(validate_msg) as file:
            json_obj = json.load(file)
            expect_msg = json_obj['message']['account_deleted']
            login.userLoginInvalidCred(user_id, user['password'], expect_msg)
def test_request_account_deleted():
    login.userLoginSuccessful(user_cred['username'], user_cred['password'])
    custom_page.customAccessibleClick("Profile")
    user_mg.userRequestDelete(user_id)
    custom_page.customAccessibleClick("Back")
    login.userLogout()