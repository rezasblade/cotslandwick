# Generated by Django 2.1.2 on 2019-02-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_player_fantasypoints'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
