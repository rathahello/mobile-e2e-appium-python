from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.AdsPage import AdvertisementPage
from pages.Custom import randomString, getCredentials, CustomPage

driver = get_driver_app()
login = TestLoginPage(driver)
user = getCredentials()
custom_page = CustomPage(driver)
ads_page = AdvertisementPage(driver)
random = randomString(10)

def test_user_login_successfully():
    login.signInBtn("Sign in")
    login.userLoginSuccessful(user['username'], user['password'])

def test_update_advertisement():
    custom_page.customAccessibleClick('Profile')
    ads_page.updateAds(random)