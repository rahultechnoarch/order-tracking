# Generated by Django 3.2.6 on 2021-09-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210901_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='status',
            field=models.CharField(choices=[('Order_received', 'Order Received'), ('In_transit', 'In Transit'), ('Out_for_delivery', 'Out for Delivery'), ('Order_delivered', 'Order Delivered')], default='Order Received', max_length=50),
        ),
    ]
