# Generated by Django 3.0.6 on 2020-06-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20200604_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
