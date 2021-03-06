# Generated by Django 3.1.5 on 2021-03-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('last_sent_time', models.DateTimeField()),
                ('token', models.CharField(max_length=64, null=True, unique=True)),
            ],
        ),
    ]
