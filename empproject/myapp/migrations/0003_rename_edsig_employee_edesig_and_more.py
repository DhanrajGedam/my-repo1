# Generated by Django 4.1.1 on 2022-09-22 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='edsig',
            new_name='edesig',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='eesal',
            new_name='esal',
        ),
    ]