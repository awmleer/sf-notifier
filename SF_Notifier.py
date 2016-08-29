from urllib import request
import json
import config

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
            # dosomething()
            print('mail!!!')
            # 更新长度记录
            with open('data', 'w') as f:
                f.write(str(length))
            # print(f.read())

        print(len(routes))
    # for k, v in f.getheaders():
    #     print('%s: %s' % (k, v))
