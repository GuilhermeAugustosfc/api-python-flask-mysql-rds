from flask import Flask, jsonify
from cliente_dao import buscar_todos_clientes

app = Flask(__name__)


@app.route("/clientes", methods=["GET"])
def obter_clientes():
    """
    Endpoint para obter todos os clientes do banco de dados.

    Retorna:
        Resposta JSON com os dados dos clientes ou mensagem de erro.
    """
    clientes = buscar_todos_clientes()
    if not clientes:
        return jsonify({"erro": "Falha ao buscar clientes no banco de dados."}), 500

    # Converter dados dos clientes em formato JSON
    lista_clientes_json = []
    for cliente in clientes:
        lista_clientes_json.append(
            {"id": cliente[0], "nome": cliente[1], "sobrenome": cliente[2]}
        )

    return jsonify({"clientes": lista_clientes_json}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
