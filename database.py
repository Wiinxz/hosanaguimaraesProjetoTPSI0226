import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),"dental_stock.db")

def summary ():
    """_summary_
     Este ficheiro utiliza sqlite3 que ve incluído em python.
     Utiliza biblioteca 'os' para construir o caminho do ficheiro
     Utiliza a classe datetime para poder trabalhar com datas

     DB_PATH utiliza o __file__ que é o caminho do própio ficheiro e o path.abspath para converter o caminh absoluto, path.dirmane pega na pasta para depois juntar com o ficheiro dental_stock.db.
     Assim o dental_stock.db é sempre criado na mesma parta que o database.py em qualquer pc.

     CATEGORIAS lista as 5 existentes no sistema, caso seja necessário criar uma nova é necessário mudar apenas aqui.

     def get_connection abre ligação com a base de dados.

     def criar_tabelas users e materiais. Cada material vai ter um user_id associado ao registro e data.
     Crio já por definição o login do admin.

     def criar_utilizador recebe os valores passados e executa a criação na database. Retorna False caso o utilizador já esteja criado na database

     def autenticar recebe email e password e valida se corresponde ao que está na database executando uma query e retornando tru or false  

    """

CATEGORIAS = ["Consumiveis","Dentisteria","Cirurgia","Endodontia","Prostodontia"]

def get_connection():
    return sqlite3.connect(DB_PATH)

def criar_tabelas():

    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                email           TEXT    UNIQUE NOT NULL,
                password        TEXT    NOT NULL,
                data_integracao TEXT    NOT NULL,
                role            TEXT    DEFAULT 'user'           
            )     
        """)
        connection.execute("""
           CREATE TABLE IF NOT EXISTS materiais(
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                nome          TEXT    NOT NULL,
                valor         REAL    NOT NULL,
                categoria     TEXT    NOT NULL,
                stock         INTEGER NOT NULL,
                stock_minimo  INTEGER NOT NULL,
                data_registro TEXT    NOT NULL,
                user_id       INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
                           )
                    """)
        connection.execute("""
            INSERT OR IGNORE INTO users (email,password,data_integracao,role)
            VALUES ('admin@clinica.pt','Admin123.','01-01-2020','admin')
        """)

def criar_utilizador(email,password,data_integracao, role="user"):

    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO users (email, password, data_integracao,role) VALUES (?,?,?,?)",
                (email,password,data_integracao,role)
            )
            
            return True, "Utilizador criado com sucesso."
    except sqlite3.IntegrityError :
        return False, "Este email á está registrado no sistema."
    
def autenticar (email, password):

    with get_connection() as conn:
        
        row = conn.execute(
            "SELECT id, email, role FROM users WHERE email = ? AND password = ?",(email,password)
        ).fetchone()
    
    return row    
    


        
