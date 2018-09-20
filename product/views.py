import csv
from subprocess import call

from django.contrib import messages
from django.shortcuts import redirect
from xlrd import open_workbook

# Create your views here.
from FaxManage import settings
from product.models import Campaign


def send_fax(request):
    try:
        _id = int(request.GET.get('id', 0))
    except Exception as e:
        messages.error(request, 'Parsing url is failed.')
        return redirect('/admin/product/campaign')
    campaign = Campaign.objects.get(id=_id)
    fax_file = settings.BASE_DIR + '/media/' + campaign.fax.name
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

    for fax_num in fax_number_list:
        if str(fax_num)[0] != '1':
            fax_num = '1' + str(fax_num)
        call(['sendfax', '-T 5', '-d', fax_num, fax_file])
    messages.info(request, 'Sent fax to %d fax numbers.' % len(fax_number_list))
    return redirect('/admin/product/campaign')
