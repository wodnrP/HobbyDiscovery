# Generated by Django 4.1.1 on 2022-10-17 04:20

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_hobby_hobby_image_hobbyimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbyimage',
            name='image',
            field=models.ImageField(upload_to=main.models.image_upload_path),
        ),
    ]