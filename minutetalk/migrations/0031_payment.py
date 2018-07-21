# Generated by Django 2.0.7 on 2018-07-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minutetalk', '0030_channel_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('cardname', models.CharField(max_length=20)),
                ('cardnumber', models.CharField(max_length=16)),
                ('expirydate', models.CharField(max_length=10)),
                ('cvc', models.CharField(max_length=4)),
            ],
        ),
    ]
