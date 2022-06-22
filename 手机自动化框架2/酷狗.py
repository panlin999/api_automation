import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

data = {
  "appium:deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "appium:platformVersion": "7.1.2",
  "appium:appPackage": "com.kugou.android",
  "appium:appActivity": "com.kugou.android.app.MediaActivity",
  "appium:noReset": "true"
}
url = "127.0.0.1:4723/wd/hub"
driver = webdriver.Remote(url, data)
driver.implicitly_wait(5)
el1 = driver.find_element(by=AppiumBy.ID, value="com.kugou.android:id/m3r")
# el1.click()
# el2 = driver.find_element(by=AppiumBy.CLASS_NAME,
#                           value="//android.widget.LinearLayout[@content-desc=\"同意用户协议和隐私政策\"]/android.widget.RelativeLayout/android.widget.ImageView")
# el1.click()
# el3 = driver.find_element_by_xpath("//android.widget.LinearLayout[@content-desc=‘同意用户协议和隐私政策‘]/android.widget.RelativeLayout/android.widget.ImageView")
# # el3.click()
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(706, 746)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
#
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(359, 1776)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(3)
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(420, 393)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
# el100=driver.find_element_by_id("com.kugou.android:id/m3q")
# el100.click()
###勾选同意框
driver.find_element_by_xpath(
  "//android.widget.LinearLayout[@content-desc='同意用户协议和隐私政策']/android.widget.RelativeLayout/android.widget.ImageView").click()
###el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="密码 安全")很容易出错，使用下面一条语句提高成功率
###选择QQ登录
e28 = driver.find_element_by_xpath(
  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]")
e28.click()
##登录
el1001 = driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
el1001.click()
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="请输入QQ号码或手机或邮箱")
el4.send_keys("470290833")
el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="密码 安全")
el5.send_keys("THE-first")
el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="登录")
el6.click()
el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="确定")
el7.click()
###组合定位
driver.find_elements_by_android_uiautomator()
