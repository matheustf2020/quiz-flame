from django.contrib import admin
from .models import Pergunta, Resultado, Alternativa, Usuario

#admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(Resultado)

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 7  # já mostra 7 campos vazios por padrão

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    inlines = [AlternativaInline]

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'pontuacao_total', 'nivel_atual', 'quantidade_quizzes', 'ultima_pontuacao',)