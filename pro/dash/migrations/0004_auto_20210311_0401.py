# Generated by Django 3.1.2 on 2021-03-10 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_auto_20210311_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='id',
        ),
        migrations.AddField(
            model_name='complaint',
            name='cid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
