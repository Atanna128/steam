# Generated by Django 3.1 on 2020-09-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0018_merge_20200831_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='images/tours/5'),
        ),
    ]