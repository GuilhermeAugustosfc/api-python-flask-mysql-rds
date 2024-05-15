import mysql.connector


def conectar_banco():
    """
    Estabelece conexão com o banco de dados RDS MySQL.

    Retorna:
        Objeto de conexão ao banco de dados ou None em caso de erro.
    """
    try:
        config = {
            "host": "database-1.cpigwcyuk6vv.us-east-2.rds.amazonaws.com",
            "user": "admin",
            "password": "SO9yvDX5GwQfF1EWEM5u",
        }
        db_connection = mysql.connector.connect(**config)
        return db_connection
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados RDS MySQL: {err}")
        return None


def fechar_conexao(db_connection):
    """
    Fecha a conexão com o banco de dados.

    Args:
        db_connection: Objeto de conexão ao banco de dados.
    """
    if db_connection:
        db_connection.close()
