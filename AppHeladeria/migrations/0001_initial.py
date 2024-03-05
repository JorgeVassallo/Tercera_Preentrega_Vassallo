# Generated by Django 5.0.2 on 2024-03-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Sabores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=25)),
                ('ingredientes', models.CharField(max_length=150)),
                ('disponibilidad', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=35)),
                ('telefono', models.CharField(max_length=35)),
                ('provincia', models.CharField(max_length=35)),
            ],
        ),
    ]