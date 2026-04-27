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

      def valida data -  recebe a data no formato DATE PATTERN e primeiro valida se esta vazio.
      Depois verifica se está no formato correto. Retorna True se estiver tudo ok.

      def validar_antiguidade - Utilizo o unpacking para separar os valores da tupla em variaveis individuais sendo "ok=False" e "msg=True".
      a variável integração converte a string para um obj datetime para fazer calculos com as datas.
      depois faco o calculo para obter a diferença de anos e depois meses, sendo que é necessário ter 3 meses completos na empresa.
      Verifico então se a já tem 3 meses de contrato para retornar True or False.

    """

EMAIL_PATTERN = r"^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9./-]+\.[a-zA-Z]{2,}$"

PASSWORD_PATTERN = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!?@#$%^&*()_+/-=])[a-zA-Z0-9!?@#$%^&*()_+/-=]{8,}$"

DATE_PATTERN = r"^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(\d{4})$"


def validar_email(email:str) -> tuple:
    
    if not email.strip():
        return False, "Obrigatório inserir um email !"
    if not re.match(EMAIL_PATTERN,email.strip()): #Lembrar que retorna na verdade None...Mas None é True
        return False,"Email ínvalido! utilize o formato esperado: user@user.com"
    return True,""


def validar_password(password:str) -> tuple:
    if not len(password)>= 8 :
        return False, "A password deve ter pelo menos 8 caracteres."
    if not re.search(r"[A-Z]",password):
        return False,"A password deve conter pelo menos 1 letra maiúscula"
    if not re.search(r"[a-z]",password):
        return False,"A password deve conter pelo menos 1 letra minúscula"
    if not re.search(r"\d",password):
        return False,"A password deve conter pelo menos 1 número"
    if not re.search(r"[!?@#$%^&*()_+/-=]",password):
        return False,"A password deve conter pelo menos 1 caractere especial entre estes ! ? @ # $ % ^ & * ( ) _ + \ - = "
    if not re.search(r"^[a-zA-Z0-9!?@#$%^&*()_+\-=]{8,}$",password):
        return False, "A password contém caracteres inválidos. Use apenas letras, números e os símbolos: ! ? @ # $ % ^ & * ( ) _ + - ="
    return True,""

def validar_data(data:str) -> tuple:
    if not re.match(DATE_PATTERN,data.strip()):
        return False, "Formato de data inválido. Use o formato DD-MM-AAAA !"
    
    try:
        datetime.strptime(data.strip(), "%d-%m-%Y")
    except ValueError:
        return False,"Data inválida ! Verifique o dia e o mês introduzidos"
    return True, ""


def validar_antiguidade(data_integracao: str) -> tuple:
    ok, msg = validar_data(data_integracao)
    if not ok:
        return False, msg
    
    integracao = datetime.strptime(data_integracao.strip(), "%d-%m-%Y")
    
    hoje = datetime.now()

    calcular_meses = (hoje.year - integracao.year) * 12 + (hoje.month - integracao.month)
    if hoje.day < integracao.day:
        calcular_meses -= 1
    if calcular_meses < 3 :
        return False, (f" São necessários pelo menos 3 meses na empresa para criar login. A data {data_integracao} tem apenas {calcular_meses} mês(es).")
    return True, ""                                   






    





