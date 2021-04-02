# Generated by Django 3.0.8 on 2020-08-25 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0008_merge_20200825_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='images/tours/1'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/avatar'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.TextField(help_text='One word about your trip !', max_length=100),
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('follower', 'following')},
            },
        ),
    ]
