# -*- coding: utf8 -*-
import socket
import config
from email.header import Header
from email.mime.text import MIMEText
import smtplib


def sendEmail(subject, msg):
    """
    邮件通知
    :param str: email content
    :return:
    """
    try:
        receiver = config.RECE_USER_MAIL
        username = config.SEND_USER_MAIL
        password = config.SEND_PWD_MAIL
        host = "smtp.qq.com"
        s = "{0}".format(msg)

        msg = MIMEText(s, 'plain', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
        msg['Subject'] = Header("dd:" + subject, 'utf-8')
        msg['From'] = username
        msg['To'] = receiver

        try:
            smtp = smtplib.SMTP_SSL(host)
            smtp.connect(host)
        except socket.error:
            smtp = smtplib.SMTP()
            smtp.connect(host)
        smtp.connect(host)
        smtp.login(username, password)
        smtp.sendmail(username, receiver.split(","), msg.as_string())
        smtp.quit()
        print(u"邮件已通知, 请查收")
    except Exception as e:
        print(u"邮件配置有误{}".format(e))


if __name__ == '__main__':
    sendEmail(1)
