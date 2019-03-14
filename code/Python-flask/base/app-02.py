from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = '树先生'
    return 'Hello %s' % name

if __name__ == "__main__":
    app.run()