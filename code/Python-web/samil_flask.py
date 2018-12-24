from flask import Flask, render_template, request, url_for, session, redirect
import os
from datetime import timedelta
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
@app.route('/')
def index():
    if 'email' in session:
        name = session.get('email')
        banner = _get_banner() if len(_get_banner()) > 0 else False 
        return render_template('index.html', name=name, banners=banner)
    else:
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['email'], request.form['password']):
            if request.form['email'] != 'lampxiezi@163.com':
                error = '邮箱账号错误'
            if request.form['password'] != '123456':
                error = '密码错误'
            session.permanent = True
            if session.get('email'):
                session.pop('email')
            session['email'] = request.form['email']
            return redirect(url_for('index'))
        else:
            error = '邮箱或密码不能为空'
    return render_template('login.html', error=error)
def valid_login(email, password):
    if email == '':
        return False
    if password == '':
        return False
    return True


def _get_banner():
    banners = []
    bannerdir = './static/banners'
    banner_list = os.listdir(bannerdir)
    if len(banner_list) > 0:
        for banner_name in banner_list:
            path = os.path.join('banners/',banner_name)
            banners.append(path) 
    return banners
if __name__ == '__main__':
    app.debug = True
    app.run()
