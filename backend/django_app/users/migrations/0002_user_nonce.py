# Generated by Django 3.1.4 on 2021-03-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nonce',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Nonce'),
        ),
    ]
