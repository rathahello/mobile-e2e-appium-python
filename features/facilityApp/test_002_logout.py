from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.Custom import getCredentials, CustomPage

driver = get_driver_app()
login = TestLoginPage(driver)
custom_page = CustomPage(driver)
user = getCredentials()
def test_user_logout_successfully():
    login.test_sign_in_btn("Sign in")
    login.test_login_successful(user['username'], user['password'])
def test_logout_successfully():
    custom_page.customAccessibleClick("Profile")
    custom_page.customXpathClick("android.view.View", "View Profile")
    login.test_logout()
