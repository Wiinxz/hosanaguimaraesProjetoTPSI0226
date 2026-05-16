# crio aqui a interfaçe gira para exibir
import sys
import os

import authentic as auth
import materials_repository as repo

def menu_principal():

    print("\n╔══════════════════════════════════════════╗")
    print("║        MENU PRINCIPAL                    ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Listar todos os materiais            ║")
    print("║  2. Pesquisar material                   ║")
    print("║  3. Ordenar materiais                    ║")
    print("║  4. Estatísticas                         ║")
    print("║  5. Editar material                      ║")
    print("║  0. Logout                               ║")
    print("║                                          ║")
    print("║  ── Área de Administração ──             ║")
    print("║  6. Adicionar material   [admin only]    ║")
    print("║  7. Remover material     [admin only]    ║")
    print("║  8. Criar Utilizador     [admin only]    ║")
    print("╚══════════════════════════════════════════╝")
    while True:
        op = input("Opção: ").strip()
        if op in ["0","1","2","3","4","5","6","7","8"]:
            return op
        print("[ERRO] Escolha uma opção válida.")

def menu_pesquisa():
    print("\n╔══════════════════════════════════════════╗")
    print("║        PESQUISA                          ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Por ID                               ║")
    print("║  2. Por Nome                             ║")
    print("║  3. Por categoria                        ║")
    print("║  4. VOLTAR                               ║")
    print("╚══════════════════════════════════════════╝")
    while True:
        op = input("Opção: ").strip()
        if op == "1": return op
        elif op == "2": return op
        elif op == "3": return op
        elif op == "4": return op
        else: print("[ERRO] Escolha uma opção entre 1 e 4.")

def menu_ordenacao():
    print("\n╔══════════════════════════════════════════╗")
    print("║        ORDENAR POR                       ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Stock                                ║")
    print("║  2. Data de registro                     ║")
    print("╚══════════════════════════════════════════╝")
    while True:
        op = input("Opção: ").strip()
        if op == "1": return "stock"
        elif op == "2": return "data"
        else: print("[ERRO] Escolha 1 ou 2.")

def menu_estatisticas():
    print("\n╔══════════════════════════════════════════╗")
    print("║        ESTATÍSTICAS                      ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. RESUMO ESTATISTICO?                  ║")
    print("║  2. MATERIAIS COM STOCK ABAIXO DO MÍNIMO ║")
    print("║  3. SAIR                                 ║")
    print("╚══════════════════════════════════════════╝")
    while True:
        op = input("Opção: ").strip()
        if op == "1": return op
        elif op == "2": return op
        elif op == "3": return op
        else: print("[ERRO] Escolha uma opção entre 1 e 3.")

def escolher_categoria():
    print("\n╔══════════════════════════════════════════╗")
    print("║        CATEGORIA                         ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Consumiveis                          ║")
    print("║  2. Dentisteria                          ║")
    print("║  3. Cirurgia                             ║")
    print("║  4. Endodontia                           ║")
    print("║  5. Prostodontia                         ║")
    print("╚══════════════════════════════════════════╝")
    while True:
        op = input("Opção: ").strip()
        if op == "1": return "Consumiveis"
        elif op == "2": return "Dentisteria"
        elif op == "3": return "Cirurgia"
        elif op == "4": return "Endodontia"
        elif op == "5": return "Prostodontia"
        else: print("[ERRO] Escolha uma opção entre 1 e 5.")

def menu_update():
    print("\n╔══════════════════════════════════════════╗")
    print("║        QUAL CAMPO DESEJA ALTERAR?        ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Nome                                 ║")
    print("║  2. Valor                                ║")
    print("║  3. Categoria                            ║")
    print("║  4. Stock                                ║")
    print("║  5. Stock mínimo                         ║")
    print("╚══════════════════════════════════════════╝")
    while True:
        op = input("Opção: ").strip()
        if op == "1": return "1"
        elif op == "2": return "2"
        elif op == "3": return "3"
        elif op == "4": return "4"
        elif op == "5": return "5"
        else: print("[ERRO] Escolha uma opção entre 1 e 5.")

# organização das minhas tabelas aqui 
def cabecalho_tabela():
    """Imprime o cabeçalho da tabela de materiais."""
    print(f"\n{'ID':<5} {'Nome':<40} {'Valor':>8} {'Categoria':<15} {'Stock':>6} {'Mín.':>5} {'Data Registro':>15}")
    print("─" * 105)

def linha_material(m):
    """
    Imprime uma linha da tabela com os dados de um material.
    Adiciona aviso ⚠ se o stock estiver abaixo do mínimo.

    Args:
        m (tuple): Tuplo com os dados do material.
    """
    alerta = "⚠️" if m[4] <= m[5] else ""
    print(f"{m[0]:<5} {m[1]:<40} {m[2]:>7.2f}€ {m[3]:<15} {m[4]:>5}{alerta} {m[5]:>5}{alerta} {m[6]:>15}")

def mostrar_lista(materiais, titulo="LISTA DE MATERIAIS"):
    """
    Apresenta uma lista de materiais em formato de tabela.

    Args:
        materiais (list): Lista de tuplos com dados dos materiais.
        titulo (str): Título a mostrar acima da tabela.
    """
    if not materiais:

        print("\n")
        return
    
    print(f"\n═{titulo} ═  ({len(materiais)} registo(s))")
    cabecalho_tabela()
    for m in materiais:
        linha_material(m)
    print("─" * 105)

    #criar validação de inputs seguros? ver depois