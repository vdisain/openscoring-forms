# Generated by Django 3.2.13 on 2022-12-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lorem', '0004_lorem_number_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='lorem',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]
