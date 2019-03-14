from flask import Flask, request, render_template, session, redirect, url_for, abort, make_response
app = Flask(__name__)

# @app.route('/error')
# def error():
#     abort(404)


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code


@app.errorhandler(InvalidUsage)
def invalid_useage(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    return response


@app.route('/exception')
def exception():
    raise InvalidUsage('大爷的', status_code=403)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = '123456'
    app.run()
