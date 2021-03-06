from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, Altera_Habilidades
from habilidades import compara_habilidades  as Hb
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Rafael',
        'habilidades': ['Python', 'Flask']},
    {
        'id': '1',
        'nome': 'Galleani',
        'habilidades': ['python', 'Django']}
]

# Devolve um desenvolvedor pelo id também altera altera e deleta.
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'Erro','mensagem':'O item requisitado não existe.'}
        except Exception:
            response = {'status':'Erro','mensagem':'Erro desconhecido'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'Sucesso','mensagem':'Registro excluído'}


# Lista todos os desenvolvedores e permite registrar um novo.
class ListaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        hab = Hb(dados['habilidades'])
        if len(hab) == 0:
            posicao = len(desenvolvedores)
            dados['id'] = str(posicao)
            desenvolvedores.append(dados)
            response = desenvolvedores[posicao]
        else:
            mensagem = 'Uma ou mais habilidades não foram encontradas no sistema, verifique a ortografia ou adicione a(s) ao sistema.'
            response = {'status': 'Erro', 'mensagem': mensagem, 'Habilidades desconhecidas': hab}
        return response

    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Habilidades, '/habilidades')
api.add_resource(Altera_Habilidades,'/habilidades/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)