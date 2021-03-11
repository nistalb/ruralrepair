# Generated by Django 3.1.7 on 2021-03-10 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('part_number', models.CharField(blank=True, max_length=100)),
                ('source', models.CharField(blank=True, max_length=100)),
                ('cost', models.PositiveIntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('make', models.CharField(blank=True, max_length=100)),
                ('mfg_year', models.PositiveIntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True)),
                ('age', models.PositiveIntegerField(blank=True, default=0)),
                ('incrementer', models.CharField(choices=[('M', 'Miles'), ('H', 'Hours')], default='M', max_length=1)),
                ('cost', models.PositiveIntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('interval', models.PositiveIntegerField(blank=True, default=0)),
                ('interval_type', models.CharField(choices=[('M', 'Miles'), ('H', 'Hours'), ('S', 'Months')], default='M', max_length=1)),
                ('duration', models.PositiveIntegerField(blank=True, default=0)),
                ('instructions', models.TextField(blank=True)),
                ('video', models.CharField(blank=True, max_length=400)),
                ('consumable', models.ManyToManyField(to='main_app.Consumable')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.equipment')),
                ('tool', models.ManyToManyField(to='main_app.Tool')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('hourly_rate', models.PositiveIntegerField(blank=True, default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.equipment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maint_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('mileage', models.PositiveIntegerField(blank=True, default=0)),
                ('hours', models.PositiveIntegerField(blank=True, default=0)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.equipment')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.task')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]