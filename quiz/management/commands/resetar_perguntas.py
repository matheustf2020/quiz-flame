from django.core.management.base import BaseCommand
from django.db import connection
from quiz.models import Pergunta, Alternativa

class Command(BaseCommand):
    help = 'Apaga todas as perguntas e alternativas, e reseta o ID (SQLite)'

    def handle(self, *args, **options):
        self.stdout.write('🔄 Apagando perguntas e alternativas...')
        Alternativa.objects.all().delete()
        Pergunta.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='quiz_pergunta';")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='quiz_alternativa';")

        self.stdout.write(self.style.SUCCESS('✅ Perguntas resetadas com sucesso!'))
