# Apenas cria e autentica um utilizador?
import os
import sqlite3
import database as data

from database import get_connection,CATEGORIAS
"""DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),"dental_stock.db")

def get_connection():
    return sqlite3.connect(DB_PATH)"""

def summary():
    """_summary_
    """

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