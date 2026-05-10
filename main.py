import os
import sys

sys.path.insert(0,os.path.dirname(__file__))

import database as db

import validadores as validadores
import authentic as authentic


#teste criação database

if __name__ == "__main__":

    """print(validadores.validar_email("admin_clin@clinica.pt"))
    print(validadores.validar_password("Admin123!"))
    print(validadores.validar_data("00-00-0000"))
    print(validadores.validar_antiguidade("24-01-2026"))"""

    
    #print(db.autenticar("admin@clinica.pt","Admin123."))
    #print(db.criar_utilizador("admin@clinica.pt","Admin123.","01-01-2020"))
    #print(db.criar_utilizador("teste@testando.pt","Teste123!","03-05-2026"))

    #print("Teste criar conta ")
    #authentic.criar_conta()

    # print("Teste login")
    # authentic.login()

    #print(f"Teste sessão ativa: {authentic.sessao_ativa()}")
    #print(f"Teste admin: {authentic.is_admin()}")

    #Chamar apenas para logout
    #print(f"Teste logout:{authentic.logout()}")
    
    #print(f"Sessão ainda ativa? {authentic.sessao_ativa()}")

    #NÃO ESQUECER ! APENAS O ADMIN PODE DELETAR PRODUTOS LEMBRAR QUANDO CONSTRUIR O ' MAIN '
    #Talvez implementar adição e remoção de usuários? fazer validação para que o admin não possa se remover
    
    











