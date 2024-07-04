# Generated by Django 5.0.4 on 2024-05-01 05:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customerprofile'),
        ('orders', '0002_alter_cart_customer_alter_order_customer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='address',
            name='customer',
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField()),
                ('birth_date', models.DateField(null=True)),
                ('membership', models.CharField(choices=[('B', 'Bronze'), ('S', 'Silver'), ('G', 'Gold')], default='B', max_length=1)),
                ('customer_image', models.ImageField(upload_to='')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerProfile',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]