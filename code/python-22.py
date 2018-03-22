# python mysql链接
import pymysql
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    connect = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='oa')
    # print(connect)
    cur=connect.cursor()
    cur.execute('select * from oa_admin')
    # print(cur.fetchmany());
    # print(type(cur.fetchall()))
    string ='<h1>python 操作数据库</h1><table border=1 cellspacing=0 cellpadding=5>'
    string +='<tr><th>ID</th><th>用户名</th><th>密码</th><th>状态</th></tr>'
    for i in cur.fetchall():
        string +='<tr>'
        for x in i:
            string +='<td>{}</td>'.format(x)
        string +='</tr>'
    string +='</table>'    
    return string

if __name__=='__main__':
    app.run(debug=True)