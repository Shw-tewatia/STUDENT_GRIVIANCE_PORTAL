# Generated by Django 4.2.5 on 2023-11-02 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_complain_createed_at_alter_complain_complain_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complain',
            old_name='createed_at',
            new_name='created_at',
        ),
    ]