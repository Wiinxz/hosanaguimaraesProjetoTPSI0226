# CRUD do stock 

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import get_connection,CATEGORIAS
from datetime import datetime

def summary():
    """_summary_
    """

def listar_tudo():
    with get_connection() as conn:
        return conn.execute(
            "SELECT id,nome,valor,categoria, stock, stock_minimo,data_registro FROM materiais ORDER BY id"
        ).fetchall()
    
def search_from_id (id:int):
    with get_connection() as conn:
        return conn.execute(
            "SELECT id,nome,valor,categoria,stock,stock_minimo,data_registro FROM materiais WHERE id = ?",(id,)
        ).fetchone()

def criar_material(nome,valor,categoria,stock,stock_minimo,user_id):
    
    #não esquecer, tenho que validar a sessão ativa aqui para obter o user_id já pre preenchido !!!!!
    data = datetime.now().strftime("%d-%m-%Y")
    with get_connection() as conn:
        conection = conn.execute(
            "INSERT INTO materiais (nome,valor,categoria,stock,stock_minimo,data_registro,user_id) VALUES (?,?,?,?,?,?,?)",(nome,valor,categoria,stock,stock_minimo,data,user_id)
        )
        conn.commit()
        return "Produto inserido com sucesso !"
    
def materials_update(nome,valor,categoria,stock,stock_minino,id):
    
    with get_connection() as conn:
        conn.execute(
            "UPDATE materiais SET nome=?, valor=?, categoria=?, stock=?, stock_minimo=? WHERE id=?",(nome,valor,categoria,stock,stock_minino,id)
        )

def remove_materials(id:int):
  
  with get_connection() as conn:
      conn.execute("DELETE FROM materiais WHERE id=?",(id,))
    
      return "Produto removido com sucesso !"

def search_linear_name(nome_search: str):
    
    resultado = []
    for n in listar_tudo():
        if nome_search.lower() in n[1].lower():
            resultado.append(n)
    
    return resultado

def search_by_category(categoria: str):
    
    with get_connection() as conn:
        return conn.execute(
            "SELECT id, nome, valor, categoria, stock, stock_minimo, data_registro FROM materiais WHERE categoria = ? ORDER BY nome",
            (categoria,)
        ).fetchall()

def search_linear_id(id:int):
    
    all = listar_tudo()
    esq,dir = 0,len(all) -1

    while esq <= dir:
        meio = (esq+dir) // 2
        
        if all[meio][0] == id:
            return all[meio]
        
        elif all[meio][0] < id:
            esq = meio + 1
        else: 
            id = meio - 1
    return None 