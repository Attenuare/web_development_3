# Generated by Django 4.1.7 on 2023-04-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hollidaymodel',
            name='country',
            field=models.CharField(default=None, max_length=100, verbose_name='country'),
        ),
        migrations.AddField(
            model_name='hollidaymodel',
            name='flag',
            field=models.CharField(default=None, max_length=100, verbose_name='flag_link'),
        ),
        migrations.AlterField(
            model_name='hollidaymodel',
            name='description',
            field=models.CharField(max_length=200, verbose_name='hollidaydescription'),
        ),
    ]
