# Generated by Django 3.2.6 on 2021-08-31 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('isbn', models.CharField(blank=True, max_length=100)),
                ('publisher', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
