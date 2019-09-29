from enum import Enum


class exceptEum(Enum):
    NOT_FIND_EL = "元素没有找到"


class eltagEum(Enum):
    # usb选择提示元素的text
    ALERT_USB_TEXT = "USB 连接方式"
    # 系统更新提示元素的text
    ALERT_SYS_TEXT = "系统更新"
    # 取消usb选择提示的元素id
    ALERT_USB_EXIT_ID = "android:id/button2"
    # 取消系统提示的元素id
    ALERT_SYS_EXIT_ID = "android:id/button3"
    # 登录按钮的ID
    LOGIN_BTN_ID = "com.alibaba.android.rimet:id/tv"
    # 输入用户名的元素ID
    EL_USER_EDIT_ID = "com.alibaba.android.rimet:id/et_phone_input"
    # 输入用户密码的元素id
    EL_PASSWORD_EDIT_ID = "com.alibaba.android.rimet:id/et_pwd_login"
    # 跳转到 工作 界面的元素的xpath
    EL_WORK_PAGE_XPATH = "//android.widget.RelativeLayout[@content-desc='工作']"


if __name__ == '__main__':
    print(exceptEum.NOT_FIND_EL.value)
