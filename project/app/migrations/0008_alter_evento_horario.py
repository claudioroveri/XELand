# Generated by Django 4.1.3 on 2022-11-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_local_tipo_alter_local_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='horario',
            field=models.TimeField(),
        ),
    ]
