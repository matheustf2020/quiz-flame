from django.shortcuts import render, redirect, get_object_or_404
from .models import Pergunta, Alternativa, Resultado
from django.http import HttpResponse
from datetime import datetime, timedelta


def bem_vindo(request):
    if request.method == "GET":
        return render(request, 'index.html')
    

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
        TOTAL_PERGUNTAS = 4
        if numero >= TOTAL_PERGUNTAS:
            # Resultado.objects.create(
            #     nome='Sem Nome',
            #     pontuacao=request.session['pontuacao']
            # )
            return redirect('nome')

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

def resultado_view(request):
    pontuacao = request.session.get('pontuacao', 0)

    request.session['ultimo_jogo'] = datetime.now().isoformat()


    if 'pontuacao' in request.session:
        del request.session['pontuacao']

    ranking = Resultado.objects.order_by('-pontuacao', '-data')[:5]

    return render(request, 'resultado.html', {
        'pontuacao': pontuacao,
        'ranking': ranking
    })

def nome_view(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        pontuacao = request.session.get('pontuacao', 0)

        Resultado.objects.create(nome=nome, pontuacao=pontuacao)
        return redirect('resultado')

    return render(request, 'nome.html')

