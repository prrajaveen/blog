from django.contrib import admin
from stock.models import Stock

@admin.register(Stock)
class AllStockAdmin(admin.ModelAdmin):
    list_display = ['symbol','company_name','market_cap']
    ordering = ('-market_cap',)
