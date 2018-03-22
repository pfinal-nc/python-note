from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/user/<username>')
def show_user_name(username):
    return 'User %s' % username

if __name__ == '__main__':
    app = create_app(config="config.yaml")
    if app.debug: use_debugger = True
    try:
        # Disable Flask's debugger if external debugger is requested
        use_debugger = not(app.config.get('DEBUG_WITH_APTANA'))
    except:
        pass
    app.run(use_debugger=use_debugger, debug=app.debug,
            use_reloader=use_debugger, host='0.0.0.0') 

