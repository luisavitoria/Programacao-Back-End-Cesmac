from django.db import models
from cursos.models import Curso
import uuid

class Aluno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    email = models.EmailField()
    cursos = models.ManyToManyField(Curso, related_name="alunos")

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

