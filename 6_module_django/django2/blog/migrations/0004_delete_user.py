# Generated by Django 5.0.6 on 2024-06-16 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
