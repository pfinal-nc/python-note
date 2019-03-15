from flask import Flask, request, render_template, session,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/article')
def article():
    return render_template('article.html')

if __name__ == "__main__":
    app.debug = True
    app.secret_key = '123456'
    app.run()