# Generated by Django 4.1.6 on 2023-02-16 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_chats_created_at_attachments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachments',
            name='attachments',
        ),
        migrations.AddField(
            model_name='attachments',
            name='attachment',
            field=models.FileField(null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='chats',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 16, 10, 29, 47, 153121)),
        ),
    ]
