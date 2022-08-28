# Generated by Django 4.0.4 on 2022-07-25 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_alter_user_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.listings'),
        ),
    ]