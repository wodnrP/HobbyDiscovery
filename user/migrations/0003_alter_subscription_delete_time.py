# Generated by Django 4.1.1 on 2022-10-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_sub_pd_subscription_subpd_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='delete_time',
            field=models.DateTimeField(null=True),
        ),
    ]