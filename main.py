# coding: utf-8

from flask import Flask,redirect,url_for
from config import DevConfig
from app.auth.views import login
from app.api.api_demo import api

##当Flask引用模板templates时，默认是从当前目录检索templates，如果templates不是放在main.py目录下，需要配置template_folder，静态文件static也是一样

app = Flask(__name__,template_folder='app/templates',static_folder="app/static",static_url_path="/static")

# Get the config from object of DecConfig
# 使用 onfig.from_object() 而不使用 app.config['DEBUG'] 是因为这样可以加载 class DevConfig 的配置变量集合，而不需要一项一项的添加和修改。
app.config.from_object(DevConfig)

# 注册蓝图 第一个参数 是蓝图对象
# app.register_blueprint(login)
app.register_blueprint(api)
app.register_blueprint(login)


@app.route('/')
def index():
    ##url_for(路由信息login注册的蓝图，home是处理函数)
    return redirect(url_for('login.home'))


if __name__ == '__main__':
    print(app.url_map)
    app.run()