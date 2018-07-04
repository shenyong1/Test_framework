# -*- coding:utf-8 -*-

import time,json

#获取时间，参数为当天日期前后加减值，如-1为昨天、1为明天
def GetTime(day=0):
    today = time.gmtime()
    year = str(today.tm_year)
    mon = str(today.tm_mon if today.tm_mon>10 else '0'+str(today.tm_mon))
    real_day = str(today.tm_mday + day)

    return year+mon+real_day


#json数据转换
class LoadsDumps(object):
    def dumps(self,data):
        if data:
            try:
                data = json.dumps(data,indent=4,ensure_ascii=False)
            except Exception as e:
                data = json.dumps(str(data),indent=4,ensure_ascii=False)

            return data
    def loads(self,data):
        return json.loads(data)


#获取随机数


if __name__ == '__main__':
    tt = GetTime()
    print(tt)
