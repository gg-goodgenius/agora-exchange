# Generated by Django 4.0.7 on 2022-08-21 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_updatedata_exchange'),
    ]

    operations = [
        migrations.RenameField(
            model_name='updatedata',
            old_name='taskid',
            new_name='resultid',
        ),
    ]