# Generated by Django 3.0.8 on 2021-01-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backs', '0011_auto_20210118_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studclass',
            name='Id',
            field=models.CharField(max_length=6, primary_key='True', serialize=False),
        ),
    ]