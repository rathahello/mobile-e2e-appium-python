import json
import os
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from pages.Custom import parentPath

device_path = parentPath("data/devices.json")
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
def get_driver_web_app():
    options = UiAutomator2Options()
    with open(device_path) as file:
        obj = json.load(file)
        device = obj["real"] # real or virtual
        options.device_name = device["device_name"]
        options.platform_version = device["version"]
    # options.app_activity = "com.chief.chieffacility.MainActivity"
    options.platform_name = "Android"
    # options.automation_name = "UiAutomator2"
    options.browser_name = "Chrome"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
    return driver