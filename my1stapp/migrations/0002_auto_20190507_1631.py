# Generated by Django 2.1.4 on 2019-05-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my1stapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
