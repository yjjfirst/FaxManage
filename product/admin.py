from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from product.models import Campaign, FaxNumber


class CampaignAdmin(admin.ModelAdmin):
    fields = ('name', 'fax', 'fax_number', 'send_date')
    list_display = ['name', 'fax', 'fax_number', 'send_date', 'send']

    def send(self, obj):
        return format_html('<a href="/sendfax?id=' + str(obj.id) + '">Send</a>')
    send.short_description = 'SEND'

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(FaxNumber)
