# Generated by Django 3.2.6 on 2021-09-01 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book_tmp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tmp',
        ),
    ]
