# Generated by Django 3.1.3 on 2023-05-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230523_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
