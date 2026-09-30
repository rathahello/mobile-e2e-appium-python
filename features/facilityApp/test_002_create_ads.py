import json
from appium.webdriver.common.appiumby import AppiumBy
from utils.facility_app import get_driver_app
from pages.Custom import randomString, getCredentials, dataPath, CustomPage
from pages.LoginPage import TestLoginPage
from pages.AdsPage import AdvertisementPage

driver = get_driver_app()
login = TestLoginPage(driver)
user_cred = getCredentials()
ads_page = AdvertisementPage(driver)
custom_page = CustomPage(driver)
ads_path = dataPath("facility_app", "ads_test_data.json")
random_str = randomString(10)

def test_user_login_successfully():
    login.signInBtn("Sign in")
    login.userLoginSuccessful(user_cred['username'], user_cred['password'])

def test_create_ads_successfully():
    with open(ads_path) as json_file:
        data = json.load(json_file)
        properties = data['create_ads']['property_info']
        specification = data['create_ads']['specifications']
        address = data['create_ads']['location']
        title = properties['title'] + " " + random_str
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
        
def test_verify_ads_after_created():
    custom_page.customAccessibleClick("Profile")
    with open(ads_path) as json_file:
        data = json.load(json_file)
        properties = data['create_ads']['property_info']
        title = properties['title'] + " " + random_str
        element = driver.find_element(AppiumBy.XPATH, f"//*[contains(@content-desc, '{title}')]")
        content_desc = element.get_attribute("content-desc")
        assert title in content_desc
        print(f"Ads with title '{title}' is created successfully and verified in the profile page.")
