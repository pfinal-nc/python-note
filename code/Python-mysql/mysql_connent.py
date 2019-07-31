import pymysql
db = pymysql.connect("localhost","root","root","scrapy_ip" )
print(db)
cursor = db.cursor() # 使用 cursor() 方法创建一个游标对象 cursor
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("数据库版本: %s" % data)
# 关闭数据库链接
db.close()