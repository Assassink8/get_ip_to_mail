'''
Author: Assassin_k8
Date: 2023-04-25 18:21:12
LastEditors: Do not edit
LastEditTime: 2023-04-25 20:22:41
FilePath: \getIP\getipv6.py
'''
#!/usr/bin/env python
import requests,os,time
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import asctime
import socket
import configparser


HOUR = 60*60
MINUTE = 60
SECOND = 1


#get current ip address
def getIP():
    hostname = socket.gethostname()
    addr_infos = socket.getaddrinfo(hostname, None)
    ips = set([addr_info[-1][0] for addr_info in addr_infos])
    ipv6 = max(ips,key=len)
    return ipv6


def send_an_email(email_content,config):           # email_content是一个字符串
    mail_host = "smtp.126.com"             # 这个去邮箱找
    mail_user = config.get('mail','mail_user')                          #发送的邮箱地址
    mail_auth_code = config.get('mail','mail_auth_code')                     #授权码，不是邮箱的登陆密码
    mail_sender = config.get('mail','mail_sender')                  # 用mail_user 作为发送人
    mail_receivers = config.get('mail','mail_receivers') # 接收人列表
    message = MIMEMultipart()
    message['From'] = Header(mail_sender)   # 寄件人
    message['Subject'] = Header("IPV6地址")
    message.attach(MIMEText(asctime(), 'plain', 'utf-8'))
    message.attach(MIMEText(email_content, 'plain', 'utf-8'))
    # print("message is {}".format(message.as_string())) # debug用
    smtpObj = smtplib.SMTP(mail_host)
    # smtpObj.set_debuglevel(1) # 同样是debug用的
    smtpObj.login(mail_user, mail_auth_code) # 登陆
    smtpObj.sendmail(mail_sender, mail_receivers, message.as_string()) # 真正发送邮件就是这里


def main():
    config = configparser.ConfigParser()
    config.read("config.ini", encoding="utf-8")
    ip = config.get('ip','ipv6')
    while True:
        new_ip = getIP()
        if new_ip != ip:
            send_an_email("IPV6地址更改"+new_ip, config)
            config.set('ip','ipv6',new_ip)
            config.write(open('config.ini','w',encoding='utf-8'))
        # else:
        #     send_an_email("IPV6地址未更改",config)
        time.sleep(5*HOUR)


if __name__ == '__main__':
    main()
