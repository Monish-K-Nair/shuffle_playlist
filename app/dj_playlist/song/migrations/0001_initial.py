# Generated by Django 4.0.4 on 2022-05-22 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SongDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=20)),
                ('genre', models.CharField(blank=True, default='', max_length=30)),
                ('duration', models.CharField(blank=True, default='', max_length=10)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('artist', models.CharField(blank=True, default='', max_length=100)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.song')),
            ],
        ),
    ]
