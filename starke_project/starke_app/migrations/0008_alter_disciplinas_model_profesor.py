# Generated by Django 4.1.7 on 2023-06-17 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starke_app', '0007_alter_client_register_model_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinas_model',
            name='profesor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]