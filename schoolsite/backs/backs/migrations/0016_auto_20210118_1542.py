# Generated by Django 3.0.8 on 2021-01-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backs', '0015_time_table_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studclass',
            name='Id',
            field=models.CharField(help_text='100lvl', max_length=6, primary_key='True', serialize=False),
        ),
    ]
