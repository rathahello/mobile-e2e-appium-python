import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
import json

DEVICE_PATH = "../data/devices.json"
APK_JSON_PATH = "../data/apk.json"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
def get_driver_current_app():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app = r"D:/android/apk/UAT_VAPT_2.4.3-283.apk"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
    return driver

def get_driver_facility_app():
    options = UiAutomator2Options()
    with open(DEVICE_PATH) as file:
        device = json.load(file)
        options.device_name = device["real_device"]
        options.platform_name = "Android"
        options.platform_version = "12"
        options.automation_name = "UiAutomator2"
        options.app_activity = "com.chief.chieffacility.MainActivity"
    with open(APK_JSON_PATH) as json_file:
        apk_json = json.load(json_file)
        apk = os.path.join(PROJECT_ROOT, "apk", apk_json["facility_apk_v2"])
        options.app = apk

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
    return driver

# print(driver.current_package)

# driver.quit()
