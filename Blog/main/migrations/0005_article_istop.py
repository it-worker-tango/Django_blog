# Generated by Django 2.1.5 on 2019-01-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_article_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isTop',
            field=models.BooleanField(default=True, verbose_name='置顶'),
        ),
    ]
