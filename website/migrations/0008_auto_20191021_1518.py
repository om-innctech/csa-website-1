# Generated by Django 2.2 on 2019-10-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20191021_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='content',
            field=models.CharField(max_length=440),
        ),
    ]
