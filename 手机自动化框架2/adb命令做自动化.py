from appium import webdriver

###设置设备的连接地址
url = "http://127.0.0.1:4723/wd/hub"
###1设置设备的参数：desired_capabilities
data = {
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.kugou.android",
    "appActivity": "com.kugou.android.app.MediaActivity",
    "noReset": "true"
}
###2发指令到appnium server，复制给driver（得到一个对象）
driver = webdriver.Remote(url, data)
###3还需要做哪些前期的准备工作
###appnium server启动
####模拟器/真机必须能够被电脑所识别  ----》如何操作
###察看被测试的收手机设备是否已经连接上，如何连接上则可以进行后续操作，否则先连接上才能进行后续的操作
