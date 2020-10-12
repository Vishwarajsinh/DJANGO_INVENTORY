from django.contrib import admin
from .models import *

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "decs",
        "category",
        "current_stock",
        "unit",
        "created_at",
    ]
    list_filter = [
        "category",
    ]

class PurchaseOrderAdmin(admin.TabularInline):
    model = PurchaseOrderItem
    list_display = [
        "bill_no", "category", "sub_category",
        "quantity", "unit_group", "unit",
        "mrp_per_unit", "supplier_name", "purchased_at",
    ]
    list_filter = ["item","mrp_per_unit",]

    readonly_fields = ['get_subtotal']

    def get_subtotal(self, obj):
        po_item = PurchaseOrderItem.objects.get(id=obj.id)
        po_item_subtotal = obj.quantity * obj.mrp_per_unit
        # return a str representation of entry subtotal
        return "₹" + str(po_item_subtotal)
    # set helper method's description display
    get_subtotal.short_description = 'subtotal'

class PurchaseBillAdmin(admin.ModelAdmin):
    inlines = (PurchaseOrderAdmin, )
    list_display = [
        "bill_no",
        "notes",
        "get_total",
        "purchased_at",
    ]
    readonly_fields = ["get_total",]

    def get_total(self, obj):
        # extend scope of variable
        total_price = 0
        # get all entries for the given cart
        po_items = PurchaseOrderItem.objects.filter(bill_no = PurchaseBill.objects.get(id=obj.id))
        # iterate through entries
        for item in po_items:
            total_price += item.quantity * item.mrp_per_unit
        return total_price
    # give the helper method a description to be displayed
    get_total.short_description = 'total'
    
class IssueOrderAdmin(admin.TabularInline):
    model = IssueOrderItem
    list_display = [
        "category",
        "sub_category",
        "quantity",
        "issued_at",
        "unit",
    ]
    list_filter = [
        "category",
        "issued_at",
    ]
    search_fields = [
        "category",
    ]

class IssueBillAdmin(admin.ModelAdmin):
    inlines = (IssueOrderAdmin, )
    list_display = [
        "bill_no",
        "issued_by",
        "issued_at",
    ]

class UnitGroupAdmin(admin.ModelAdmin):
    list_display = ['name']

class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit_group']
    list_filter = ['unit_group']


admin.site.register( Category ),
admin.site.register( UnitGroup, UnitGroupAdmin ),
admin.site.register( Unit, UnitAdmin ),
admin.site.register( Item, ItemAdmin ),
admin.site.register( PurchaseBill, PurchaseBillAdmin ),
admin.site.register( IssueBill, IssueBillAdmin ),
