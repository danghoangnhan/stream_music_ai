# Generated by Django 3.1.8 on 2021-04-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210409_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_id',
            field=models.CharField(max_length=50),
        ),
    ]
