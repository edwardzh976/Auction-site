# Generated by Django 4.0.4 on 2022-07-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_listings_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, to='auctions.listings'),
        ),
    ]
