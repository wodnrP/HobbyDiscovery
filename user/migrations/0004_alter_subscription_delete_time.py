# Generated by Django 4.1.1 on 2022-10-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_subscription_delete_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='delete_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]