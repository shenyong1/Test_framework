import pymysql
from conf.setting import MYSQL_INFO
class MyDb(object):
    def __del__(self):
        #析构函数
        self.cur.close()
        self.coon.close()
        # print('over...')
    def __init__(self,
                 host,user,passwd,db,
                 port=3306,charset='utf8'):
        try:
            self.coon = pymysql.connect(
                host=host,user=user,passwd=passwd,port=port,charset=charset,db=db,
                autocommit=True,#自动提交
            )
        except Exception as e:
            print('数据库连接失败！%s'%e)
        else:
            self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)
    def ex_sql(self,sql):
        try:
            self.cur.execute(sql)
        except Exception as e:
            print('sql语句有问题，%s'%sql)
        else:
            self.res = self.cur.fetchall()
            return self.res



my_sql = MyDb(**MYSQL_INFO)

if __name__ == '__main__':
    # sql = 'select * from app_myuser'
    sql = 'select * from class where cid=1'
    res = my_sql.ex_sql(sql)
    print(res)

