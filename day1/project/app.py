import os,sys

from flask import Flask,url_for,render_template,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import click

WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"   # windows 平台
else:
    prefix = "sqlite:////"   # Mac,Linux 平台
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Mary'
db = SQLAlchemy(app)

#models 数据层
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    year = db.Column(db.String(4))


# 视图函数

# @app.route('/')
# @app.route('/home/')
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == "POST":
        #获取表单的数据
        title = request.form.get("title")
        year = request.form.get("year")
        #验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash("输入错误")
            return redirect(url_for('index'))
        # 将数据保存的数据库
        movie = Movie(title=title,year=year)    # 创建记录
        db.session.add(movie)
        db.session.commit()
        flash("创建成功")
        return redirect(url_for('index'))

    # print(url_for('index',name="hahah"))
    # user = User.query.first()
    movies = Movie.query.all()
    return render_template("index.html",movies=movies)


# 自定义命令
# 建立空数据库
@app.cli.command()   # 命令注册
@click.option('--drop',is_flag=True,help="先删除在创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成")


# 向空数据库插入数据
@app.cli.command()
def forge():
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
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo("导入数据库完成")


# 404 错误的处理函数
@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    return render_template('404.html')

# 上下文处理函数
@app.context_processor
def common_user():
    user = User.query.first()
    return dict(user=user)


# if __name__ == '__main__':
#     app.run(debug=True)