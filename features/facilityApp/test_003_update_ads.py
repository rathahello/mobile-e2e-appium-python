from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.AdsPage import AdvertisementPage
from pages.Custom import randomString, getCredentials, CustomPage

def test_update_advertisement():
    driver = get_driver_app()
    login = TestLoginPage(driver)
    user = getCredentials()
    login.signInBtn("Sign in")
    login.userLoginSuccessful(user['username'], user['password'])
    custom_page = CustomPage(driver)
    custom_page.customAccessibleClick('Profile')
    ads_page = AdvertisementPage(driver)
    random = randomString(10)
    ads_page.updateAds(random)