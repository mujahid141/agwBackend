# Generated by Django 5.0.4 on 2024-04-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='customer_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, null=True, related_name='customer_user_permissions', to='auth.permission'),
        ),
    ]
