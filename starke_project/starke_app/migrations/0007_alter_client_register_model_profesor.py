# Generated by Django 4.1.7 on 2023-06-17 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('starke_app', '0006_client_register_model_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_register_model',
            name='profesor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='starke_app.profesores_model'),
        ),
    ]
