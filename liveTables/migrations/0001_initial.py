# Generated by Django 3.0.6 on 2020-06-03 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
                ('home_score', models.IntegerField(blank=True, default=None, null=True)),
                ('away_score', models.IntegerField(blank=True, default=None, null=True)),
                ('result', models.CharField(max_length=4)),
                ('match_number', models.IntegerField(unique=True)),
                ('status', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('matches', models.ManyToManyField(to='liveTables.Match')),
            ],
        ),
    ]
