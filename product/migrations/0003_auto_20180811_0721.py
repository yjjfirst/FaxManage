# Generated by Django 2.1 on 2018-08-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_campaign_test_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='fax',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='fax_number',
            field=models.FileField(upload_to=''),
        ),
    ]
