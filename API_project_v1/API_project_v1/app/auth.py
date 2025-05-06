#pip install pyjwt

import datetime
import jwt

from functools import wraps
from flask import request, jsonify, Blueprint, current_app

# toda a parte de encapsulamento da API, vai ser de responsabildiade do
# Blueprints
auth_bp = Blueprint('auth', __name__)

#cria as rotas de autenticação
@auth_bp.route('login',methods=['POST'])
def login():
    #recuperar o payload em json
    auth_data = request.get_json()
    # recuperar o dados do payload
    username = auth_data.get('username')
    password = auth_data.get('password')

    if username == 'admin' and password == 'password':
        token = jwt.encode({
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        },
        current_app.config["SECRET_KEY"],
        algorithm='HS256'
        )
        return jsonify({'token': token }), 200 # sucesso na requisição
    return jsonify({'messsage': 'Invalid username/passaword'}), 401 #erro de autenticação

# criar marcação de rotas com funções
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        #inicializar um token como nulo
        token = None

        if 'x-access-token' in request.headers
            token = request.headers['x-access-token']
        if not token:
            return jsonify({ 'message': 'Token is missing'}), 401


        # se tem token, tenta decodificar
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms='HS256')
            current_user = data['user']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token is expired'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token is invalid'}), 401

        return  f(current_user, *args, **kwargs)
    return decorated()
