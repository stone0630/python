# -*- coding: utf-8 -*-
# 发送邮件的库
import smtplib
# 邮件文本库
from email.mime.text import MIMEText

# smtp服务器
SMTPSERVER = 'smtp.163.com'

# 发邮件的地址
SENDER = 'cuizhenzhen0630@163.com'

# 授权码(网易邮箱中的授权码设置)
PASSWD = '123qwe123'

# 设置发送内容
MESSAGE = 'this is a test email'
# 转换为python能识别的的格式
MSG = MIMEText(MESSAGE)

#标题
MSG['Subject'] = 'test_email'

# 发送者
MSG['From'] = SENDER

# (创建smtp服务器， 25是发送端口)
mailServer = smtplib.SMTP(SMTPSERVER, 25)

# 登录邮件服务器
mailServer.login(SENDER, PASSWD)

# 发送邮件(列表内是接收者的邮件地址)
mailServer.sendmail(SENDER, ['937890478@qq.com', ], MSG.as_string())

# 退出邮箱
mailServer.quit()


