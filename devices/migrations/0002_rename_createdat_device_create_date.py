# Generated by Django 4.0.4 on 2022-06-05 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='createdat',
            new_name='create_date',
        ),
    ]