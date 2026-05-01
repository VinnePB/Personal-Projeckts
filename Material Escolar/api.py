from flask import Flask, request, jsonify

app = Flask(__name__)

filmes = ['Gente Grande','Interestelar','Madagascar']

@app.route('/filmes', methods=['GET'] )
def list_filmes():
    return jsonify(filmes)

@app.route('/filmes', methods=['POST'])
def cadastrar_filme():
    data = request.get_data().decode('utf-8').to_json()
    filme = data['filme']
    print(filme)
    filmes.append(filme)
    #filmes.append(filme)

    if not filme:
        return jsonify('Nome do filme é obrigatório'), 400
    
    if filme in filmes:
         return jsonify('Filme já cadastrdo'),400

    filmes.append(filme)
    return jsonify('filme cadastrado')


if __name__=='__main__':
    app.run(host= '0.0.0.0', debug=True)
