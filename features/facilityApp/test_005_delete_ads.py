from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.AdsPage import AdvertisementPage
from pages.Custom import CustomPage, getCredentials

def test_advertisement_deletion():
    driver = get_driver_app()
    login = TestLoginPage(driver)
    user = getCredentials()
    login.test_sign_in_btn("Sign in")
    login.test_login_successful(user['username'], user['password'])
    custom_page = CustomPage(driver)
    custom_page.customAccessibleClick('Profile')
    ads_page = AdvertisementPage(driver)
    ads_page.deleteAds()
