# Generated by Django 4.2.7 on 2023-11-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twocolumns', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='l_name',
        ),
        migrations.AddField(
            model_name='student',
            name='full_name',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
