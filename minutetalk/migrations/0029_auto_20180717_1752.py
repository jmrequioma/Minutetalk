# Generated by Django 2.0.6 on 2018-07-17 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minutetalk', '0028_auto_20180717_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channel_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='minutetalk.ChannelType'),
        ),
    ]
