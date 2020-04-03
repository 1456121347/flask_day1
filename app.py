import os,sys

from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy  
import click


WIN = sys.platform.startswith('win') # 判断是不是windows系统
if WIN:
    prefix = "sqlite:///" # window系统
else:
    prefix = "sqlite:////" # Mac linux系统

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] =  prefix + os.path.join(app.root_path,'data.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 对内存做优化

db = SQLAlchemy(app) # 初始化app

# # models 数据层
# class User(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(20))

# class Movie(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(20))
#     year = db.Column(db.String(4))




# views 视图函数
@app.route('/')
def index():
    name = '席栋祥'
    movie = [
        {'title':"大赢家",'year':"2020"},
        {'title':"囧妈",'year':"2020"},
        {'title':"疯狂外星人",'year':"2019"},
        {'title':"战狼",'year':"2005"},
        {'title':"战狼2",'year':"2017"},
        {'title':"非常完美",'year':"2017"},
        {'title':"非常完美",'year':"2017"},
    ]
    # name = User.query.all()
    # movie = Movie.query.all()
    return render_template('index.html',name=name,movie=movie)

# 自定义命令
@app.cli.command() # 注册为命令
@click.option('--drop',is_flag=True,help="先删除在创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成！")



# @app.errorhandler(404)
# def pa (e):
#     name =User.query.all()
#     return render_template("404.html",name = name)
