# Generated by Django 3.2.7 on 2023-02-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0013_auto_20230203_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='webstory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
