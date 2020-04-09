from watchlist import app
from flask import render_template


# 404 错误的处理函数
@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    return render_template('404.html')