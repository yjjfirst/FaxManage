# Generated by Django 2.1 on 2018-08-11 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='test_field',
        ),
    ]
