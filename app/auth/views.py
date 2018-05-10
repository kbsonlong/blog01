#coding:utf8

from flask import Blueprint , render_template,request,session,redirect,url_for

#  创建蓝图 第一个参数为蓝图的名字
login = Blueprint('login',__name__)

@login.route('/register')
def register():
    return 'register'


@login.route('/login')
def login_demo():
    """View function for home page"""
    context={}
    info =''
    username = ''
    # 判断是否是验证提交
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = {'code':'1'}
        if result['code'] == 0:
            session['username'] = username
            session['author'] = result['authorization']
            return redirect(url_for('home'))
        elif result['code'] == 1:
            info = result['errmsg']
    return render_template('auth/login.html',info = info ,username = username)