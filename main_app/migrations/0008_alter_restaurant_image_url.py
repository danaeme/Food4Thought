# Generated by Django 5.1.1 on 2024-09-23 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_restaurant_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
