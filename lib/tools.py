# -*- coding:utf-8 -*-
#date:  2018/6/2
import os,unittest,datetime,yagmail
from conf.setting import *
from BeautifulReport import BeautifulReport as bf

def makeCase():
    all_yaml = os.listdir(YAML_PATH)
    base_case_str = open(CASE_TEMPLATE,encoding='utf8').read() #读取模版数据

    for yaml in all_yaml:
        if yaml.endswith('.yaml') or yaml.endswith('.yml'):
            class_name = yaml.replace('.yaml','').replace('.yml','').capitalize() #首字母大写
            file_name = os.path.join(YAML_PATH,yaml)
            content = base_case_str %(class_name,file_name)

            py_file_name = os.path.join(CASE_PATH,class_name) #py文件存在的路径
            open('%s.py'%py_file_name,'w',encoding='utf8').write(content)

def run_all_case():
    suite = unittest.TestSuite()
    all_py = unittest.defaultTestLoader.discover(CASE_PATH,'*.py') #寻找Py文件
    [suite.addTests(py) for py in all_py] #将测试用例(class)添加到测试集

    run = bf(suite)
    today = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    title = '%s_接口测试报告.html'%today
    report_abs_path = os.path.join(REPORT_PATH,title)
    # report_abs_path = os.path.join('.',title)
    run.report(title,filename=title,log_path=REPORT_PATH)

    return run.success_count,run.failure_count,report_abs_path

def sendmail(title,content,attrs=None):
    m = yagmail.SMTP(host=MAIL_HOST,user=USER,password=PASSWORD)

    m.send(to=TO,
           subject=title,
           contents=content,
           attachments=attrs
           )


if __name__ == '__main__':
    run_all_case()