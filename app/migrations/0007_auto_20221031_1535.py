# Generated by Django 3.1.2 on 2022-10-31 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_commande_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='items',
            new_name='Item',
        ),
    ]
