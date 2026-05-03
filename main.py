import os
import sys

sys.path.insert(0,os.path.dirname(__file__))

import database as db
import validadores as validadores

#teste criação database

if __name__ == "__main__":
    print(validadores.validar_email("admin_clin@clinica.pt"))
    print(validadores.validar_password("Admin123!"))
    print(validadores.validar_data("00-00-0000"))
    print(validadores.validar_antiguidade("24-01-2026"))







