# -*- coding:utf-8 -*-
#date:  2018/5/26
import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
import yagmail
from conf.setting import *
from lib.log import apt_log
def sendmail(title,content,attrs=None):
    m = yagmail.SMTP(host=MAIL_HOST,user=USER,password=PASSWORD,smtp_ssl=True)
    try:
        m.send(to=TO,
               subject=title,
               contents=content,
               attachments=attrs
               )
        apt_log.info("邮件发送成功！")

    except Exception as e:
        print('error')

if __name__ == '__main__':
    sendmail('测试用例运行结果','哈哈哈哈')