# -*- coding=utf-8 -*-
from retrying import retry
import random
import datetime


@retry(stop_max_attempt_number=3)
def tests(func):
    return func()


def run():
    i = random.randint(0, 10)
    if i < 9:
        print("重试" + str(i))
        raise Exception('yc')
    else:
        return i


if __name__ == '__main__':
    now = datetime.datetime.now()
    print(now.hour * 60 * 60 + now.minute * 60 + now.second)
