# Generated by Django 3.1.4 on 2021-01-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_remove_post_ispinned'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='isPruned',
            field=models.BooleanField(default=False, verbose_name='Is Pruned'),
        ),
    ]