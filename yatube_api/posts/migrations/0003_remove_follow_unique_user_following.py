# Generated by Django 3.2.16 on 2023-04-20 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_follow_unique_user_following'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_user_following',
        ),
    ]