# Generated by Django 4.1.1 on 2022-11-03 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_add', models.TextField()),
                ('o_num', models.CharField(max_length=200)),
                ('o_name', models.CharField(max_length=200)),
                ('o_pay', models.CharField(max_length=100)),
                ('o_total_price', models.IntegerField()),
                ('o_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_quantity', models.IntegerField()),
                ('od_price', models.IntegerField()),
                ('od_id', models.ForeignKey(db_column='od_id', on_delete=django.db.models.deletion.CASCADE, related_name='order', to='order.order')),
                ('od_pd', models.ForeignKey(db_column='od_hobby', on_delete=django.db.models.deletion.CASCADE, related_name='order_hobby', to='main.hobby')),
            ],
        ),
    ]
