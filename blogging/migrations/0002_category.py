# Generated by Django 3.1.3 on 2020-11-05 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('posts', models.ManyToManyField(blank=True, related_name='categories', to='blogging.Post')),
            ],
        ),
    ]
