# Generated by Django 3.1.3 on 2022-06-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='sub_phone_number',
            field=models.CharField(db_column='sub_phone_number', default='01099999999', max_length=13),
            preserve_default=False,
        ),
    ]
