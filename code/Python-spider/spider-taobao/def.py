import  os
import pymysql

list_dir = os.listdir('images')

print(list_dir)
db = pymysql.connect('192.168.1.249', 'root', 'yundian20180808', 'shopnc')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "SELECT t_id FROM shopnc_taobao_goods"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    list_dirs = []
    for i in results:
        list_dirs.append(i[0])


except:
    print("数据库链接失败")
db.close()