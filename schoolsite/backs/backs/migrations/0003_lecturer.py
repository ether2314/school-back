# Generated by Django 3.0.8 on 2021-01-15 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backs', '0002_auto_20210115_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Date_of_Birth', models.DateField(help_text='yy-mm-dd')),
                ('phone_no', models.DecimalField(decimal_places=0, max_digits=11)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('state', models.CharField(choices=[('enugu', 'enugu'), ('Anambra', 'Anambra'), ('Kano', 'Kano'), ('Imo', 'Imo'), ('Bauchi', 'Bauchi'), ('Kastina', 'Kastina'), ('Abuja', 'Abuja')], max_length=50)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backs.Department')),
                ('faculty', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backs.Faculty')),
            ],
        ),
    ]
