from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.AdsPage import AdvertisementPage
from pages.Custom import CustomPage, getCredentials

driver = get_driver_app()
login = TestLoginPage(driver)
user = getCredentials()
custom_page = CustomPage(driver)
def test_logout_successfully():
    login.test_sign_in_btn("Sign in")
    login.test_login_successful(user['username'], user['password'])
def test_delete_ads():
    custom_page.customAccessibleClick('Profile')
    ads_page = AdvertisementPage(driver)
    ads_page.deleteAds()
