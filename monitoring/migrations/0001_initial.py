# Generated by Django 2.1.7 on 2019-03-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('status', models.CharField(choices=[('green', 'green'), ('yellow', 'yellow'), ('red', 'red')], max_length=64)),
                ('updated_datetime', models.DateTimeField()),
                ('message', models.TextField()),
                ('traceback', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(db_index=True)),
                ('level', models.IntegerField()),
                ('message', models.TextField()),
                ('traceback', models.TextField(null=True)),
            ],
        ),
    ]
