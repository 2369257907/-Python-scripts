import time
import datetime
import requests
import pytz
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendEmil():
    # smtplib模块主要负责发送邮件：是一个发送邮件的动作，连接邮箱服务器，登录邮箱，发送邮件（有发件人，收信人，邮件内容）。
    # email模块主要负责构造邮件：指的是邮箱页面显示的一些构造，如发件人，收件人，主题，正文，附件等。
    # if (code == 200):
    host_server = 'smtp.qq.com'  # qq邮箱smtp服务器
    sender_qq = 'xxxxx@qq.com'  # 发件人邮箱
    pwd = 'qraonwvyndsads'    #smtp邮箱授权码
    receiver = ['xxxx@qq.com']  # 收件人邮箱


    tz = pytz.timezone('Asia/Shanghai')
    date_p = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M")   #设置时区
    str_p = str(date_p)
    mail_title = str_p + '报警'  # 邮件标题
    mail_content = "【网站异常报警】您管理的xxx网页发生异常，现已无法正常访问，请及时处理"  # 邮件正文内容
    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    # msg["To"] = Header("测试邮箱",'utf-8')
    msg['To'] = ";".join(receiver)
    # 邮件正文内容
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    smtp = SMTP_SSL(host_server)  # ssl登录

    smtp.login(sender_qq, pwd)

    smtp.sendmail(sender_qq, receiver, msg.as_string())

    # quit():用于结束SMTP会话。
    smtp.quit()


def check_status():
    response = requests.get("http://xxxx")  #监控的网站网址
    code = response.status_code
    print(code)


def main():
    try:
        check_status()
    except:
        sendEmil()


if __name__ == "__main__":
    main()
