# Generated by Django 3.1.7 on 2021-03-23 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maint_record',
            old_name='hours',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='maint_record',
            name='mileage',
        ),
        migrations.AddField(
            model_name='maint_record',
            name='incrementor',
            field=models.CharField(default='M', max_length=1),
        ),
    ]
