import os
import sys

sys.path.insert(0,os.path.dirname(__file__))

import database as db

#teste criação database

if __name__ == "__main__":
    db.criar_tabelas()
    print("Hello Word")







