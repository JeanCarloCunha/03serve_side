from flask import jsonify, request
from app import db
from app.models import Client
from app.routes import bp
from app.auth import token_required

@bp.route('/clients', methods=['GET'])
@token_required
def get_clients(current_user):
    # recupera uma id de cliente que pode ter sido passado por parâmetro
    client_id = request.args.get('client_id')

    # se existir uma id de cliente
    if client_id:
        try:
            client = Client.query.get_or_404(client_id)
            return jsonify(client.to_dict()), 200 # sucesso na requisição
        except Exception as e:
            return  jsonify({'erro': str(e)})

    else:
        # se não tem um id, manda todos os clientes
        try:
            clients = Client.query.all()
            return jsonify([client.to_dict() for get_client in clients]), 200 # sucesso na requisição
        except Exception as e:
            return jsonify({'erro': str(e)})
