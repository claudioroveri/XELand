# Generated by Django 4.1.3 on 2022-11-24 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0004_delete_palestrante_delete_tipoevento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palestrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('instituicao', models.CharField(max_length=50)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('horario', models.DateTimeField()),
                ('vagas', models.IntegerField(default=40)),
                ('palestrante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.palestrante')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipoevento')),
            ],
        ),
    ]
