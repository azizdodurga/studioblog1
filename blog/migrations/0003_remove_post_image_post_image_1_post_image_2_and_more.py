# Generated by Django 4.1.5 on 2023-02-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_1',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_2',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_3',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_4',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]