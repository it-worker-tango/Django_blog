# Generated by Django 2.1.5 on 2019-01-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.CharField(max_length=50, verbose_name='文章内容')),
                ('add_date', models.DateField(auto_now=True, verbose_name='添加时间')),
                ('view_count', models.IntegerField(verbose_name='阅读量')),
                ('comments', models.IntegerField(verbose_name='留言量')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='导航名称')),
                ('add_date', models.DateField(auto_now=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='网站名')),
                ('url', models.URLField(verbose_name='友情链接地址')),
                ('add_date', models.DateField(auto_now=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='标签名称')),
                ('add_date', models.DateField(auto_now=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='WebInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indof', models.CharField(max_length=50, verbose_name='公告内容')),
                ('add_date', models.DateField(auto_now=True, verbose_name='添加时间')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='main.Tag', verbose_name='标签'),
        ),
    ]
