from flask import Flask, request, render_template, session,redirect,url_for
app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
        else:
            return redirect(url_for('login'))
    if 'user' in session:
        return 'Hello %s !' % session['user']
    else:
        title = request.args.get('title', 'PFinal社区')
        return render_template('login.html', title=title)

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))
if __name__ == "__main__":
    app.debug = True
    app.secret_key = '123456'
    app.run()
