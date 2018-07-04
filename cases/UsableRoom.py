# -*- coding:utf-8 -*-

import unittest,json
from lib.my_request import MyRequest
from conf.setting import BASE_URL
from urllib import parse
from lib.commonTools import GetTime
from lib.log import logger

class UsableRoom(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.header = {'Content-Type': 'application/json'}
        data = {'username': '18221293942',
                'password': '123456'}
        res = MyRequest.post(url='http://10.32.231.205:8080/api/v1/pms/login',
                            data=data,
                            header=cls.header,
                             is_json=True)
        res = json.loads(res)

        cls.bid = res.get('data').get('bid')

    def get_iniId(self):
        url = 'api/v1/pms/api/stat2/allInn?bid=%s'
        real_url = parse.urljoin(BASE_URL,url%self.bid)
        data = {'startDate':GetTime(),
                'endDate':GetTime(1)}
        res = MyRequest.post(real_url,
                             data=data,
                             header=self.header,
                             is_json=True)
        res = json.loads(res)
        innId = res['data']['innList'][1]['innId']
        return innId

    def test_getroom(self):
        '''正常获取可用房间'''
        url = 'api/v1/pms/api/room/getUsableForOverNight?bid=%s'
        real_url = parse.urljoin(BASE_URL,url%self.bid)
        print(real_url)

        innId = self.get_iniId()

        data = {'innId':innId,
                'checkinDate':GetTime(),
                'checkoutDate':GetTime(1)}

        # logger.info('data：%s'%data)

        res = MyRequest.post(real_url,
                             data=data,
                             header=self.header,
                             is_json=True)
        print('post')
        print(data)

        self.assertIn('成功',res,msg='获取房间信息失败！')


