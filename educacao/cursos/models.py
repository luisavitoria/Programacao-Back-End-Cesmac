from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo