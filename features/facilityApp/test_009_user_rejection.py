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

def test_user_register_successful():
    user_data = parentPath("data/register_test_data.json")
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
def test_user_rejection():
    login.test_sign_in_btn("Sign in to Continue")
    login.test_login_successful(user_cred['username'], user_cred['password'])
    custom_page.customAccessibleClick("Profile")
    user_data = parentPath("data/register_test_data.json")
    with open(user_data) as json_file:
        data = json.load(json_file)
        user_mg.userRejection(data['staffId'])
