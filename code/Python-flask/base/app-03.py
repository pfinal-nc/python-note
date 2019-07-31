from flask import Flask,request
app = Flask(__name__)

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return 'POST请求'
    else:
        return 'GET请求'    

if __name__ == "__main__":
    app.run()