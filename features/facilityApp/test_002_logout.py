from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.Custom import getCredentials

def test_user_logout_successfully():
    driver = get_driver_app()
    login = TestLoginPage(driver)
    user = getCredentials()
    login.test_sign_in_btn("Sign in")
    login.test_login_successful(user['username'], user['password'])
    login.test_logout()
