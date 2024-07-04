# Generated by Django 5.0.4 on 2024-04-28 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_image', models.ImageField(upload_to='')),
                ('bio', models.TextField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='customers.customer')),
            ],
        ),
    ]
