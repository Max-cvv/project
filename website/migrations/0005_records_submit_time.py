# Generated by Django 2.0 on 2021-04-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210423_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='submit_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
