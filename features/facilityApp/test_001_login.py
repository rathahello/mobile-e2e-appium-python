from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.Custom import getCredentials

driver = get_driver_app()
login = TestLoginPage(driver)
user_cred = getCredentials()

def test_user_login_successfully():
    login.test_sign_in_btn("Sign in")
    login.test_login_successful(user_cred['username'], user_cred['password'])
    login.test_logout()
def test_user_login_invalid_credentials():
    login.test_sign_in_btn("Sign in to Continue")
    expected_msg = "User credentials are incorrect"
    login.test_login_in_valid_cred("username", "Test@1234", expected_msg)
