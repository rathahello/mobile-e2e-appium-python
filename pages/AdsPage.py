import os
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from pages.Custom import CustomPage, getCurrentDate

os.makedirs("screenshots", exist_ok=True)
currentDate = getCurrentDate()
class AdvertisementPage:
    def __init__(self, driver):
        self.driver = driver
        self.custom_page = CustomPage(self.driver)
        self.wait = WebDriverWait(self.driver, 20)

    def addPhoto(self, numOfPhoto):
        self.custom_page.customScrollToEnd(10)
        self.custom_page.customAccessibleClick("Add Photos")
        self.custom_page.customAccessibleClick("Gallery")
        access_photo = self.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_message')
        if access_photo.is_displayed():
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
                )
            ).click()
        self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("android.widget.LinearLayout").instance(9)')
            )
        ).click()
        for i in range(numOfPhoto):
            print("Photo Index ", i)
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().resourceId("com.sec.android.gallery3d:id/deco_view_layout").instance({i})')
                )
            ).click()
        self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ID, 'com.sec.android.gallery3d:id/action_done'))
        ).click()

    def createAds(self,
                  numOfPhoto, title, price, monthlyPayment,
                  prop_code, description, status,
                  landSize, roadSize, houseSize, floors,
                  bedrooms, bathrooms, subCategory, address
                  ):
        try:
            self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button'))
            ).click()
            if subCategory == "Land":
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "Sub Category\nHouse")]')
                    )
                ).click()
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Land"]')
                    )
                ).click()
            self.addPhoto(numOfPhoto)
            # Properties section
            self.custom_page.customUiAutoIndexValue(0, title)
            self.custom_page.customUiAutoIndexValue(1, price)
            self.custom_page.customUiAutoIndexValue(2, monthlyPayment)
            self.custom_page.customAccessibleClick("Property Type")
            if subCategory == "Land":
                self.custom_page.customAccessibleClick("Vacant Land")
            else:
                self.custom_page.customAccessibleClick("King Villa")
            self.custom_page.customUiAutoIndexValue(3, prop_code)
            self.custom_page.customUiAutoIndexValue(4, description)
            self.driver.press_keycode(AndroidKey.BACK)
            if status == "Urgent":
                self.custom_page.customAccessibleClick("Urgent")
            # Specifications section
            self.custom_page.customXpathContain("Land Size", landSize)
            self.custom_page.customXpathContain("Road Size", roadSize)
            if subCategory == "House":
                self.custom_page.customXpathContain("House Size", houseSize)
                self.custom_page.customXpathContain("Floors", floors)
                self.custom_page.customXpathContain("Bedrooms", bedrooms)
                self.custom_page.customXpathContain("Bathrooms", bathrooms)
            self.driver.press_keycode(AndroidKey.BACK)
            self.custom_page.customAccessibleClick("Direction")
            self.custom_page.customAccessibleClick("North")
            self.custom_page.customAccessibleClick("Type of Title Deed")
            self.custom_page.customAccessibleClick("Hard")
            self.custom_page.customAccessibleClick("City/Province")
            self.custom_page.customAccessibleClick("Phnom Penh")
            self.custom_page.scrollDown(100, 100, 200, 500, 3.0)
            self.custom_page.customAccessibleClick("Khan/District")
            self.custom_page.customAccessibleClick("Chamkar Mon")
            self.custom_page.customAccessibleClick("Sangkat/Commune")
            self.custom_page.customAccessibleClick("Tonle Basak")
            self.custom_page.scrollDown(100, 100, 200, 500, 3.0)
            self.custom_page.customAccessibleClick("Phum/Village")
            self.custom_page.customAccessibleClick("Phum 1")
            self.custom_page.customXpathContain("Borey Name", "Borey Sorla")
            self.custom_page.customXpathContain("Address", address)
            self.driver.press_keycode(AndroidKey.BACK)
            self.custom_page.customScrollView("Google Map")
            confirm_access = self.driver.find_element(
                AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'
            )
            if confirm_access.is_displayed():
                confirm_access.click()
            self.custom_page.customAccessibleClick("Confirm Location")
            time.sleep(2)
            # Submit Advertisement
            self.driver.press_keycode(AndroidKey.BACK)
            self.custom_page.customAccessibleClick("Post")
            submit_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Are you sure you want to create this post?')
            print(submit_btn.get_attribute('content-desc'))
            if submit_btn.is_displayed():
                self.wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Post"]')
                    )
                ).click()
            confirm_btn = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, 'Advertisement is created successfully')
                )
            )
            print(confirm_btn.get_attribute('content-desc'))
            if confirm_btn.is_displayed():
                self.custom_page.customAccessibleClick("OK")
            self.custom_page.generate_screenshot("create_ads_success_" + currentDate)
        except Exception as error:
            self.custom_page.generate_screenshot("create_ads_failure_" + currentDate)
            print(error)

    def updateAds(self, title):
        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Show menu").instance(0)')
                )
            ).click()
            self.custom_page.customAccessibleClick("Edit")
            self.addPhoto(1)
            self.custom_page.customScrollToBegin(20)
            self.custom_page.customXpathContain("Title", f"Update Ads {title}")
            self.driver.press_keycode(AndroidKey.BACK)
            self.custom_page.customAccessibleClick("Update Listing")
            confirm_msg = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Are you sure you want to update this post?"))
            )
            print(confirm_msg.get_attribute('content-desc'))
            if confirm_msg.is_displayed():
                self.custom_page.customAccessibleClick("Update")
            success_msg = self.wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Advertisement is updated successfully'))
            )
            print(success_msg.get_attribute('content-desc'))
            if success_msg.is_displayed():
                self.custom_page.customAccessibleClick("OK")
            self.custom_page.generate_screenshot("update_ads_success" + currentDate)
        except Exception as error:
            self.custom_page.generate_screenshot("update_ads_failure" + currentDate)
            print(error)

    def deleteAds(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Show menu").instance(0)')
                )
            ).click()
            self.custom_page.customAccessibleClick("Delete")
            confirm_delete = self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, 'Delete Post')
                )
            )
            if confirm_delete.is_displayed():
                self.custom_page.customAccessibleClick("Delete")
            confirm_msg = self.wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Advertisement is deleted successfully'))
            )
            print(confirm_msg.get_attribute('content-desc'))
            if confirm_msg.is_displayed():
                self.custom_page.customAccessibleClick("OK")
            self.custom_page.generate_screenshot("delete_ads_success_" + currentDate)
        except Exception as error:
            self.custom_page.generate_screenshot("delete_ads_failure_" + currentDate)
            print(error)
    def addAndRemoveFavoriteAds(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[1]/android.view.View')
                )
            ).click()
            remove = self.wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Remove from favorite successfully'))
            )
            add = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Added to favorite successfully'))
            )
            content_desc = remove.get_attribute('content-desc')
            if "Remove" in content_desc:
                print(remove.get_attribute('content-desc'))
                self.custom_page.generate_screenshot("add_favorite_success")
            if "Add" in content_desc:
                self.custom_page.generate_screenshot("remove_favorite_success")
        except Exception as error:
            self.custom_page.generate_screenshot("add_favorite_failure")
            print(error)