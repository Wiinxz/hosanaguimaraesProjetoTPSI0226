# 🦷 Sistema de Gestão de Stock — Clínica Dentária

Aplicação de terminal desenvolvida em **Python** para gestão de materiais de uma clínica dentária, com autenticação por sessão, controlo de acessos por role, operações CRUD, algoritmos de ordenação e análise estatística de stock.

***

## 📋 Funcionalidades

### Utilizador comum (User)
- Listar todos os materiais registados
- Pesquisar materiais por **ID**, **Nome** ou **Categoria**
- Ordenar materiais por **quantidade em stock** (Selection Sort) ou por **data de registo** (Bubble Sort — crescente/decrescente)
- Ver **estatísticas** completas: total de registos, valor mínimo/médio/máximo, stock total e alertas de stock abaixo do mínimo
- Ver listagem de materiais com **stock abaixo do mínimo**
- **Editar** um material (por ID) — alterar nome, valor, categoria, stock ou stock mínimo
- **Logout** para terminar sessão

### Administrador (Admin)
Todas as funcionalidades do utilizador comum, mais:
- **Adicionar** novo material (nome, valor, categoria, stock inicial e stock mínimo)
- **Remover** material por ID, com confirmação da operação
- **Criar conta** de utilizador com validação de email, password e antiguidade mínima de 3 meses na clínica

***

## 🗂️ Estrutura do Projeto

```
hosanaguimaraesProjetoTPSI0226/
├── main.py                  # Ponto de entrada e fluxo principal
├── interface.py             # Menus e visualização no terminal
├── materials_repository.py  # CRUD, ordenação e estatísticas de materiais
├── users_repository.py      # Criação e autenticação de utilizadores
├── authentic.py             # Gestão de sessão (login, logout, roles)
├── validadores.py           # Validação com REGEX (email, password, data)
├── database.py              # Configuração e criação da base de dados
└── dental_stock.db          # Base de dados SQLite
```

***

## 🧩 Descrição dos Módulos

### `database.py`
Configura e inicializa a base de dados SQLite. O caminho é construído dinamicamente com `os.path` para garantir portabilidade entre sistemas e máquinas diferentes. Cria as tabelas `materiais` e `users` e insere o utilizador `admin` por defeito.

| Tabela | Campos principais |
|--------|-------------------|
| `materiais` | id, nome, valor, categoria, stock, stock_minimo, data_registro, user_id |
| `users` | id, email, password, data_integracao, role |

***

### `validadores.py`
Contém todas as validações com **expressões regulares (REGEX)**, construídas com apoio do site [regex101.com](https://regex101.com):

| Validador | Critérios |
|-----------|-----------|
| **Email** | Aceita caracteres especiais (`-.+`) antes do `@`; mínimo 2 letras após o último ponto |
| **Password** | Mínimo 8 caracteres; obrigatório: 1 maiúscula, 1 minúscula, 1 número, 1 carácter especial |
| **Data** | Formato `DD-MM-AAAA`; dia 01-31, mês 01-12, ano com 4 dígitos |
| **Antiguidade** | Mínimo 3 meses de contrato na clínica para criação de conta |

***

### `authentic.py`
Gere a sessão ativa através de um dicionário `session` com os campos `id`, `email` e `role`. Implementa login com validação de credenciais, criação de conta com loop de validação, verificação de role admin e logout.

***

### `users_repository.py`
Contém duas funções de acesso à base de dados:
- `criar_utilizador` — insere novo utilizador e devolve `True/False` com mensagem
- `autenticar` — valida email e password contra a base de dados com `fetchone()`

***

### `materials_repository.py`
Módulo principal com toda a lógica de materiais:

- **CRUD completo** — listar, criar, editar, remover
- **Pesquisa** — por ID (linear), por nome (linear com `lower()`), por categoria (query SQL)
- **Selection Sort** — ordena por stock de forma decrescente; identifica o maior elemento em cada passagem e efetua a troca apenas no final do ciclo interno
- **Bubble Sort** — ordena por data de registo de forma crescente; compara elementos adjacentes e troca-os quando necessário; usa `datetime.strptime()` para comparação correta de datas
- **Estatísticas** — total de registos, valor mínimo/médio/máximo, stock total e listagem de materiais com stock abaixo do mínimo

***

### `interface.py`
Responsável por toda a apresentação visual no terminal. Usa **f-strings com formatação de alinhamento** (`:<` para esquerda, `:>` para direita) para apresentar os dados em forma de tabela organizada. Inclui alerta visual (⚠️) sempre que o stock de um material estiver abaixo do mínimo definido.

***

### `main.py`
Ponto de entrada da aplicação. Inicializa as tabelas, autentica o utilizador e gere o fluxo principal com um `match/case` para cada opção do menu. As funcionalidades exclusivas do admin são verificadas com `auth.is_admin()` antes de serem executadas.

***

## 🔐 Controlo de Acessos

| Funcionalidade | User | Admin |
|----------------|:----:|:-----:|
| Listar materiais | ✅ | ✅ |
| Pesquisar materiais | ✅ | ✅ |
| Ordenar materiais | ✅ | ✅ |
| Ver estatísticas | ✅ | ✅ |
| Editar material | ✅ | ✅ |
| Adicionar material | ❌ | ✅ |
| Remover material | ❌ | ✅ |
| Criar utilizador | ❌ | ✅ |

***

## ⚙️ Algoritmos de Ordenação

| Algoritmo | Campo | Ordem base | Ficheiro |
|-----------|-------|-----------|----------|
| **Selection Sort** | Stock (quantidade) | Decrescente | `materials_repository.py` |
| **Bubble Sort** | Data de Registo | Crescente (`[::-1]` para inverter) | `materials_repository.py` |

***

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Utilização |
|------------|------------|
| Python 3 | Linguagem principal |
| SQLite3 (built-in) | Base de dados local sem servidor |
| `re` (REGEX) | Validação de email, password e data |
| `datetime` | Manipulação e comparação de datas |
| `os.path` | Caminho dinâmico para a base de dados |

***

## ▶️ Como executar

1. Clonar o repositório:
```bash
git clone https://github.com/hosana/hosanaguimaraesProjetoTPSI0226.git
cd hosanaguimaraesProjetoTPSI0226
```

2. Executar a aplicação:
```bash
python main.py
```

> Não são necessárias instalações adicionais. Todas as bibliotecas utilizadas são nativas do Python :)).

**Credenciais de admin por defeito:**
```
Email:    admin@clinica.pt
Password: Admin123!
```

***

## 👩‍💻 Autora

**Hosana Guimarães**
 Projeto UC-0620 — TPSI 2026
