# Generated by Django 3.1.2 on 2021-03-11 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_auto_20210311_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(default='Complaint Registered', max_length=1000),
        ),
    ]
