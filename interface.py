# crio aqui a interfaçe gira para exibir
import sys
import os

import authentic as authentic

def menu_principal():
    print("\n╔══════════════════════════════════════════╗")
    print("║        MENU PRINCIPAL                    ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Listar todos os materiais            ║")
    print("║  2. Pesquisar material                   ║")
    print("║  3. Ordenar materiais                    ║")
    print("║  4. Estatísticas e filtros               ║")
    print("║  5. Editar material                      ║")
    print("║                                          ║")
    print("║  ── Área de Administração ──             ║")
    print("║  6. Adicionar material   [admin only]    ║")
    print("║  7. Remover material     [admin only]    ║")
    print("║  0. Logout                               ║")
    print("╚══════════════════════════════════════════╝")
    return input("Opção: ").strip()