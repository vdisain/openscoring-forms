# Generated by Django 3.2.13 on 2022-12-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lorem', '0003_auto_20221228_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='lorem',
            name='number_field',
            field=models.IntegerField(default=0),
        ),
    ]