# Generated by Django 4.2.4 on 2023-08-14 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repot', '0002_alter_news_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='news',
            new_name='New',
        ),
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'new', 'verbose_name_plural': 'news'},
        ),
    ]
