# Generated by Django 2.0.6 on 2018-07-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minutetalk', '0007_auto_20180703_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]