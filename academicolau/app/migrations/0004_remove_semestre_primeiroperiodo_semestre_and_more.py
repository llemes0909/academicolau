# Generated by Django 4.2.5 on 2023-09-25 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_curso_area_saber_alter_disciplina_area_saber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semestre',
            name='primeiroperiodo_semestre',
        ),
        migrations.RemoveField(
            model_name='semestre',
            name='segundoperiodo_semestre',
        ),
    ]
