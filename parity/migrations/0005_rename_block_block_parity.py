# Generated by Django 4.0.4 on 2022-07-12 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parity', '0004_alter_block_position'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Block',
            new_name='Block_parity',
        ),
    ]