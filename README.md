# Portfólio — Django

Site de portfólio em Django, tema roxo, para apresentar seu trabalho como
desenvolvedor e analista de dados. Já vem com seções de Sobre, Experiência,
Habilidades, Projetos e um formulário de Contato — tudo editável pelo painel
de administração do Django, sem precisar tocar no código.

## Como rodar localmente

```bash
# 1. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Crie as tabelas no banco de dados
python manage.py migrate

# 4. (Opcional, mas recomendado) crie um usuário admin
python manage.py createsuperuser

# 5. Popule o site com dados de exemplo (Prosegur, freelancer, projetos exemplo)
python manage.py seed_data

# 6. Rode o servidor
python manage.py runserver
```

Depois é só abrir http://127.0.0.1:8000/ no navegador.

## Receber as mensagens do formulário de contato no seu e-mail

Sem nenhuma configuração extra, toda mensagem enviada pelo formulário do site
fica salva em **/admin/ → Mensagens de contato**, mas nenhum e-mail é
disparado (em desenvolvimento, o conteúdo só aparece no terminal onde o
`runserver` está rodando). Para receber de verdade na sua caixa de entrada:

1. Copie o arquivo de exemplo:
   ```bash
   cp .env.example .env
   ```
2. Se você usa Gmail, gere uma "senha de app" em
   https://myaccount.google.com/apppasswords (precisa ter a verificação em
   duas etapas ativada na conta — é diferente da sua senha normal).
3. Abra o `.env` e preencha:
   ```env
   EMAIL_HOST_USER=seuemail@gmail.com
   EMAIL_HOST_PASSWORD=a-senha-de-app-gerada-no-passo-2
   CONTACT_EMAIL=seuemail@gmail.com
   ```
4. Reinicie o `python manage.py runserver`. A partir daí, toda mensagem
   enviada pelo formulário chega tanto no banco de dados quanto no e-mail
   definido em `CONTACT_EMAIL`.

Se você usa outro provedor de e-mail que não seja Gmail (Outlook, um e-mail
profissional, etc.), troque também `EMAIL_HOST` e `EMAIL_PORT` no `.env`
pelos dados SMTP do seu provedor.

## Como editar o conteúdo

### 1. Seus dados pessoais (nome, e-mail, links)
Abra `core/views.py` e edite o dicionário `OWNER` no topo do arquivo:

```python
OWNER = {
    "name": "Seu Nome",
    "role": "Desenvolvedor & Analista de Dados",
    "tagline": "...",
    "location": "Brasil",
    "email": "seuemail@exemplo.com",
    "github": "https://github.com/seu-usuario",
    "linkedin": "https://www.linkedin.com/in/seu-usuario",
}
```

### 2. Experiências, habilidades e projetos
Acesse **http://127.0.0.1:8000/admin/** com o usuário criado no passo de
`createsuperuser`. Lá você pode adicionar, editar ou remover:

- **Experiências** — empresa, cargo, datas e descrição (já vêm cadastradas
  "Autônomo" e "Prosegur" como exemplo — edite a descrição como quiser).
- **Habilidades** — nome, categoria (Linguagens, Dados & Automação,
  Ferramentas) e nível de 1 a 5.
- **Projetos** — título, descrição, imagem, tags, link do projeto e do
  repositório.
- **Mensagens de contato** — todas as mensagens enviadas pelo formulário do
  site ficam salvas aqui.

Os dados de exemplo criados pelo `seed_data` podem ser editados ou apagados
livremente pelo admin.

### 3. Cores do tema
Todas as cores estão centralizadas no topo do arquivo
`core/static/core/css/style.css`, dentro do bloco `:root`. Por exemplo, para
deixar o roxo mais escuro ou mais claro, basta trocar:

```css
--primary: #8b5cf6;       /* roxo principal usado em botões e destaques */
--primary-light: #c4b5fd; /* roxo claro usado em textos e links */
--bg: #120c1f;            /* fundo da página */
```

## Estrutura do projeto

```
portfolio/
├── manage.py
├── requirements.txt
├── portfolio/          # configurações do projeto Django
│   ├── settings.py
│   └── urls.py
└── core/                # app principal do site
    ├── models.py        # Skill, Experience, Project, ContactMessage
    ├── views.py          # lógica da página + dados do OWNER
    ├── forms.py           # formulário de contato
    ├── admin.py            # registro dos modelos no /admin/
    ├── management/commands/seed_data.py  # popula dados de exemplo
    ├── templates/core/   # base.html e home.html
    └── static/core/      # style.css e main.js
```

## Antes de colocar em produção

- Troque `SECRET_KEY` em `portfolio/settings.py` por um valor novo e secreto.
- Defina `DEBUG = False` e preencha `ALLOWED_HOSTS` com seu domínio.
- Rode `python manage.py collectstatic` para juntar os arquivos estáticos.
- Configure um servidor de banco de dados real (Postgres, por exemplo) se for
  além do SQLite padrão.
