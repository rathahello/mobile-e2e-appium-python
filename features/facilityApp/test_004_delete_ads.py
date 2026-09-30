from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.AdsPage import AdvertisementPage
from pages.Custom import CustomPage, getCredentials

driver = get_driver_app()
login = TestLoginPage(driver)
user = getCredentials()
custom_page = CustomPage(driver)
ads_page = AdvertisementPage(driver)
def test_user_login_successfully():
    login.signInBtn("Sign in")
    login.userLoginSuccessful(user['username'], user['password'])
def test_delete_ads():
    custom_page.customAccessibleClick('Profile')
    ads_page.deleteAds()
