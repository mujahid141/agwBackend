# Generated by Django 4.2.4 on 2024-06-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_remove_userprofile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='customer_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
