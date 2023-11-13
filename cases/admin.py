from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Case, Order, OrderItem


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'maker', 'city', 'region', 'capacity', 'base_value', 'buy_assurance',
                    'guaranteed_gain', 'guaranteed_gain_percent', 'end_time', 'status', 'datetime_created')
    ordering = ('-datetime_created', )
    prepopulated_fields = {'slug': ('title',)}
    # inlines = [
    #     ReviewInProductInline,
    # ]

class ItemsInOrdersInline(admin.TabularInline):
    model = OrderItem
    fields = ('order', 'case', 'meter', 'base_value',)
    extra = 1

@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'is_paid', 'national_code', 'datetime_created',)
    ordering = ('-datetime_created', )
    inlines = [
        ItemsInOrdersInline,
    ]

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('order', 'case', 'meter', 'base_value',)


