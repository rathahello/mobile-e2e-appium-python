import json
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.Custom import parentPath

device_path = parentPath("data/devices.json")
apk_path = parentPath("data/apk.json")
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
def get_driver_app():
    options = UiAutomator2Options()
    with open(device_path) as file:
        obj = json.load(file)
        device = obj["real"] # real or virtual
        options.device_name = device["device_name"]
        options.platform_version = device["version"]
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    # options.app_package = "com.bpcbt.android.app.chiefbank"
    options.app_activity = "com.chief.chieffacility.MainActivity"
    with open(apk_path) as json_file:
        apk_json = json.load(json_file)
        apk = os.path.join(PROJECT_ROOT, "apk", apk_json["facility_apk"])
        options.app = apk

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
    return driver