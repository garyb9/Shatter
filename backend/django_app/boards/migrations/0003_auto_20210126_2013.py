# Generated by Django 3.1.4 on 2021-01-26 18:13

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20210126_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
        migrations.AddField(
            model_name='post',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
        migrations.AddField(
            model_name='thread',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
        migrations.AlterField(
            model_name='board',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Image'),
        ),
    ]
