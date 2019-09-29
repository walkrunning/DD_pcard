# -*- coding=utf-8 -*-
import config
from main.cmEnum import exceptEum
from main.emailSendQQ import sendEmail


def find_element_by_id(resourceId):
    try:
        config.driver.implicitly_wait(config.wait_el_time)
        return config.driver.find_element_by_id(resourceId)
    except Exception as e:
        do_except(resourceId, e)


def find_element_by_xpath(xpath):
    try:
        config.driver.implicitly_wait(config.wait_el_time)
        return config.driver.find_element_by_xpath(xpath)
    except Exception as e:
        do_except(xpath, e)


def is_element_exist_by_xpath(xpath):
    try:
        config.driver.implicitly_wait(config.wait_el_time)
        return config.driver.find_element_by_xpath(xpath).is_displayed()
    except Exception as e:
        return False


def is_element_exist_by_id(id):
    try:
        config.driver.implicitly_wait(config.wait_el_time)
        return config.driver.find_element_by_id(id).is_displayed()
    except Exception as e:
        return False


def find_elements_by_android_uiautomator(des):
    try:
        return config.driver.find_elements_by_android_uiautomator(des)
    except Exception as e:
        do_except(des, e)


def find_element_by_android_uiautomator(des):
    try:
        config.driver.implicitly_wait(config.wait_el_time)
        return config.driver.find_element_by_android_uiautomator(des)
    except Exception as e:
        do_except(des, e)


def do_except(msg, e):
    sendEmail("失败", msg + ":" + exceptEum.NOT_FIND_EL.value)
    print(e)
    config.driver.quit()


if __name__ == '__main__':
    find_element_by_id("")
