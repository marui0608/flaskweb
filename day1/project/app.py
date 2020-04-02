from flask import Flask,url_for,render_template
app = Flask(__name__)

# @app.route('/')
# @app.route('/home/')
@app.route('/')
def index():
    # print(url_for('index',name="hahah"))
    name = "Mary"
    movies = [
        {'title':"大赢家","year":"2020"},
        {'title':"囧妈","year":"2018"},
        {'title':"疯狂外星人","year":"2019"},
        {'title':"速度与激情8","year":"2016"},
        {'title':"极限特工","year":"20115"},
        {'title':"叶问","year":"2014"},
        {'title':"杀破狼","year":"2013"},
        {'title':"叶问2","year":"2012"},
        {'title':"叶问4","year":"2010"},
    ]
    return render_template("index.html",name=name,movies=movies)





# if __name__ == '__main__':
#     app.run(debug=True)