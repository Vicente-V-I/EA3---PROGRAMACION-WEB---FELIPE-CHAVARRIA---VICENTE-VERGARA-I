# Generated by Django 3.2.4 on 2021-06-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20210623_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='disponible',
        ),
        migrations.AddField(
            model_name='productos',
            name='stock',
            field=models.IntegerField(default=0, null=True),
        ),
    ]