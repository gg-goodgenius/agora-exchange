# Generated by Django 4.0.7 on 2022-08-21 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_taskid_updatedata_resultid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatedata',
            name='exchange',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='core.exchange'),
        ),
    ]
