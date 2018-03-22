from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/lists', methods=['GET'])
def lists():
    str = '<h1>这个是表格</h1>'
    str +='<table border=1 cellspacing=0 cellpadding="5">'
    for i in range(10):
        str +='<tr>'
        for j in range(10):
            str +='<td>%d * %d = %d </td>' % (j,i,j*i)
        str +='</tr>'
    str +='</table>'    
    return str  

if __name__ == '__main__':
    app.run()
