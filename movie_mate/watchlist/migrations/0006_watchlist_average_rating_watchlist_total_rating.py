# Generated by Django 4.2 on 2023-04-22 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0005_review_review_user_alter_review_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='total_rating',
            field=models.IntegerField(default=0),
        ),
    ]