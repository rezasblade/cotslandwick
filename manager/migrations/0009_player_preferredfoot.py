# Generated by Django 2.1.2 on 2019-02-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20190201_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='preferredfoot',
            field=models.CharField(default='Right', max_length=50),
        ),
    ]