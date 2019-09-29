# -*- coding=utf-8 -*-
import datetime, time, random, threading
import config
from main.loadDriver import auto_activity

# 上班时间
START_TIME = config.START_CLOCK_TIME - random.randint(1, config.FL_CLOCK_TIME)
# 下班时间
OUT_TIME = config.OUT_CLOCK_TIME + random.randint(1, config.FL_CLOCK_TIME)


def count_time():
    now = datetime.datetime.now()
    now_sec = now.hour * 60 * 60 + now.minute * 60 + now.second

    s = "距离上班打卡已过去:" + str(now_sec - START_TIME) if ((now_sec - START_TIME) > 0) else "距离上班打卡还有:" + str(
        now_sec - START_TIME)
    s += "s,"
    s += "距离下班打卡已过去:" + str(OUT_TIME - now_sec) if ((OUT_TIME - now_sec) < 0) else "距离下班打卡还有:" + str(
        OUT_TIME - now_sec)
    s += "s"
    print(s.replace("-", ""))

    if 0 < (now_sec - START_TIME) < 30:
        auto_activity()
        return
    elif 0 < (OUT_TIME - now_sec) < 30:
        auto_activity()
        return


def task():
    while True:
        count_time()
        time.sleep(30)


def startTask():
    thread = threading.Thread(target=task())
    threading.start()


if __name__ == '__main__':
    startTask()
