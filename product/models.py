import csv

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from xlrd import open_workbook

from FaxManage import settings


class Campaign(models.Model):
    name = models.CharField(max_length=50)
    send_date = models.DateField(null=True, blank=True)
    fax = models.FileField(null=True, blank=True)
    fax_number = models.FileField()


class FaxNumber(models.Model):
    number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.number


@receiver(post_save, sender=Campaign)
def insert_fax_number(sender, instance, created=False, **kwargs):
    campaign = instance
    fax_number_file = settings.BASE_DIR + '/media/' + campaign.fax_number.name

    fax_number_list = []
    if campaign.fax_number.name.split('.')[-1].lower() == 'csv':
        with open(fax_number_file) as csvfile:
            csvReader = csv.reader(csvfile)
            for row in csvReader:
                fax_number_list += row
    else:
        excel = open_workbook(fax_number_file)
        sheet = excel.sheet_by_index(0)
        for row_id in range(sheet.nrows):
            fax_number_list.append(str(sheet.row(row_id)[0].value).split('.')[0])
        print(fax_number_list)

    try:
        for fax_num in fax_number_list:
            FaxNumber.objects.get_or_create(number=fax_num)
    except Exception as e:
        print(e)

