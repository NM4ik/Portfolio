# Generated by Django 3.2.6 on 2021-08-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_work_background_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
