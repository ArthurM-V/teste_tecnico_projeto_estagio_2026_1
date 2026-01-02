<img src="logo.png" alt="Mupi Systems Logo" width="200"/>

# Teste Técnico - Estágio Desenvolvedor Full Stack

---

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte do teste técnico para a vaga de Estágio Desenvolvedor Full Stack e consiste em uma plataforma fictícia voltada à construção de aplicações web.

## Objetivo do Projeto

- Implementar um painel simples de mensagens
- Trabalhar autenticação de usuário administrador
- Demonstrar organização de projeto Django
- Utilizar templates e estilização moderna

### Estrutura e páginas

O projeto é constituído por 3 páginas principais:

1. **Uma landing page pública** - Página inicial com informações sobre o serviço e um formulário de contato.
2. **Uma página de login** - Página que permite o acesso à área do administrador.
3. **Uma área administrativa** - Onde o administrador pode visualizar todas as mensagens recebidas.

### Fluxo de navegação

```
┌─────────────────────────────────────────────────────────────┐
│  VISITANTE                                                  │
│  ↓                                                          │
│  Acessa a landing page → Preenche formulário (nome, email,  │
│  mensagem) → Clica em "Enviar" → Mensagem salva no banco    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  ADMINISTRADOR                                              │
│  ↓                                                          │
│  Acessa /painel → Faz login (superusuário) → Visualiza      │
│  lista com todas as mensagens (nome, email, mensagem, data) │
└─────────────────────────────────────────────────────────────┘
```

#### Tecnologias Utilizadas

- **Django** - Para o back-end
- **Django Templates** - Renderização das páginas
- **TailwindCSS** - Estilização
- **Alpine.js** - Interatividade no front-end

### Passo a Passo para rodar a aplicação

#### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

#### 2️⃣ Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

#### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5️⃣ Crie um superusuário (para acessar a área admin)

```bash
python manage.py createsuperuser
```

#### 6️⃣ Execute o servidor

```bash
python manage.py runserver
```

#### 7️⃣ Acesse a aplicação

- **Landing page:** `http://localhost:8000`
- **Login:** `http://localhost:8000/login`
- **Painel Administrativo:** `http://localhost:8000/painel` (requer login)

---
