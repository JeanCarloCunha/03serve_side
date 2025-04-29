import os #recupera dados do sistema operacional

# caminho relativo para a aplicação

basedir = os.path.abspath(os.path.dirname(__file__)) #vai buscar o endereço do config.py que você entrou e vai alimentar nessa variavel, independente onde tiver

class Config:
    # buscar um arquivo na estrutura de arquivos contendo a chave secreta
    # utilizamos o you-will-never-guess para ambiente de desenvolvimento
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # endereço do banco de dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # se quiser fazer log de todas as modificações
    SQLALCHEMY_TRACK_MODIFICATIONS = False
