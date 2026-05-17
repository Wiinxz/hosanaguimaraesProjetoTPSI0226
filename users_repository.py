# Apenas cria e autentica um utilizador?
import os
import sqlite3
import database as data

from database import get_connection,DB_PATH

def summary():
    """
    def criar_utilizador recebe os valores passados e executa a criação na database. Retorna False caso o utilizador já esteja criado na database
    def autenticar recebe email e password e valida se corresponde ao que está na database executando uma query e retornando tru or false. Crio variável row para fazer o select no database apenas e uso fetchone para devolver 1 ou none 
    
    """

def criar_utilizador(email,password,data_integracao, role="user"):

    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO users (email, password, data_integracao,role) VALUES (?,?,?,?)",
                (email,password,data_integracao,role)
            )
            conn.commit()
            
            return True, "Utilizador criado com sucesso."
    except sqlite3.IntegrityError :
        return False, "Este email á está registrado no sistema."
    
def autenticar (email, password):

    with get_connection() as conn:
        
        row = conn.execute(
            "SELECT id, email, role FROM users WHERE email = ? AND password = ?",(email,password)
        ).fetchone()
    
    return row