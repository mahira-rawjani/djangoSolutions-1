# Generated by Django 5.0.1 on 2024-02-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(null='True', upload_to='uploads/products'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(null='True', upload_to='uploads/products'),
            preserve_default='True',
        ),
    ]
