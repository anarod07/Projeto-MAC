from flask import Flask, request, jsonify
from database import init_db
from repository import DiscoRepository

app = Flask(_name_)

# Instanciando o repositório
discoRepository = DiscoRepository()

@app.route('/discos', methods=['GET'])
def listar_discos():
    discos = discoRepository.listar_todos_discos()
    return jsonify([disco.toJson() for disco in discos])

@app.route('/disco/<int:disco_id>', methods=['GET'])
def obter_disco(disco_id):
    disco = discoRepository.obter_disco_por_id(disco_id)
    if disco:
        return jsonify({'id': disco.id, 'titulo': disco.titulo, 'artista': disco.artista, 'preco': disco.preco, 'disponivel': disco.disponivel})
    return jsonify({'erro': 'Disco não encontrado'}), 404

@app.route('/disco', methods=['POST'])
def criar_disco():
    titulo = request.json.get('titulo')
    artista = request.json.get('artista')
    preco = request.json.get('preco')
    disponivel = request.json.get('disponivel', True)
    novo_disco = discoRepository.criar_disco(titulo, artista, preco, disponivel)
    return jsonify({'id': novo_disco.id, 'titulo': novo_disco.titulo, 'artista': novo_disco.artista, 'preco': novo_disco.preco, 'disponivel': novo_disco.disponivel}), 201

@app.route('/disco/<int:disco_id>', methods=['PUT'])
def atualizar_disco(disco_id):
    data = request.get_json()
    titulo = data.get('titulo')
    artista = data.get('artista')
    preco = data.get('preco')
    disponivel = data.get('disponivel')
    disco_atualizado = discoRepository.atualizar_disco(disco_id, titulo, artista, preco, disponivel)
    if disco_atualizado:
        return jsonify({'id': disco_atualizado.id, 'titulo': disco_atualizado.titulo, 'artista': disco_atualizado.artista, 'preco': disco_atualizado.preco, 'disponivel': disco_atualizado.disponivel})
    return jsonify({'erro': 'Disco não encontrado'}), 404

@app.route('/disco/<int:disco_id>', methods=['DELETE'])
def deletar_disco(disco_id):
    disco_deletado = discoRepository.deletar_disco(disco_id)
    if disco_deletado:
        return jsonify({'mensagem': 'Disco deletado com sucesso'})
    return jsonify({'erro': 'Disco não encontrado'}), 404

@app.route('/disco/<int:disco_id>/vender', methods=['POST'])
def vender_disco(disco_id):
    disco = discoRepository.obter_disco_por_id(disco_id)
    if disco and disco.disponivel:
        discoRepository.marcar_como_vendido(disco_id)
        return jsonify({'mensagem': f'Disco "{disco.titulo}" vendido com sucesso'})
    return jsonify({'erro': 'Disco não disponível para venda'}), 400

@app.route('/disco/<int:disco_id>/alugar', methods=['POST'])
def alugar_disco(disco_id):
    disco = discoRepository.obter_disco_por_id(disco_id)
    if disco and disco.disponivel:
        discoRepository.marcar_como_alugado(disco_id)
        return jsonify({'mensagem': f'Disco "{disco.titulo}" alugado com sucesso'})
    return jsonify({'erro': 'Disco não disponível para aluguel'}), 400

if _name_ == "_main_":
    init_db(app)
    app.run(debug=True)
