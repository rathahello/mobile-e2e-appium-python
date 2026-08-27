import json

from pages.Custom import randomString, getCredentials, parentPath
from utils.facility_app import get_driver_app
from pages.LoginPage import TestLoginPage
from pages.AdsPage import AdvertisementPage

def test_create_advertisement_successfully():
    ads_path = parentPath("data/ads_test_data.json")
    driver = get_driver_app()
    login = TestLoginPage(driver)
    user = getCredentials()
    login.test_sign_in_btn("Sign in")
    login.test_login_successful(user['username'], user['password'])
    ads_page = AdvertisementPage(driver)
    random_str = randomString(10)
    with open(ads_path) as json_file:
        data = json.load(json_file)
        properties = data['create_ads']['property_info']
        title = properties['title'] + " " + random_str
        specification = data['create_ads']['specifications']
        address = data['create_ads']['location']
        ads_page.createAds(
            4,
            title,
            properties['price'],
            properties['monthly_payment'],
            properties['property_code'],
            properties['description'],
            "Urgent",
            specification['land_size'],
            specification['road_size'],
            specification['home_size'],
            specification['floor_count'],
            specification['bedrooms'],
            specification['bathrooms'],
            "House",
            address['address'],
        )
