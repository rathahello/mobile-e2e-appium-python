import json

from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.Custom import getCredentials, CustomPage, parentPath, dataPath

driver = get_driver_app()
login = TestLoginPage(driver)
user_cred = getCredentials()
custom_page = CustomPage(driver)
validate_msg = dataPath("facility_app", "validation_message_test_data.json")

def test_user_login_successfully():
    login.signInBtn("Sign in")
    login.userLoginSuccessful(user_cred['username'], user_cred['password'])
def test_logout_successfully():
    custom_page.customAccessibleClick("Profile")
    custom_page.customXpathClick("android.view.View", "View Profile")
    login.userLogout()
def test_user_login_invalid_credentials():
    login.signInBtn("Sign in to Continue")
    with open(validate_msg) as json_file:
        data = json.load(json_file)
        expected_msg = data["message"]["invalid_cred"]
        login.userLoginInvalidCred("username", "Test@1234", expected_msg)
