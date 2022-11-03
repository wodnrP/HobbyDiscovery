# Generated by Django 4.1.1 on 2022-11-03 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coments',
            name='post_id',
            field=models.ForeignKey(blank=True, db_column='post_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_num', to='community.post'),
        ),
        migrations.AddField(
            model_name='coments',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='comenter', to=settings.AUTH_USER_MODEL),
        ),
    ]
