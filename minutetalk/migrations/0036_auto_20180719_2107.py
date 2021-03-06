# Generated by Django 2.0.7 on 2018-07-19 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minutetalk', '0035_merge_20180719_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatlog',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='minutetalk.Channel'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
