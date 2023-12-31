# Generated by Django 4.2.4 on 2023-09-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pet', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('data_reserva', models.DateField()),
                ('observacoes', models.CharField(max_length=3000)),
            ],
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contato',
            name='mensagem',
            field=models.CharField(max_length=3000),
        ),
    ]
