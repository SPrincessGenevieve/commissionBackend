# Generated by Django 4.2.5 on 2023-09-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
