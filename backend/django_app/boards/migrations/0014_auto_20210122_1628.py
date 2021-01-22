# Generated by Django 3.1.4 on 2021-01-22 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0013_auto_20210122_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='replies',
            field=models.ManyToManyField(blank=True, related_name='_post_replies_+', to='boards.Post', verbose_name='Replies'),
        ),
        migrations.AlterField(
            model_name='post',
            name='replies_to',
            field=models.ManyToManyField(blank=True, related_name='_post_replies_to_+', to='boards.Post', verbose_name='Replies To'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='replies',
            field=models.ManyToManyField(blank=True, related_name='_thread_replies_+', to='boards.Thread', verbose_name='Replies'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='replies_to',
            field=models.ManyToManyField(blank=True, related_name='_thread_replies_to_+', to='boards.Thread', verbose_name='Replies To'),
        ),
    ]