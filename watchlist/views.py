from watchlist import app,db
from flask_login import login_user,logout_user,login_required,current_user
from flask import Flask,url_for,render_template,request,redirect,flash
from watchlist.models import User,Movie
import click



# views 视图函数
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        # 获取表单的数据
        title = request.form.get('title')
        year = request.form.get('year')
        # 验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash('输入错误')
            return redirect(url_for('index'))
        # 将数据保存到数据库
        movie = Movie(title=title,year=year) # 创建记录
        db.session.add(movie)
        db.session.commit()
        flash('创建成功')
        return redirect(url_for('index'))

    movies = Movie.query.all()
    return render_template('index.html',movies=movies)

# 更新/movie/edit
@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST']) 
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        if not title or not year or len(year)>4 or len(title)>60:
            flash('输入有误')
            return redirect(url_for('edit'),movie_id = movie_id)
        movie.title = title
        movie.year = year
        db.session.commit()
        flash('电影更新完成')
        return redirect(url_for('index'))
    return render_template('edit.html',movie=movie)

# delete视图函数
@app.route('/movie/delete/<int:movie_id>',methods=['GET','POST']) 
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('删除完成')
    return redirect(url_for('index'))

# 登录
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('输入有误')
            return redirect(url_for('login'))
        user = User.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('登录成功')
            return redirect(url_for('index'))
        flash('验证失败')
        return redirect(url_for('login'))

    return render_template('login.html')

# logout 登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('退出成功')
    return redirect(url_for('index'))

# settings 设置
@app.route('/settings',methods=['POST','GET'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']
        if not name or len(name)>20:
            flash('输入错误')
            return redirect(url_for('settings'))
        current_user.name = name
        db.session.commit()
        flash('名字已经更新')
        return redirect(url_for('index'))

    return render_template('settings.html')


# 向空数据库中插入数据
@app.cli.command()
def forge():
    # name = "席栋祥"
    movies = [
       {'title':"大赢家","year":"2020"},
       {'title':"囧妈","year":"2020"},
       {'title':"疯狂外星人","year":"2019"},
       {'title':"战狼","year":"2017"},
       {'title':"速度与激情8","year":"2018"},
       {'title':"极限特工","year":"2010"},
       {'title':"叶问","year":"2014"},
       {'title':"杀破狼","year":"2000"},
       {'title':"叶问2","year":"2016"}
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo("导入数据完成")


# 自定义指令，生成管理员账号flask admin
# 输入用户名Admin,密码，确认密码
@app.cli.command()
@click.option('--username',prompt=True,help='登录的用户名')
@click.option('--password',prompt=True,help='登录的密码',confirmation_prompt=True,hide_input=True)
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo('更新管理员用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建管理员账户')
        user = User(username=username,name='Admin')
        user.set_password(password)
        db.session.add(user)
    
    db.session.commit()
    click.echo('管理员账号更新/创建完成')

