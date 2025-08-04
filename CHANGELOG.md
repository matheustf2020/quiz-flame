📌 Versão 2.0 — Quiz Flame Sertão
Data de lançamento: 04/08/2025
Responsável: [Matheus - TrindaDev]

✅ Funcionalidades novas
🔐 Sistema de login com autenticação (User)

🎮 Pontuação associada ao usuário logado

🔁 Bloqueio de nova tentativa por 1h após o jogo

📈 Ranking geral atualizado dinamicamente

🧮 Sistema de níveis com base na pontuação total

👤 Painel do Jogador com dados personalizados:

Pontuação total

Última pontuação

Quantidade de quizzes feitos

Nível atual

Bio do usuário

🎨 Melhorias visuais
Interface 100% reformulada com Bootstrap 5

Cards, botões e blocos estilizados com:

Sombreamento

Arredondamento de bordas (rounded-4)

Paleta harmônica com azul e verde

Adição de área transparente azul para destacar textos

Imagens otimizadas com img-fluid e posicionamento centralizado

Tela inicial com explicação do quiz + botão destacado

Mensagens Django centralizadas com fundo e cor por tipo (alert-success, alert-danger, etc.)

Tabelas estilizadas para ranking e responsividade geral

📱 Responsividade
Uso intensivo da grid Bootstrap (col-12, col-md-6, etc.)

Remoção de width: 1000px fixos e substituição por max-width com w-100

Ajustes de espaçamento com classes (p-3, mt-4, etc.)

Layouts flexíveis com d-flex e gap-2 para melhor visualização em dispositivos móveis

🔧 Refatorações e melhorias técnicas
Views atualizadas para uso de request.user e @login_required

Separação lógica entre resultado_view, nome_view, e painel

models.py com campos adicionais no modelo Usuario (pontuação_total, nível, quizzes, bio, etc.)

Otimização de sessões (request.session['pontuacao'])

Redução de divs aninhadas excessivamente

Melhor uso de static para imagens e estilos

📌 Próximos passos (previstos para v2.1 ou v3.0)
📋 Página de cadastro personalizada

🏷️ Sistema de níveis com nomes (Ex: Discípulo, Servo, Apóstolo)

✨ Personalização de Avatar do usuário

🔧 Admin simplificado para perguntas, usuários e ranking

🧎 Painel de pedidos de oração (integrar com sessão)