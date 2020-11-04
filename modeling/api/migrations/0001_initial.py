# Generated by Django 3.1.2 on 2020-11-04 07:46

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=800)),
                ('visit_count', models.IntegerField(default=0)),
                ('thumb_img', models.ImageField(blank=True, null=True, upload_to=api.models.program_image_path)),
                ('tags', models.ManyToManyField(to='accounts.Tag')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program', to='accounts.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('online_count', models.IntegerField()),
                ('offline_count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programprice', to='api.program')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('max_online_count', models.IntegerField()),
                ('max_offline_count', models.IntegerField()),
                ('now_online_count', models.IntegerField()),
                ('now_offline_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programrecord', to='accounts.client')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programrecord', to='api.program')),
                ('programprice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programrecord', to='api.programprice')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramReservationDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='날짜')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programreservationday', to='api.program')),
            ],
        ),
        migrations.CreateModel(
            name='TrainerComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('content', models.CharField(max_length=800)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainercomment', to='accounts.client')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainercomment', to='accounts.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20, verbose_name='00요일')),
                ('start_hour', models.DateTimeField()),
                ('end_hour', models.DateTimeField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progamschedule', to='api.program')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramReservationTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.DateTimeField()),
                ('end_hour', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ProgramDay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programreservationtime', to='api.programreservationday')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programreservationtime', to='accounts.client')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramRecordDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_type', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=800)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('programRecord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programrecorddetail', to='api.programrecord')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programpayment', to='accounts.client')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programpayment', to='api.program')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('content', models.CharField(max_length=800)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programcomment', to='accounts.client')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programcomment', to='api.program')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programcomment', to='accounts.trainer')),
            ],
        ),
    ]
