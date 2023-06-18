# Generated by Django 4.1.7 on 2023-06-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starke_app', '0003_client_register_model_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='profesores_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesor', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='disciplinas_model',
            name='disciplina',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]