from flask import request
from flask_restful import Resource
import json
lista_habilidades = ['Python','Java','Flask','PHP']

# Exibe todos os itens e adiciona a lista de habilidades.
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    def post(self):
        pos = len(lista_habilidades)
        dados = json.loads(request.data)
        lista_habilidades.append(dados['habilidade'])
        return {'status': 'Sucesso', 'id': str(pos), 'habilidade': lista_habilidades[pos]}

# Altera, remove e exibe itens da lista de habilidades.
class Altera_Habilidades(Resource):
    # retorna a habilidade requisitada ou uma mensagem de erro
    def id_existe(self, id):
        try:
            habilidade = lista_habilidades[id]
        except IndexError:
            mensagem = 'Não há uma habilidade com o id especificado.'
        except Exception:
            mensagem = 'Erro Desconhecido.'
        try:
            response = {'status': 'Erro', 'mensagem': mensagem}
        except UnboundLocalError:
            response = {'status': 'Ok', 'mensagem': habilidade}
        return response


    msg_sus = {'Status': 'Sucesso', 'mensagem': ''}
    def get(self, id):
        response = self.id_existe(id)
        if response['status'] == 'Ok':
            response = {'id': str(id), 'habilidade': lista_habilidades[id]}
        return response
    def delete(self, id):
        response = self.id_existe(id)
        if response['status'] == 'Ok':
            lista_habilidades.pop(id)
            self.msg_sus['mensagem'] = 'Habilidade removida com sucesso.'
            response = self.msg_sus
        return response
    def put(self, id):
        response = self.id_existe(id)
        if response['status'] == 'Ok':
            dados = json.loads(request.data)
            lista_habilidades[id] = dados['habilidade']
            self.msg_sus['mensagem'] = 'Habilidade alterada com sucesso.'
            response = self.msg_sus
        return response





