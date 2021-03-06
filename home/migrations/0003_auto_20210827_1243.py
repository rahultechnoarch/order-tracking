# Generated by Django 3.2.6 on 2021-08-27 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20210827_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='update_Time',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_Time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_Time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Order Received', 'Order Received'), ('Order Scheduled', 'Order Scheduled'), ('Shipped Out', 'Shipped Out'), ('Arrived at warehouse', 'Arrived at warehouse'), ('Out for Delivery', 'Out for Delivery'), ('Order Delivered', 'Order Delivered')], default='Order Received', max_length=50)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
