# Generated by Django 2.1 on 2019-01-02 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('matchdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.MatchDay')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='totaldraws',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='totallosses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='totalwins',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerpoints',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.Player'),
        ),
    ]