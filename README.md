# Sistema de Gestão de Stock — Clínica Dentária

 Projeto desenvolvido em Python como um modelo básico para gestão de stock de uma clinica dentária com autenticação de sessão, CRUD, algoritimos de ordenação e análise estatística de stock.

 O projeto está dividido em 7 ficheiros e 1 Database, sendo essa a estrutura:
       

## Estrutura do Projeto 

```
hosanaguimaraesProjetoTPSI0226/
├── dental_stock.py
├── database.py
├── validadores.py
├── authentic.py
├── users_repository.py
├── materials_repository.py
├── interface.py
└── main.db
```

## Ficheiros


### `Main.py` - Ficheiro inicial! Ponto de entrada da aplicação. Inicializa a base de dados, executa o loop principal e chama todos os métodos implementados nos restantes módulos gerindo assim o fluxo de navegção do utilizador.

***

### `Interface.py` - Responsável pela apresentação visual da aplicação no terminal. 
Contém métodos para:
- Exibir os menus maiores de navegação formtados
- Apresentar a tabela de materiais de forma organizada e legível
- Exibe também alguns alertas visuais

***
   
### `Materials_repository.py` - Contém toda a lógica implementada no projeto para manipulação dos dados relativos aos materiais existentes na database. Implementa:
     
     - **Implementação do CRUD** - Create,Read(all),Update & Delete
     - **listagens** - Listagens totais e por categoria
     - **Pesquisa** - Pesquisa avançada por ID,Nome e Categoria
     - **Ordenação de listagens:**
       - Por **STOCK** utiliza o algoritimo [SELECTION SORT] e 
       - Por **DATA** utiliza o algoritimo [BUBBLE SORT] (crescente / decrescente)
     - **Estatísticas :**
        - Resumo estatístico com total de registros, valores dos produtos mínimos/médios/máximos, stock total
        - Identificação e listagem de máteriais com o stock abaixo do mínimo definido

***


### `Users_repository` - Contém toda a lógica implementada no projeto para manipulação dos dados relativos aos utilizadores

      - criação de novo utilizador na database
      - Autenticação de utilizador a database (verificação de email e password)

***


### `Authentic.py `- Gere a sessão ativa do utilizador. Contém métodos para:

    - **Login** - Validação de credenciais para inicio de sessão
    - **Criação de login** - Registro de novo utilizador com validação de dados
    - **Validação de sessão ativa** - confirma se existe um utilizador autenticado
    - **Verificação de admin** - restringe as funcionalidades apenas desa role 
    - **logout** - termina a sessão atual

***

 
### `Validadores.py` - Módulo de validação de dados utilizados no registro e login.
Todas as validações são implementadas com **espressões regulares (REGEX)**:
 
 - Validação de formato de **email**
 - Validação de **password** (mín: 8 caracteres, sendo 1 maiúscula, 1 minúscula, 1 número e pelo menos 1 caráctere especial predefinido por mim)
 - Vlidação de **data de integração** e antiguidade mínima de contato(3 meses)

***

### `dental_stock.db`
Base de dados SQLite com os dados persistentes da aplicação.

| Tabela | Descrição |
|--------|-----------|
| `materiais` | Registo de todos os materiais clínicos com stock, valor e categoria |
| `users` | Utilizadores com email, password e role (admin / user) |

***

## Tecnologias Utilizadas

| Tecnologia | Utilização |
|------------|------------|
| Python 3 | Linguagem principal |
| SQLite3 | Base de dados local |
| REGEX (`re`) | Validação de dados |
| `datetime` | Manipulação e comparação de datas |

***