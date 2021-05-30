from django.contrib import admin
from .models import Refund


class RefundAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['order_number', 'reason']


admin.site.register(Refund, RefundAdmin)
