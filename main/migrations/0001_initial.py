# Generated by Django 4.1.1 on 2022-11-03 10:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('pd_id', models.AutoField(primary_key=True, serialize=False)),
                ('pd_title', models.CharField(max_length=100)),
                ('pd_descrition', models.TextField()),
                ('pd_info', models.TextField(blank=True, null=True)),
                ('pd_price', models.IntegerField()),
                ('pd_sell', models.CharField(blank=True, max_length=100, null=True)),
                ('pd_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HobbyImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=main.models.image_upload_path)),
                ('pd_image', models.ImageField(blank=True, null=True, upload_to=main.models.image_upload_path)),
            ],
            options={
                'db_table': 'hobby_image',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('grade', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('hobby_rv', models.ForeignKey(blank=True, db_column='hobby_rv', on_delete=django.db.models.deletion.CASCADE, related_name='hobby_rv', to='main.hobby')),
            ],
        ),
        migrations.CreateModel(
            name='Review_Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.image_upload_path)),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rv_image', to='main.review')),
            ],
            options={
                'db_table': 'review_image',
            },
        ),
    ]
