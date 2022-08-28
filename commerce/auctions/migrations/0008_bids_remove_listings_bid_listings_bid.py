# Generated by Django 4.0.4 on 2022-07-18 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_remove_comments_listing_listings_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='listings',
            name='bid',
        ),
        migrations.AddField(
            model_name='listings',
            name='bid',
            field=models.ManyToManyField(to='auctions.bids'),
        ),
    ]
