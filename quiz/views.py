from django.shortcuts import render, redirect, get_object_or_404
from .models import Pergunta, Alternativa
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Usuario as User
from django.contrib.auth.decorators import user_passes_test



def bem_vindo(request):
    if request.method == "GET":
        return render(request, 'index.html')
    
@login_required(login_url='logar')
def pergunta_view(request, numero):
    # Bloqueio baseado no horário do último jogo
    ultimo_jogo_str = request.session.get('ultimo_jogo')

    if ultimo_jogo_str:
        ultimo_jogo = datetime.fromisoformat(ultimo_jogo_str)
        agora = datetime.now()
        if agora < ultimo_jogo + timedelta(hours=1):
            tempo_restante = (ultimo_jogo + timedelta(hours=1)) - agora
            minutos = int(tempo_restante.total_seconds() // 60)
            return render(request, 'bloqueado.html', {'minutos': minutos})

    # (segue com o restante da view normalmente)
    pergunta = get_object_or_404(Pergunta, id=numero)

    if numero == 1:
        request.session['pontuacao'] = 0

    if request.method == "POST":
        resposta_id = request.POST.get('resposta')

        if not resposta_id:
            alternativas = pergunta.alternativa_set.all()
            return render(request, 'pergunta.html', {
                'pergunta': pergunta,
                'alternativas': alternativas,
                'erro': 'Você precisa escolher uma alternativa.',
                'pontuacao': request.session.get('pontuacao', 0)
            })

        alternativa_escolhida = Alternativa.objects.get(id=resposta_id)
        acertou = alternativa_escolhida.correta

        if acertou:
            request.session['pontuacao'] += 10

        # Se for a última pergunta:
        TOTAL_PERGUNTAS = 5
        if numero >= TOTAL_PERGUNTAS:
            return redirect('resultado')

        # Senão, vai para a próxima pergunta
        proxima = numero + 1
        return redirect('pergunta', numero=proxima)

    # GET
    alternativas = pergunta.alternativa_set.all()
    return render(request, 'pergunta.html', {
        'pergunta': pergunta,
        'alternativas': alternativas,
        'pontuacao': request.session.get('pontuacao', 0)
    })


def calcular_nivel(pontuacao):
    # Define as faixas de pontuação para cada nível
    if pontuacao < 50:
        return 1
    elif pontuacao < 150:
        return 2
    elif pontuacao < 300:
        return 3
    elif pontuacao < 500:
        return 4
    else:
        return 5
@login_required(login_url='logar')
def resultado_view(request):
    # Recupera a pontuação da sessão (calculada no quiz)
    pontuacao = request.session.get('pontuacao', 0)

    # Atualiza os dados do usuário logado
    user = request.user
    user.pontuacao_total += pontuacao
    user.ultima_pontuacao = pontuacao
    user.quantidade_quizzes += 1

    # Define o nível com base na nova pontuação total
    user.nivel_atual = calcular_nivel(user.pontuacao_total)
    
    user.save()

    # Marca a hora do último jogo (usado para cooldown)
    request.session['ultimo_jogo'] = datetime.now().isoformat()

    # Limpa a pontuação da sessão para não reaproveitar
    if 'pontuacao' in request.session:
        del request.session['pontuacao']

    # Gera o ranking dos top 5 com maior pontuação total
    ranking = User.objects.order_by('-pontuacao_total')[:5]

    return render(request, 'resultado.html', {
        'pontuacao': pontuacao,
        'ranking': ranking
    })



def resetar_perguntas(request):
    # Apaga todas as perguntas
    Pergunta.objects.all().delete()

    # Reseta o ID (autoincremento)
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='quiz_pergunta';")

    # Redireciona para a página de manutenção (altere conforme necessário)
    return redirect('manutencao')

@user_passes_test(lambda u: u.is_superuser, login_url='logar')
def manutencao(request):
    return render(request, 'manutencao.html')


def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = authenticate(username=nome, password=senha)
        if not usuario:
            messages.error(request, 'Usuario não existe')
            return redirect('logar')
        else:
            messages.success(request, 'Usuario logado')
            login(request, usuario)
            return redirect('bem_vindo')
        
@login_required(login_url='logar')
def painel_usuario(request):
    usuario = request.user  # Já é do tipo Usuario (AbstractUser)
    ranking = User.objects.order_by('-pontuacao_total')[:5]


    return render(request, 'painel.html', {
        'usuario': usuario,
        'ranking': ranking
    })

def sair(request):
    messages.success(request, 'Você saiu do sistema')
    logout(request)
    return redirect('bem_vindo')

def cadastrar(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')
    elif request.method == "POST":
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        if len(senha) < 6:
            messages.error(request, 'Senha menor que 6 caracteres')
            return redirect('cadastrar')
        if not nome or not senha:
            messages.error(request, 'Preencha todos os campos')
            return redirect('cadastrar')
        if not User.objects.filter(username=nome).exists():
            User.objects.create_user(username=nome, password=senha)
            messages.success(request, 'Usuario cadastrado com sucesso')
            return redirect('logar')
        else:
            messages.error(request, 'Usuario já existe, tente novamente')
            return redirect('cadastrar')