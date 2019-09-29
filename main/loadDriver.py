# -*- coding=utf-8 -*-
# 加载appium
from appium import webdriver

import config
import main.findElUtils as findEl
from main.cmEnum import eltagEum
from main.emailSendQQ import sendEmail

# 配置启动需要的参数
desired_caps = {
    'platformName': 'Android',
    'deviceName': config.DEVICE_NAME,
    'platforVersion': config.ANDROID_VERSION,
    'automationName': 'Uiautomator2',
    'appPackage': "com.alibaba.android.rimet",
    'appActivity': "com.alibaba.android.rimet.biz.LaunchHomeActivity",
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True
}

if config.IS_LOCK:
    desired_caps["unlockType"] = config.LOCK_TYPE
    desired_caps["unlockKey"] = config.LOCK_PWD


# 启动app自动化测试
def start_appium():
    try:
        config.driver = webdriver.Remote(config.APPIUM_URL, desired_caps)
    except Exception as e:
        if config.flag:
            config.flag = False
            start_appium()
        else:
            sendEmail("失败", "appium启动失败")
            print(format(e))


# 检测有没有弹框 这个和手机有关
def check_alert():
    try:
        config.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("' + eltagEum.ALERT_USB_TEXT.value + '")')
    except Exception:
        print("没有检测到usb提示弹窗")
    else:
        config.driver.find_element_by_id(eltagEum.ALERT_USB_EXIT_ID.value).click()
    try:
        config.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("' + eltagEum.ALERT_SYS_TEXT.value + '")')
    except Exception:
        print("没有检测到系统更新提示弹窗")
    else:
        config.driver.find_element_by_id(eltagEum.ALERT_SYS_EXIT_ID.value).click()


# 判断要不要登录
def check_login():
    if findEl.is_element_exist_by_id(eltagEum.LOGIN_BTN_ID.value):
        login_btn = findEl.find_element_by_id(eltagEum.LOGIN_BTN_ID.value)
        login_btn.click()
        findEl.find_element_by_id(eltagEum.EL_USER_EDIT_ID.value).send_keys(config.DD_USERNAME)
        findEl.find_element_by_id(eltagEum.EL_PASSWORD_EDIT_ID.value).send_keys(config.DD_PWD)
        login_btn.click()


def auto_activity():
    start_appium()
    check_alert()
    check_login()
    # 匹配以‘工作’开头的元素
    work_els = findEl.find_elements_by_android_uiautomator('new UiSelector().descriptionMatches("^工作.*")')
    # 点击最后一个
    work_els[len(work_els) - 1].click()
    # 到考勤打卡页面
    findEl.find_element_by_android_uiautomator('new UiSelector().description("考勤打卡")').click()
    # 打卡
    auto_car = findEl.find_element_by_android_uiautomator(
        'new UiSelector().descriptionMatches(".*打卡$")')
    desc = auto_car.get_attribute(name='content-desc')
    if desc != '外勤打卡':
        sendEmail("ok", desc)
    else:
        sendEmail("警告", desc)
    # 关闭app
    config.driver.close_app()
    # 锁屏
    config.driver.lock()
    # 关闭
    config.driver.quit()


if __name__ == '__main__':
    auto_activity()
