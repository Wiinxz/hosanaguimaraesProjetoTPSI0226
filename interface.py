# crio aqui a interfaçe gira para exibir
import sys
import os

import authentic as auth

def menu_principal():

    print("\n╔══════════════════════════════════════════╗")
    print("║        MENU PRINCIPAL                    ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Listar todos os materiais            ║")
    print("║  2. Pesquisar material                   ║")
    print("║  3. Ordenar materiais                    ║")
    print("║  4. Estatísticas                         ║")
    print("║  5. Editar material                      ║")
    print("║                                          ║")
    print("║  ── Área de Administração ──             ║")
    print("║  6. Adicionar material   [admin only]    ║")
    print("║  7. Remover material     [admin only]    ║")
    print("║  0. Logout                               ║")
    print("╚══════════════════════════════════════════╝")
    return input("Opção: ").strip()

def menu_pesquisa():
    print("\n╔══════════════════════════════════════════╗")
    print("║        PESQUISA                          ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Por ID                               ║")
    print("║  2. Por Nome                             ║")
    print("║  3. Por categoria                        ║")
    print("║  4. VOLTAR                               ║")
    print("╚══════════════════════════════════════════╝")
    return input("Opção: ").strip()

def menu_ordenacao():
    print("\n╔══════════════════════════════════════════╗")
    print("║        ORDENAÇÃO                         ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. bUBBLE SORT                          ║")
    print("║  2. SELECTION SORT                       ║")
    print("║  3. SAIR                                 ║")
    print("╚══════════════════════════════════════════╝")
    return input("Opção: ").strip()

def menu_estatisticas():
    print("\n╔══════════════════════════════════════════╗")
    print("║        ESTATÍSTICAS                      ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. RESUMO ESTATISTICO?                  ║")
    print("║  2. MATERIAIS COM STOCK ABAIXO DO MÍNIMO ║")
    print("║  3. SAIR                                 ║")
    print("╚══════════════════════════════════════════╝")
    return input("Opção: ").strip()


