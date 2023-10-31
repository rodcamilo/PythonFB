#pip install mysql-connector-python
import mysql.connector
def conectar_bd():
    try:
        conexao=mysql.connector,connect(
            host=local_arquivo,
            user=nome_usuario,
            password=senha,
            database=nome_arquivo)
        return conexao
    except mysql.connector.Erro as err:
        print(f"Erro de conexão com o Banco de Dados: {err}")
        return None
def consultar_dados(conexao):
    if conexao:
        try:
            cursor=conexao.cursor()
            cursor.execute("SELECT * FROM tabela")
            resultados=cursor.fetchall()
            for resultado in resultados:
                print(resultado)
        except mysql.connector.Erro as err:
                print(f"Erro ao consultar dados: {err}")
        finally:
            cursor.close()
def inserir_dados(conexao):
