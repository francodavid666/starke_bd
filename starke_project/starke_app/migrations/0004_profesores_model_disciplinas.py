# Generated by Django 3.2.18 on 2023-06-22 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('starke_app', '0003_remove_disciplinas_model_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesores_model',
            name='disciplinas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='starke_app.disciplinas_model'),
        ),
    ]
