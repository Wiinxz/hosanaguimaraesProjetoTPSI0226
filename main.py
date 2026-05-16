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
               pesquisar()

            case "3":
                ordenar()
                #trocar o ordenar por categoria para ordenar por data... está redundante
            case "4":
                 estatisticas()

            case "5":
                editar() #Criar o editar

            case "6":
             if auth.is_admin():
               criar()
             else:
                print("[ERRO] Acesso negado. Apenas administradores.")              

            case "7":
              if auth.is_admin():
                remove()
              else:
                print("[ERRO] Acesso negado. Apenas administradores.") 
            
            case "8":
               if auth.is_admin():
                   auth.criar_conta()

            case "0":
                auth.logout()
                break

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

def ordenar():
    ordem = interface.menu_ordenacao()

    if ordem == "stock":
        stock = repo.bubble_sort_ord_by_name(repo.listar_tudo(),"stock")
        interface.mostrar_lista(stock,"ORDENADO POR STOCK")

    if ordem == "data":

        print("═════ TIPO DE ORDENAÇÃO ═════")
        print(" [ 1 ] - Decrescente [mais novo - mais antigo] ")
        print(" [ 2 ] - Crescente   [mais antigo - mais novo]")
        
        while True:
            opc = input("\nEscolha a opção desejada: ").strip()
            if opc in ["1","2"]:
                break
        
        
        result = repo.selection_sort_ord_by_stock(repo.listar_tudo(),"data_registro")
        interface.mostrar_lista(result,"ORDENADO POR DATA")

    if opc == 2:
        result = result[::-1] # uso para inverter a lista

def estatisticas():
    
    estatisticas = interface.menu_estatisticas()

    if estatisticas == "1":
        
        stats = repo.statistics()
        if not stats:
            print("[INFO] Sem dados para calcular.")
            return
        
        print("\n═════ RESUMO ESTATÍSTICO ═════")
        print(f"  Total de registos : {stats['total']}")
        print(f"  Valor médio       : {stats['valor_medio']:.2f}€")
        print(f"  Valor máximo      : {stats['valor_max']:.2f}€")
        print(f"  Valor mínimo      : {stats['valor_min']:.2f}€")
        print(f"  Stock total       : {stats['stock_total']} unidades")
        print(f"  Abaixo do mínimo  : {len(stats['abaixo_minimo'])} material(is) ")

    elif estatisticas == "2":
        
        stats = repo.statistics()
        if not stats:
            print("[INFO] Sem dados.")
            return
        interface.mostrar_lista(stats["abaixo_minimo"], "STOCK ABAIXO DO MÍNIMO !")
    
    else:
        return

def editar():
   
   while True:
            try:
                id = int(input("ID do Material :"))
                break
            except ValueError:
                print("[!ERRO!] Introduza um número inteiro.")

   r = repo.search_from_id(id)
   if r :
      interface.mostrar_lista([r], "Resultado por ID")       
   else:
      print(f"Matérial com o ID {id} não encontrado") 

   update = interface.menu_update()
   
   nome, valor, categoria, stock, stock_min = r[1], r[2], r[3], r[4], r[5]

   match update:
        case "1":
            nome = input(f"Novo nome [{r[1]}]: ").strip() or r[1]
        case "2":
            valor = input(f"Novo valor [{r[2]}]: ") or r[2]
        case "3":
            categoria = interface.escolher_categoria()
        case "4":
            stock = int(input(f"Novo stock [{r[4]}]: ") or r[4])
        case "5":
            stock_min = int(input(f"Novo stock mín. [{r[5]}]: ") or r[5])

    
   repo.materials_update(nome, valor, categoria, stock, stock_min, id)
   print(f"[OK] Material actualizado com sucesso!")

def criar():

   print("\n═════ ADICIONAR MATERIAL ═════")

   while True: # para o nome
       nome = input("Insira o nome do Material : ").strip()
       if nome:
           break
       print("[ERRO] O nome não pode estar vazio.")

   while True: # para o valor
       try:
           valor = float(input("Insira o valor [FORMATO: 0.00] : "))
           if valor > 0:
               break
           print("[ERRO] O valor tem de ser positivo.")
       except ValueError:
           print("[ERRO] Insere um número válido. Ex: 1.99")

   categoria = interface.escolher_categoria()

   while True: # para o stock inicial
       try:
           stock = int(input("Insira a quantidade inicial do matérial : "))
           if stock >= 0 :
               break
           print("[ERRO] ATENÇÃO ! Stock não pode ser negativo.")
       except ValueError:
            print("[ERRO] Apenas válido números inteiros.")

   while True:
      try:
          stock_min = int(input("Insira o stock mínimo necessário para este matérial: "))
          if stock_min >= 0:
              break
          print("[ERRO] ATENÇÃO ! Stock mínimo não pode ser negativo.")
      except ValueError:
        print("[ERRO] Apenas válido números inteiros.")
          
   user_id = auth.session["id"]

   repo.criar_material(nome,valor,categoria,stock,stock_min,user_id)

   print("[OK] Material adicionado com sucesso!")

def remove():

    print("\n═════ REMOVER MATERIAL ═════")

    id = int(input("Insira o ID do máterial a remover: "))

    remove = repo.search_from_id(id)
    interface.mostrar_lista([remove])

    if not remove:
        print(f"[ERRO] Material com ID {id} não encontrado.")
        return
    
    confirmar = input("Tem certeza que deseja remover este máterial ? (s/n): ").strip().lower()

    if confirmar == "s":
        repo.remove_materials(id)
        print("[OK] Material removido com sucesso!")
    else:
        print("[INFO] Operação cancelada.")


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

  










