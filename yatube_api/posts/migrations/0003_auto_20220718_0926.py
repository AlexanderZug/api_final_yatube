# Generated by Django 2.2.16 on 2022-07-18 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220717_1421'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_name_follow',
        ),
    ]
