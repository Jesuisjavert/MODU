# Generated by Django 3.1.2 on 2020-11-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerschedule',
            name='end_hour',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trainerschedule',
            name='start_hour',
            field=models.TimeField(),
        ),
    ]