# Generated by Django 3.1.3 on 2022-01-30 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('device_name', models.CharField(db_column='device_name', max_length=20)),
                ('device_command', models.CharField(db_column='device_command', max_length=10)),
                ('device_command_time', models.DateTimeField(auto_now_add=True, db_column='device_command_time')),
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='members.members', unique=True)),
            ],
            options={
                'db_table': 'devices',
            },
        ),
    ]
