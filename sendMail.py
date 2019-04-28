#!/usr/bin/python
# -*- coding: UTF-8 -*-
#UxQhNd5AexAvVcBE
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'dong@wangdongdong.xyz'  # 发件人邮箱账号
my_pass = 'UxQhNd5AexAvVcBE'  # 发件人邮箱密码
my_user = '429240967@qq.com'  # 收件人邮箱账号，我这边发送给自己

class email():


    def mail(self,sendTo,contains):
        try:
            msg = MIMEText(contains, 'plain', 'utf-8')
            msg['From'] = formataddr(["MarkDown", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr([":", sendTo])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "MarkDownNotes密码找回"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.wangdongdong.xyz", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login("dong@wangdongdong.xyz", "Thomas310")  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [sendTo, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            return True
        except  Exception:
            return False




