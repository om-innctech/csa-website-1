# Generated by Django 2.2 on 2019-09-19 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csa', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AgentLead',
        ),
        migrations.RemoveField(
            model_name='customerlead',
            name='for_property',
        ),
        migrations.DeleteModel(
            name='FloorPlan',
        ),
        migrations.RemoveField(
            model_name='property',
            name='address',
        ),
        migrations.RemoveField(
            model_name='property',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='property',
            name='media',
        ),
        migrations.RemoveField(
            model_name='property',
            name='nearest',
        ),
        migrations.RemoveField(
            model_name='property',
            name='other_charges',
        ),
        migrations.RemoveField(
            model_name='property',
            name='overlooking',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='CustomerLead',
        ),
        migrations.DeleteModel(
            name='Landmark',
        ),
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.DeleteModel(
            name='Nearest',
        ),
        migrations.DeleteModel(
            name='OtherCharges',
        ),
        migrations.DeleteModel(
            name='Overlooking',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
