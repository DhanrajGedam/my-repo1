# Generated by Django 4.1.1 on 2022-09-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]