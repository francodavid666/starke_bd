# Generated by Django 4.1.7 on 2023-06-17 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starke_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinas_model',
            name='disciplina',
            field=models.CharField(blank=True, choices=[('Yoga', 'Yoga'), ('Funcional', 'Funcional'), ('Personalizado', 'Personalizado'), ('Spining', 'Spining')], default='Funcional', max_length=20),
        ),
    ]