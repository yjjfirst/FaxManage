from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from product.models import Campaign, FaxNumber, DeletedFaxNumber


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'fax', 'send_date', 'send']
    # list_display = ['name', 'fax', 'fax_number', 'send_date', 'send']

    def send(self, obj):
        return format_html('<a href="/sendfax?id=' + str(obj.id) + '">Send</a>')
    send.short_description = 'SEND'


class FaxNumberAdmin(admin.ModelAdmin):
    list_display = ['number']
    list_filter = ['campaign__name']
    search_fields = ['number']

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(FaxNumber, FaxNumberAdmin)
admin.site.register(DeletedFaxNumber)
