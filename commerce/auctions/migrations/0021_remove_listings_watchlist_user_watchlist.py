# Generated by Django 4.0.4 on 2022-07-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_remove_user_watchlist_listings_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, to='auctions.listings'),
        ),
    ]
