# Generated by Django 2.1.4 on 2018-12-05 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='palestrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=100)),
                ('palestrante', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('resumo', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
            ],
        ),
    ]
