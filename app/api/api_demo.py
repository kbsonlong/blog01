from flask import Blueprint

api = Blueprint('api',__name__,url_prefix='/api')


@api.route('/register')
def reg():
    return 'register'