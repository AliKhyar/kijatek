# Generated by Django 3.0.4 on 2020-04-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200414_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='abreviated_name',
            field=models.CharField(max_length=100, verbose_name='Abreviated Name'),
        ),
    ]
