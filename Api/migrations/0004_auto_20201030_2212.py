# Generated by Django 3.1.2 on 2020-10-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_auto_20201030_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='Date',
            field=models.CharField(max_length=12),
        ),
    ]
