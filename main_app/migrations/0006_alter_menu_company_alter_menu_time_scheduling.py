# Generated by Django 4.0.6 on 2022-07-29 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_addonitem_price_alter_items_disc_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.company'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='time_scheduling',
            field=models.BooleanField(default=False),
        ),
    ]
