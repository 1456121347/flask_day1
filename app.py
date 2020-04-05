import os,sys

from flask import Flask,url_for,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy  
import click


WIN = sys.platform.startswith('win') # 判断是不是windows系统
if WIN:
    prefix = "sqlite:///" # window系统
else:
    prefix = "sqlite:////" # Mac linux系统

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 对内存做优化
app.config['SECRET_KEY'] = '1903_dev' 

db = SQLAlchemy(app) # 初始化app

# models 数据层
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20))
    year = db.Column(db.String(4))




# views 视图函数
@app.route('/', methods=['GET','POST'])
def index():
    movie = Movie.query.all()
    if request.method == 'POST':
        g_title = request.form.get('title')
        g_year = request.form.get('year')
        # 验证数据
        if not g_title or not g_year or len(g_year)>4 or len(g_title)>20:
            flash('输入错误！')
            return redirect(url_for('index'))
        # 将数据保存到数据库    
        mov = Movie(title=g_title,year=g_year)
        db.session.add(mov)
        db.session.commit()
        flash('提交成功！')
        return redirect(url_for('index'))

    return render_template('index.html',movie=movie)

# 自定义命令
# 建立空数据库
@app.cli.command() # 注册为命令
@click.option('--drop',is_flag=True,help="先删除在创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成！")

# 向数据库插入数据
@app.cli.command()
def forge():
    # name = '席栋祥'
    # movie = [
    #     {'title':"大赢家",'year':"2020"},
    #     {'title':"囧妈",'year':"2020"},
    #     {'title':"疯狂外星人",'year':"2019"},
    #     {'title':"战狼",'year':"2017"}
    # ]
    user = User(name=name)
    db.session.add(user)
    for m in movie:
        mov = Movie(title=m['title'],year=m['year'])
        db.session.add(mov)
    db.session.commit()
    click.echo("导入数据完成！")

# 错误信息页面
@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('404.html')


# 模板上下文出力函数
@app.context_processor
def common_user():
    user = User.query.first()
    return dict(user=user)




