# Generated by Django 3.1.5 on 2021-03-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maillist',
            name='mail_sent',
            field=models.BooleanField(default=False),
        ),
    ]
