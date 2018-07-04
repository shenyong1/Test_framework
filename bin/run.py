# -*- coding:utf-8 -*-
#date:  2018/6/2
import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from lib import tools
import datetime

def main():
    tools.makeCase()#自动生成py文件
    pass_count,fail_count,abs_path = tools.run_all_case()

    msg = '''
    大家好：
        本次接口测试结果如下：
            通过用例: %s条。
            失败用例: %s条。
            详细信息见附【%s】。
    '''%(pass_count,fail_count,os.path.basename(abs_path))
    today = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    title = '接口测试报告%s'%today

    # tools.sendmail(title,msg,abs_path)

main()
