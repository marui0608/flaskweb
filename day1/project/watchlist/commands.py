from watchlist import app,db
from watchlist.models import User,Movie
import click

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
    # name = "Mary"
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
    # user = User(name=name)
    # db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo("导入数据库完成")

#自定义指令，生成管理员账号flask admin
#输入用户名Admin，密码，确认密码
@app.cli.command()
@click.option('--username',prompt=True,help='登陆用户名')
@click.option('--password',prompt=True,help="登录密码",confirmation_prompt=True,hide_input=True)
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo("更新管理员账户")
        user.username = username
        user.set_password(password)
    else:
        click.echo("创建管理员账户")
        user = User(username=username,name='Admin')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo("管理员账号更新/创建完成")