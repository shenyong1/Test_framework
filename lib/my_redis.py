import redis
from conf.setting import REDIS
# r = redis.Redis()
class MyRedis():
	def __init__(self,host,port=6379,db=0):
		#构造函数
		try:
			self.r = redis.Redis(host=host,port=port,db=db)
			# r = redis.ConnectionPool(host=ip,password=password,port=port,db=db)
		except Exception as e:
			print('redis连接失败，错误信息%s'%e)
	def str_get(self,k):
		res = self.r.get(k)
		if res:
			return res.decode()
	def str_set(self,k,v,time=None):
		self.r.set(k,v,time)
	def delete(self,k):
		tag = self.r.exists(k) #判断这个key是否存在
		if tag:
			self.r.delete(k)
			print('删除成功')
		else:
			print('这个key不存在')
	def hash_get(self,name,k):
		res = self.r.hget(name,k)
		if res:
			return res.decode()
	def hash_set(self,name,k,v):
		self.r.hset(name,k,v)
	def hash_getall(self,name):
		data = {}
		# {b'12': b'1212', b'3': b'sdad', b'4': b'asdadsa'}
		res = self.r.hgetall(name)
		if res:
			for k,v in res.items():
				k =  k.decode()
				v = v.decode()
				data[k]=v
		return data
	def hash_del(self,name,k):
		res = self.r.hdel(name,k)
		if res:
			print('删除成功')
			return 1
		else:
			print('删除失败，该key不存在')
			return 0

	@property
	def clean_redis(self):
		self.r.flushdb()  #清1空redis
		print('清空redis成功！')
		return 0


my_redis = MyRedis(**REDIS)







