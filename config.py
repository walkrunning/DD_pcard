# appium连接的url 4.7.6
APPIUM_URL = "http://127.0.0.1:4723/wd/hub"
# 设备号 dos命令:adb devices 
DEVICE_NAME = "MKJNW17C13041697"
# 安卓版本
ANDROID_VERSION = "8.0.0"
# 是否有锁
IS_LOCK = True
# 锁类型
LOCK_TYPE = "pin"
# 解锁密文
LOCK_PWD = "1997"
# 每次等待元素出现的最长时间s
WAIT_EL_TIME = 10
# 上班时间 24小时制 第几秒是上班打卡截止时间 表示9点30是上班打卡终止时间 9 * 60 * 60 + 30 * 60
START_CLOCK_TIME = 9 * 60 * 60 + 20 * 60
# 下班时间 表示19点是下班打卡开始时间 19 * 60 * 60 + 0 * 60
OUT_CLOCK_TIME = 18 * 60 * 60 + 50 * 60
# 打卡浮动时间 秒
FL_CLOCK_TIME = 5 * 60
# 钉钉账号
DD_USERNAME = 
# 钉钉
DD_PWD = ""
# 定时执行时间 s
Interval_Time = 30
# 邮箱发送者
SEND_USER_MAIL = "674025810@qq.com"
# 邮箱授权码
SEND_PWD_MAIL = ""
# 邮箱的接收者账号
RECE_USER_MAIL = "674025810@qq.com"
#等待元素出现的最长时间
wait_el_time = 10
#失败重试的最大次数
retry_num = 3
#运行失败是否要再一次运行
flag = True
driver = None
