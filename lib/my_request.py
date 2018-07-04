# -*- coding:utf-8 -*-
#date:  2018/6/9
import requests
from lib.log import logger

class MyRequest():

    @staticmethod
    def post(url,data=None,cookie=None,header=None,is_json=False,files=None):
        data = data if data else {}
        cookie = cookie if cookie else {}
        header = header if header else {}
        files = files if files else {}
        try:
            if is_json:
                res = requests.post(url,json=data,cookies=cookie,headers=header,verify=False,files=files).text
            else:
                res = requests.post(url,data=data,cookies=cookie,headers=header,verify=False,files=files).text
        except Exception as e:
            logger.error('异常信息：接口调用失败！ url 【%s】 data 【%s】'%(url,data))
            res = {'error':str(e)}

        return res

    @staticmethod
    def get(url, data=None, cookie=None, header=None):
        data = data if data else {}
        cookie = cookie if cookie else {}
        header = header if header else {}
        try:
            res = requests.get(url, params=data, cookies=cookie, headers=header,verify=False).json()
            #verify=False 的意思是https能访问
        except Exception as e:
            logger.error('异常信息：接口调用失败！ url 【%s】 data 【%s】' % (url, data))
            res = {'error': str(e)}

        return res

