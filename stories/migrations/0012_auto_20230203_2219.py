# Generated by Django 3.2.7 on 2023-02-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0011_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='webstory',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='static/cover/'),
        ),
    ]
