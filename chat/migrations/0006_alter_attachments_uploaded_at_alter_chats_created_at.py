# Generated by Django 4.1.6 on 2023-02-16 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_attachments_uploaded_at_alter_attachments_attachment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 16, 14, 6, 35, 884077)),
        ),
        migrations.AlterField(
            model_name='chats',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 16, 14, 6, 35, 883074)),
        ),
    ]
