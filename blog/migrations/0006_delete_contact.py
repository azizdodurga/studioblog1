# Generated by Django 4.1.5 on 2023-02-20 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contact_alter_post_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
