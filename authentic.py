import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from validadores import validar_email, validar_password, validar_antiguidade
from database import criar_utilizador, autenticar

def summary ():
    """
    Primeiro crio um dicioário para guardar email e role do utilizador atual.

    def sessao_ativa que retorna o email se nao for null.

    def is_admin que valida se o role é do admin.

    def logout altera o estado do email e da role para none (reseta) para terminar a sessão.

    def login imprime a janela aonde tem um input que pede o email e transforma em strip, utilizo o unpacking novamente para separar os valores da tupla em variaveis individuais sendo "ok=False" e "msg=True".
    depois pede password e pega os 2 dados e coloca na variavel utlizador que chama o método autenticar passando emaile pass, se true depois passa os valores para o dicionario session mostra mensagem de bem vindo e retorna True, 
    se nao retorna False e menssagem de erro.

    def criar_conta recebe um input email e transforma em strip e depois pede password (input) e valida novamente, depois pede a data de integração para ver se já esta há pelo menos 3 meses na clinica.
    utilizo o unpacking novamente para separar os valores da tupla em variaveis individuais sendo "resposta=False" e "sucess=True" chamo a def criar_utilizador para inserir depois na DB.
    """

# funções da minha sessão
session = {"email": None, "role": None}

def sessao_ativa():
    return session["email"] is not None

def is_admin():
    return session ["role"] == "admin"

def logout ():
    session["email"] = None
    session["role"] = None
    print("--- Sessão terminada com sucesso! ---")

def login ():
    
    print("\n------ LOGIN ------")

    email = input("Email: ").strip()
    ok, msg = validar_email(email)
    if not ok:
        print(f"ERRO ! :{msg}")
        return False
    
    password = input("Password: ").strip()

    utilizador = autenticar(email,password)
    
    if utilizador:
        
        session["email"] = utilizador[1]
        session["role"] = utilizador[2]
        print(f" Bem-vindo(a), {session['email']} ")
        return True
    else:
        print("ERRO ! Email ou password incorretos, tente novamente! ")
        return False

def criar_conta():

    print("\n-------- CRIAR CONTA --------")
    print("[IMPORTANTE] : Para criar um login são necessários pelo menos 3 meses de contrato\n")

    email = input("Email: ").strip()
    ok,msg = validar_email(email)
   
    if not ok:
        print(f"ERRO ! {msg}")
        return
    
    print("[PASSWORD] : não esqueca que tem que conter mín.8 caracteres. 1 maiúscula, 1 minúscula, 1 número e 1 caractere ! ? @ # $ % ^ & * ( ) _ + \ - = ")
    password = input("Password: ").strip()
    ok,msg = validar_password(password)
    if not ok:
        print(f"ERRO ! {msg}")
        return
    
    password_confirmation = input("Digite novamente a password para confirmar: ").strip()
    if password != password_confirmation:
        print("ERRO ! As passwords não coincidem !")
    
    data= input("Data de integração (DD - MM - AAAA) : ").strip()
    ok,msg = validar_antiguidade(data)
    if not ok:
        print(f"ERRO ! {msg}")
        return
    
    sucess,resposta = criar_utilizador(email, password, data)
    if sucess:
        print(f"\n[--LOGIN ACEITE--] {resposta} ")
    else:
        print(f"[ERRO] {resposta}")

    


        