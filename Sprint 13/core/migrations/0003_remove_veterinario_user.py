# Generated by Django 5.2.3 on 2025-06-27 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_medicamento_veterinario_cirugia_bitacoraconsulta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veterinario',
            name='user',
        ),
    ]
