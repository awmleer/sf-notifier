from urllib import request
import json
import config

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))






# 读取上次的长度记录
with open('data', 'r') as f:
    length=int(f.read())
print(length)

# 发送请求
with request.urlopen('http://www.sf-express.com/sf-service-web/service/bills/'+config.ORDER_ID+'/routes?app=bill&lang=sc&region=cn&translate=') as f:
    data = f.read()
    if f.status==200:
        obj=json.loads(data.decode('utf-8'))
        # print('Data:', data.decode('utf-8'))
        print(obj[0]['id'])
        routes=obj[0]['routes']
        if len(routes)>length:
            length=len(routes)
            # 发送邮件
            msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
            msg['From'] = _format_addr('Python爱好者 <%s>' % config.SEND_MAIL)
            msg['To'] = _format_addr('管理员 <%s>' % config.RECEIVE_MAIL)
            msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

            server = smtplib.SMTP(config.SMTP_SERVER, 25)
            server.set_debuglevel(1)
            server.login(config.SEND_MAIL, config.SEND_PASSWORD)
            server.sendmail(config.SEND_MAIL, [config.RECEIVE_MAIL], msg.as_string())
            server.quit()
            print('mail!!!')
            # 更新长度记录
            with open('data', 'w') as f:
                f.write(str(length))
            # print(f.read())

        print(len(routes))
    # for k, v in f.getheaders():
    #     print('%s: %s' % (k, v))
