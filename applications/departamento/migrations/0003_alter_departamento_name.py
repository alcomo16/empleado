# Generated by Django 4.2.7 on 2023-11-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_anulate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre'),
        ),
    ]
