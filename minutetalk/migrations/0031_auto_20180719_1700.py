# Generated by Django 2.0.6 on 2018-07-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minutetalk', '0030_channel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
