# Generated by Django 3.1.5 on 2021-03-27 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0008_maillist_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MailList',
        ),
    ]