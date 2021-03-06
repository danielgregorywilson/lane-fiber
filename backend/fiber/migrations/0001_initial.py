# Generated by Django 3.1.7 on 2021-03-20 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('fiber_strand_count', models.CharField(max_length=200)),
                ('strand_config', models.CharField(max_length=200)),
                ('cable_type', models.CharField(max_length=200)),
                ('infrastructure_class', models.CharField(max_length=200)),
                ('foot_stamp_units', models.CharField(max_length=200)),
                ('foot_stamp_number', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('manufacturer_catalog_number', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('installer', models.CharField(max_length=200)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
                ('mount_type', models.CharField(max_length=200)),
                ('installation_type', models.CharField(max_length=200)),
                ('location_type', models.CharField(max_length=200)),
                ('card_rows', models.CharField(max_length=200)),
                ('card_columns', models.CharField(max_length=200)),
                ('slot_orientation', models.CharField(max_length=200)),
                ('ports_per_card', models.CharField(max_length=200)),
                ('port_type', models.CharField(max_length=200)),
                ('installation_date', models.CharField(max_length=200)),
                ('installer', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
