# Generated by Django 3.2.9 on 2021-12-06 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificacao_vacina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
