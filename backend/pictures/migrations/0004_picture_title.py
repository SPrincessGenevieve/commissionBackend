# Generated by Django 4.2.5 on 2023-09-21 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_remove_picture_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='title',
            field=models.CharField(default='Untitled', max_length=255),
        ),
    ]
