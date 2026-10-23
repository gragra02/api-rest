# 📚 API REST de Gestão de Matérias Escolares + Chatbot de Reservas

Este projeto consiste em uma **API REST** desenvolvida com **Django** e **Django REST Framework (DRF)** para o gerenciamento de matérias escolares (operações completas de CRUD), integrada a um **Frontend com Assistente Virtual (Chatbot)** para reserva de laboratório de informática.

Projeto desenvolvido como parte do desafio prático da disciplina de **Linguagem de Programação III** (Curso de Análise e Desenvolvimento de Sistemas - FMP).

---

## 🚀 Tecnologias Utilizadas

* **Back-end:** Python 3, Django, Django REST Framework (DRF)
* **Banco de Dados:** SQLite3 (padrão do Django)
* **Front-end:** HTML5, CSS3 e JavaScript (Fetch API para consumo em tempo real)

---

## ⚙️ Funcionalidades

### 1. API REST (`/api/materias/`)
Endpoints públicos (`AllowAny`) que permitem o gerenciamento completo das disciplinas escolares:
* **GET** `/api/materias/` — Lista todas as matérias cadastradas em formato JSON.
* **POST** `/api/materias/` — Cadastra uma nova matéria (`nome`, `professor`, `carga_horaria`).
* **PUT** `/api/materias/<id>/` — Atualiza os dados de uma matéria existente.
* **DELETE** `/api/materias/<id>/` — Remove uma matéria do banco de dados.

### 2. Chatbot de Reserva de Laboratório (`/reserva/`)
Interface interativa onde o assistente virtual da *TechNova* conversa com o usuário:
* Realiza uma requisição `GET` assíncrona (`fetch`) para buscar as matérias cadastradas na API em tempo real.
* Coleta o nome do professor, a matéria desejada, a data e o horário da aula.
* Gera um resumo para confirmação e emite o comprovante da reserva do laboratório.

---

## 🛠️ Como Executar o Projeto Localmente

1. **Clone o repositório (ou acesse a pasta do projeto):**
   ```bash
   git clone <url-do-seu-repositorio>
   cd escola_api
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install django djangorestframework
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

---

## 🔗 Endereços de Acesso (Endpoints)

Com o servidor rodando, acesse no navegador:
* **Interface DRF / API de Matérias:** [http://127.0.0.1:8000/api/materias/](http://127.0.0.1:8000/api/materias/)
* **Interface do Chatbot de Reservas:** [http://127.0.0.1:8000/reserva/](http://127.0.0.1:8000/reserva/)

---

## 👩‍💻 Autora

Desenvolvido por **Graziele da Silva**.