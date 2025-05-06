from app import create_app, db
from app.models import Client

# Cria a instância aplicativo
app = create_app()

@app.shell_context_processor
def make_shell_context():
    # pode executar comandos shell durante a execução
    # do app
    return { 'db': db, 'Client':Client }