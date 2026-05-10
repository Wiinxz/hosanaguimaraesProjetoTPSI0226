import os
import sys

sys.path.insert(0,os.path.dirname(__file__))

import database as db

import validadores as validadores
import authentic as authentic
import users_repository as users_repository
import materials_repository as materials_repository
import interface as interface


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

    print("Teste login")
    authentic.login()
    
    interface.menu_principal()
    #print(f"Teste sessão ativa: {authentic.sessao_ativa()}")
    #print(f"Teste admin: {authentic.is_admin()}")

    #Chamar apenas para logout
    #print(f"Teste logout:{authentic.logout()}")
    
    #print(f"Sessão ainda ativa? {authentic.sessao_ativa()}")
    
    #print("teste criar material ")
    #print(materials_repository.criar_material("Pasta Sensodyne","1.59","Consumiveis","100","50","1"))

    #NÃO ESQUECER ! APENAS O ADMIN PODE DELETAR PRODUTOS LEMBRAR QUANDO CONSTRUIR O ' MAIN '
    #Talvez implementar adição e remoção de usuários? fazer validação para que o admin não possa se remover
    
    











