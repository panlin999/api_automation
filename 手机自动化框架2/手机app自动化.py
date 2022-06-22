from time import sleep

from appium import webdriver

url = "127.0.0.1:4723/wd/hub"

param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.tencent.mobileqq",
  "appActivity": "com.tencent.mobileqq.activity.SplashActivity"
}
sleep(3)
driver = webdriver.Remote(url, param)
sleep(3)
el1 = driver.find_element_by_accessibility_id("QQ")
el1.click()
sleep(3)
el2 = driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
el2.click()
sleep(3)
el3 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el3.send_keys("2823677281")
sleep(3)
el4 = driver.find_element_by_accessibility_id("密码 安全")
el4.send_keys("azxcvbnm")
el5 = driver.find_element_by_accessibility_id("登录")
el5.click()
sleep(3)
el6 = driver.find_element_by_accessibility_id("确定")
el6.click()
