from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

data = {
    "appium:deviceName": "c6yhprivnbfqw8pz",
    "appium:platformName": "Android",
    "appium:platformVersion": "12",
    "appium:appPackager": "com.tencent.mm",
    "appium:appAcitivity": "com.tencent.mm.ui.LauncherUI",
    "appium:noReset": "true"
}
data1 = {
    "appium:deviceName": "c6yhprivnbfqw8pz",
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:appPackage": "com.tencent.mm",
    "appium:appActivity": "com.tencent.mm.ui.LauncherUI",
    "appium:noReset": "true"
}
url = "127.0.0.1:4723/wd/hub"
driver = webdriver.Remote(url, data1)
driver.implicitly_wait(5)
###通讯录
el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")
el1.click()
##点击添加
el1.click()
el2 = driver.find_element_by_xpath("//android.widget.RelativeLayout[@content-desc=\"更多功能按钮\"]/android.widget.ImageView")
el2.click()
##点击添加朋友
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
el3.click()
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout")
el4.click()
# el5=driver.find_elements_by_class_name("android.widget.LinearLayout")
el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="取消").click()
el21 = driver.find_element_by_id("com.tencent.mm:id/fz")
el21.click()
el8 = driver.find_element(by=AppiumBy.CLASS_NAME,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[1]")
el8.click()
el9 = driver.find_element(by=AppiumBy.CLASS_NAME,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout")
el9.click()
el10 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/l5g")
el10.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(352, 2260)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(571, 670)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(402, 2340)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(555, 816)
actions.w3c_actions.pointer_action.release()
actions.perform()

el11 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/by2")
el11.click()
el12 = driver.find_element(by=AppiumBy.CLASS_NAME,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
el12.click()
el13 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/f5")
el13.click()
el14 = driver.find_element(by=AppiumBy.CLASS_NAME,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[15]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
el14.click()
el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="返回")
el15.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(536, 1857)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(697, 444)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(483, 2133)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(705, 731)
actions.w3c_actions.pointer_action.release()
actions.perform()

el16 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/fz")
el16.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(27, 1088)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(877, 1076)
actions.w3c_actions.pointer_action.release()
actions.perform()
