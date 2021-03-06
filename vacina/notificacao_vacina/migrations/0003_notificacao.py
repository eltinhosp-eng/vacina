# Generated by Django 3.2.9 on 2021-12-06 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notificacao_vacina', '0002_pessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificacao_celular', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
                ('notificacao_email', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao_vacina.pessoa')),
                ('vacina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificacao_vacina.vacina')),
            ],
        ),
    ]
