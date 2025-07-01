# 🏢 SmartSpace — Sistema de Gerenciamento de Salas de Reunião

Projeto acadêmico desenvolvido com o objetivo de aplicar conhecimentos em **Python, Django, HTML/CSS e banco de dados**, criando uma aplicação web funcional para **gestão de salas de reunião em uma empresa**.

---

## 🧠 Objetivo do Projeto

Desenvolver um sistema web que permita:

- Visualizar salas de reunião disponíveis
- Agendar horários de uso
- Consultar os próprios agendamentos
- Cancelar reservas com justificativa
- Exportar relatórios em CSV
- Controlar acesso por tipo de usuário (admin/equipe)

---

## 🔧 Funcionalidades

### 🗂️ 1. Visualização de Salas

- Página com listagem de salas disponíveis
- Exibição de detalhes e horários agendados

### 📅 2. Agendamento de Salas

- Formulário para agendar salas disponíveis
- Associação do agendamento ao usuário autenticado
- Prevenção de conflitos de horário

### 👤 3. Meus Agendamentos

- Listagem exclusiva dos agendamentos feitos pelo usuário logado
- Opções para editar ou excluir reservas futuras

### ❌ 4. Cancelamento de Reservas

- Cancelamento com justificativa obrigatória
- Registro dos cancelamentos para auditoria
- Página exclusiva com a listagem de agendamentos cancelados

### 📤 5. Exportação de Relatórios (CSV)

- Exportação dos dados de salas, usuários, agendamentos e cancelamentos
- Controle de acesso para equipe autorizada

---

## 🌐 Interface

- Interface web simples e funcional
- Desenvolvida com HTML5, CSS3 e Django Templates
- Responsividade básica com CSS puro

---

## ⚙️ Tecnologias Utilizadas

| Frontend         | Backend              | Banco de Dados | Outros              |
|------------------|----------------------|----------------|---------------------|
| HTML5 / CSS3     | Python 3.12          | SQLite         | Git + GitHub        |
| JavaScript       | Django 5.2.1         |                | Django Admin (CRUD) |

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/smartspace.git
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

---

## 👨‍💻 Desenvolvedor

**Guilherme Caixeta**  
