# 📖 Quiz Flame

Um sistema de Quiz Bíblico desenvolvido com Django, com foco em praticar fundamentos do desenvolvimento backend, organização em MVC, banco de dados relacional e deploy em ambiente Linux.

## 🚀 Funcionalidades

- Sistema de perguntas e respostas com pontuação
- CRUD completo de perguntas no Django Admin
- Sistema de ranking de usuários (em desenvolvimento)
- Possibilidade de resetar perguntas e IDs
- Integração com templates para exibir perguntas ao usuário
- Deploy funcional em VPS com domínio: [trindadev.ddns.net](http://trindadev.ddns.net)

## ⚙️ Tecnologias utilizadas

- Python 3
- Django
- SQLite (banco de dados padrão)
- HTML (Templates Django)
- Git e GitHub
- Linux (Ubuntu Server)
- Gunicorn + Nginx (Deploy)
- Certbot (SSL gratuito)


## 🧱 Organização do Projeto
quiz-flame/
├── core/ # App principal (views, models, urls)
├── templates/ # Templates HTML
├── static/ # Arquivos estáticos (CSS, imagens, etc.)
├── db.sqlite3 # Banco de dados
├── manage.py
└── requirements.txt

## 🛠️ Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/matheustf2020/quiz-flame.git
cd quiz-flame
