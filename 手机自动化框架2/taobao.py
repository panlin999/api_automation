from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

url = "127.0测试.0测试.1:4723/wd/hub"

param = {
  "deviceName": "c6yhprivnbfqw8pz",
  "platformName": "Android",
  "platformVersion": "12",
  "appPackage": "com.taobao.taobao",
  "appActivity": "com.taobao.tao.TBMainActivity",
  "noReset": "true"
}
driver = webdriver.Remote(url, param)

sleep(5)
el1 = driver.find_element_by_xpath(
  "//android.widget.FrameLayout[@content-desc=\"购物车\"]/android.widget.ImageView").click()
sleep(8)
el2 = driver.find_element_by_xpath(
  "//android.widget.FrameLayout[@content-desc=\"我的淘宝\"]/android.widget.ImageView").click()
sleep(5)
el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="设置")
sleep(5)
el3.click()
sleep(5)
el4 = driver.find_element_by_xpath(
  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout")
sleep(5)
el4.click()
