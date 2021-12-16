# 下面四行导入依赖的包
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)

# 设置服务器所需信息 该部分需要修改
# outlook邮箱SMTP服务器地址

mail_host = 'smtp.gmail.com'

# 126邮箱用户名

mail_user = 'yunpeng'

# 密码(部分邮箱如qq邮箱为授权码)

mail_pass = 'hyp13801069546'

# 邮件发送方邮箱地址

sender = 'huayunpeng2017@gmail.com'

# 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发

receivers = ['huayunpeng2011@126.com']

# 以上部分需要修改

# 设置email信息

# 邮件内容设置

message = MIMEText('正文说点啥好呢', 'plain', 'utf-8')

# 邮件主题

message['Subject'] = ip

# 发送方信息

message['From'] = sender

# 接受方信息

message['To'] = receivers[0]

# 登录并发送邮件

server = smtplib.SMTP(mail_host, 587)

server.set_debuglevel(1)

server.ehlo()

server.starttls()

server.login(mail_user, mail_pass)

server.sendmail(sender, receivers, message.as_string())

server.quit()

exit()