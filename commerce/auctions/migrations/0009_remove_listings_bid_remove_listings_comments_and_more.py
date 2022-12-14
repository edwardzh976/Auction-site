# Generated by Django 4.0.4 on 2022-07-18 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_bids_remove_listings_bid_listings_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='listings',
            name='comments',
        ),
        migrations.AddField(
            model_name='listings',
            name='bid_id',
            field=models.ManyToManyField(blank=True, to='auctions.bids'),
        ),
        migrations.AddField(
            model_name='listings',
            name='comments_id',
            field=models.ManyToManyField(blank=True, to='auctions.comments'),
        ),
    ]
