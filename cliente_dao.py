import db_conection


def buscar_todos_clientes():
    """
    Busca todos os clientes do banco de dados.

    Retorna:
        Lista de clientes (tuplas com ID, nome e sobrenome) ou None em caso de erro.
    """
    db = db_conection.conectar_banco()
    if not db:
        return None

    cursor = db.cursor()
    cursor.execute("USE teste")
    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()
    cursor.close()
    db_conection.fechar_conexao(db)

    return resultados
