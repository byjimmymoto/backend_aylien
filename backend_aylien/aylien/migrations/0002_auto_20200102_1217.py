# Generated by Django 3.0.1 on 2020-01-02 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aylien', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ayliensentiment',
            unique_together={('url', 'polarity')},
        ),
    ]
