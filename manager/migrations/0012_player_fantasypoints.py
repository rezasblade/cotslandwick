# Generated by Django 2.1.2 on 2019-02-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_auto_20190206_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='fantasypoints',
            field=models.IntegerField(default=0),
        ),
    ]