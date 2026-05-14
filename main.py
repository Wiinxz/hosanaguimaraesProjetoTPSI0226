import os
import sys

sys.path.insert(0,os.path.dirname(__file__))

import database as db
import validadores as validadores
import authentic as auth
import users_repository as users_repository
import materials_repository as repo
import interface as interface


def loop_inicial():
  
  while True:
    op = interface.menu_principal()

    match op:
            case "1":
                materials = repo.listar_tudo()
                interface.mostrar_lista(materials)
                
            case "2":
               pesquisa = pesquisar()
               interface.mostrar_lista(pesquisa)

            case "3":
                implementar_ordenar()
            case "4":
                implementar_estatisticas()
            case "5":
                implementar_editar()
            case "6":
                implementar_adicionar()
            case "7":
                implementar_remover()
            case "0":
                auth.logout()
                break
       #continuar  amanha os case 2 e os restantes 

def listar():
  
  materials = repo.listar_tudo()
  interface.mostrar_lista(materials)

def pesquisar():
  
  op = interface.menu_pesquisa()
  if op == "1":
        
        while True:
            try:
                idi = int(input("ID a pesquisar: "))
                break
            except ValueError:
                print("[!ERRO!] Introduza um número inteiro.")

        result = repo.search_from_id(idi)
        if result :
           interface.mostrar_lista([result], "Resultado por ID")       
        else:
           print(f"Matérial com o ID {idi} não encontrado") 

  if op == "2":
        
         nome = input("Nome a pesquisar: ")
         result = repo.search_linear_name(nome)
         
         if result :
           interface.mostrar_lista(result, "Resultado por Nome")       
         else:
           print(f"Matérial com o Nome {nome} não encontrado") 
   
  if op == "3":
        
         nome = input("Categoria a pesquisar: ")
         result = repo.search_by_category(nome)
         
         if result :
           interface.mostrar_lista(result, "Resultado por Categoria")       
         else:
           print(f"Matérial na Categoria {nome} não encontrado") 

if __name__ == "__main__":
 def testes():
  
    """print(validadores.validar_email("admin_clin@clinica.pt"))
    print(validadores.validar_password("Admin123!"))
    print(validadores.validar_data("00-00-0000"))
    print(validadores.validar_antiguidade("24-01-2026"))"""

    
    #print(db.autenticar("admin@clinica.pt","Admin123."))
    #print(db.criar_utilizador("admin@clinica.pt","Admin123.","01-01-2020"))
    #print(db.criar_utilizador("teste@testando.pt","Teste123!","03-05-2026"))

    #print("Teste criar conta ")
    #authentic.criar_conta()

    #print("Teste login")
    #authentic.login()
    
    #interface.menu_principal()
    #listando = repo.listar_tudo()
    #print(listando)

    #procura_id = int(input("insere um ID"))
    #print(repo.search_from_id(procura_id))

    #atualiza_material = int(input("insere um ID: "))
    #print(repo.search_from_id(atualiza_material))
    
    #print(repo.materials_update("Pasta Colgate", 1.98, "Consumiveis", 120, 50, 1))
    #repo.remove_materials(atualiza_material)

    #print(f"Teste sessão ativa: {authentic.sessao_ativa()}")
    #print(f"Teste admin: {authentic.is_admin()}")

    #Chamar apenas para logout
    #print(f"Teste logout:{authentic.logout()}")
    
    #print(f"Sessão ainda ativa? {authentic.sessao_ativa()}")
    
    #print("teste criar material ")
    #print(materials_repository.criar_material("Pasta Sensodyne","1.59","Consumiveis","100","50","1"))

    #NÃO ESQUECER ! APENAS O ADMIN PODE DELETAR PRODUTOS LEMBRAR QUANDO CONSTRUIR O ' MAIN '
    #Talvez implementar adição e remoção de usuários? fazer validação para que o admin não possa se remover
    
    #interface.menu_principal()
    #interface.menu_pesquisa()
    #interface.menu_ordenacao()
    #interface.menu_estatisticas()

db.criar_tabelas()

if auth.login():
  loop_inicial()

  










