# Generated by Django 4.1.3 on 2022-11-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_alter_notification_archive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='archive',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]