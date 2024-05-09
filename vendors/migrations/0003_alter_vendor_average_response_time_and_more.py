# Generated by Django 5.0.4 on 2024-05-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_historicalperformance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='average_response_time',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(null=True),
        ),
    ]
