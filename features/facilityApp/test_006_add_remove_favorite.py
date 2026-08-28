from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.Custom import getCredentials
from pages.Custom import CustomPage
from pages.AdsPage import AdvertisementPage

driver = get_driver_app()
login = TestLoginPage(driver)
user = getCredentials()
custom_page = CustomPage(driver)
def test_login_successfully():
    login.test_sign_in_btn("Sign in")
    login.test_login_successful(user['username'], user['password'])
def test_add_remove_favorite():
    custom_page.customAccessibleClick('Profile')
    add_favorite = AdvertisementPage(driver)
    add_favorite.addAndRemoveFavoriteAds()
