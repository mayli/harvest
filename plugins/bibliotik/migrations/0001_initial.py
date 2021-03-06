# Generated by Django 2.1.7 on 2019-02-23 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BibliotikClientConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('is_server_side_login_enabled', models.BooleanField()),
                ('login_datetime', models.DateTimeField(null=True)),
                ('cookies', models.BinaryField(null=True)),
                ('last_login_failed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BibliotikThrottledRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('url', models.CharField(max_length=2048)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
