import re
from datetime import datetime

def summary():

    """
    _summary_
      Importo regex e também datetime para trabalharmos com datas

      Utilizei regex101.com para criar as expressões EMAIL_PATTERN, PASSWORD_PATTERN E DATE_PATTERN

      * email - aceita a-z,A-Z, 0-9 e caracteres ._-+ apenas. Obrigatório @ e depois do . pelo menos 2 letras. 
      * password - mínimo 1 maiscula e minuscula, 1 digito e qualquer um desses caracteres !?@#$%^&*()_+\-= 
      * data valida - DD-MM-AAAA 

      def validar_email - recebe o email em string e transforma em tupla, retira espaços vazios e valida 1º se esta vazio e retorna true or false,
      depois verifica se segue o formato EMAIL_PATTERN e retorna true or False. Caso esteja tudo ok retorna apenas True""

      def valida_password - recebe a password em string e transforma em tupla. Não aceita espaços vazios.
      1ª verifica se o tamanho é menor que 8, depois verifica se existe 1 caractere maiúsculo, 1 minúsculo 1 número e 1 caractere especial dentre os selecionados.
      Retorna True or False de acordo com o input recebido




    """

EMAIL_PATTERN = r"^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"

PASSWORD_PATTERN = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.[!?@#$%^&*()_+\-=]).{8,}$"

DATE_PATTERN = r"^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(\d{4})$"


def validar_email(email:str) -> tuple:
    
    if not email.strip():
        return False, "Obrigatório inserir um email !"
    if not re.match(EMAIL_PATTERN,email.strip()): #Lembrar que retorna na verdade None...Mas None é True
        return False,"Email ínvalido! utilize o formato esperado: user@user.com"
    return True,""


def validar_password(password:str) -> tuple:
    if not len(password)< 8:
        return False, "A password deve ter pelo menos 8 caracteres."
    if not re.search(r"[A-Z]",password):
        return False,"A password deve conter pelo menos 1 letra maiúscula"
    if not re.search(r"[a-z]",password):
        return False,"A password deve conter pelo menos 1 letra minúscula"
    if not re.search(r"\d",password):
        return False,"A password deve conter pelo menos 1 número"
    if not re.search(r"[!?@#$%^&*()_+\-=]",password):
        return False,"A password deve conter pelo menos 1 caractere especial entre estes ! ? @ # $ % ^ & * ( ) _ + \ - = "
    return True,""



##### Continuar validacoes 

# criar def de validar data e validar_antiguidade. Testar no fim com prints no main 





