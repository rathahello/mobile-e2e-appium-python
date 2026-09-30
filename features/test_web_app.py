from appium.webdriver.common.appiumby import AppiumBy

from utils.web_app import get_driver_web_app

driver = get_driver_web_app()
def test_openWebApp():
    driver.get("https://www.google.com")
    # element = driver.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar")
    # element.click()
    # element.send_keys("hello world")
