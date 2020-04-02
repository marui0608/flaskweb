from flask import Flask,url_for
app = Flask(__name__)

# @app.route('/')
# @app.route('/home/')
@app.route('/index/<name>')
def index(name):
    print(url_for('index',name="hahah"))
    return "你好，{}！".format(name)