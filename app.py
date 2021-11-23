from flask import Flask, jsonify, request
import json

app = Flask(__name__)
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
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'Erro','mensagem':'O item requisitado não existe.'}
        except Exception:
            response = {'status':'Erro','mensagem':'Erro desconhecido'}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso','mensagem':'Registro excluído'})

# Lista todos os desenvolvedores e permite registrar um novo.
@app.route('/dev', methods=['GET','POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)