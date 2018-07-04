# -*- coding:utf-8 -*-
#date:  2018/6/2
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MAIL_HOST = 'smtp.qq.com'
USER = '2890104046@qq.com'
PASSWORD = 'xybzqknuhdgfddah'
TO = [
    '136945832@qq.com'
]

LOG_LEVER = 'debug'

LOG_NAME='utp.logs'

#日志路径
LOG_PATH = os.path.join(BASE_PATH,'logs')
#用例路径
CASE_PATH = os.path.join(BASE_PATH,'cases')
#yaml文件路径
YAML_PATH = os.path.join(BASE_PATH,'case_data')
#用例模版路径
CASE_TEMPLATE = os.path.join(BASE_PATH,'conf','base.txt')
#接口地址
BASE_URL = 'http://10.32.231.205:8080/'

BASE_INNID = 4786
#报告生成地址
REPORT_PATH = os.path.join(BASE_PATH,'report')


MYSQL_INFO = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'passwd':'Shen19920616',
    'charset':'utf8',
    'db':'shenyong_test'
}

REDIS = {
    'host':'127.0.0.1',
    'port':'6379',
}