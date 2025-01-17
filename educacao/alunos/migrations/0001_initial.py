# Generated by Django 5.1.4 on 2024-12-07 22:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('sobrenome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('cursos', models.ManyToManyField(related_name='alunos', to='cursos.curso')),
            ],
        ),
    ]
