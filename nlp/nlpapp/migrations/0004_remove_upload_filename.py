# Generated by Django 2.0 on 2023-03-10 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nlpapp', '0003_auto_20230310_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='filename',
        ),
    ]
