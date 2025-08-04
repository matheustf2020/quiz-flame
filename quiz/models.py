from django.db import models
from django.contrib.auth.models import AbstractUser

class Pergunta(models.Model):
    texto = models.CharField(max_length=150)

class Alternativa(models.Model):
    texto = models.CharField(max_length=150)
    correta = models.BooleanField()
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)


class Resultado(models.Model):
    nome = models.CharField(max_length=100)  # pode ser opcional ou default "Anônimo"
    pontuacao = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.pontuacao} pontos'
    
class Usuario(AbstractUser):
    pontuacao_total = models.IntegerField(default=0)
    nivel_atual = models.IntegerField(default=0)
    quantidade_quizzes = models.IntegerField(default=0)
    ultima_pontuacao = models.IntegerField(default=0)
    data_nascimento = models.IntegerField(default=0)
    bio = models.TextField(blank=True)

    
