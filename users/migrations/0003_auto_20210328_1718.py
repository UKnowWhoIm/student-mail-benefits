# Generated by Django 3.1.5 on 2021-03-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_maillist_mail_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maillist',
            name='last_sent_time',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
