from flask import Blueprint

api = Blueprint('api',__name__)


@api.route('/api/register')
def reg():
    return 'register'