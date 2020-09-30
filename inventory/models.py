from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
from django.conf import settings
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    class Meta:
        verbose_name_plural = "SubCategories"

    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='sub_categories')
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class UnitGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    unit_group = models.ForeignKey(UnitGroup, on_delete = models.CASCADE, null=False, blank=False, related_name='units')
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    decs = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, related_name='categories')
    sub_categories = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='sub_categories')
    current_stock = models.PositiveIntegerField(editable=False, blank=True, default = 0, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.name


class ItemDetails(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, blank=False, related_name='item_detail')
    unit_group = models.ForeignKey(UnitGroup, on_delete=models.CASCADE, null=False, blank=False)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=False, blank=False)
    size = models.FloatField(default=0.0)
    stock = models.PositiveIntegerField(editable=False, blank=True, default = 0, validators=[MinValueValidator(0)])

    def __str__(self):
        # pylint: disable=E1101
        name = self.item.name
        size = self.size
        stock = self.stock
        unit = self.unit
        return f'{name} | Size: {size} {unit} | Qty: {stock}'

# autogenerate purchase bill no
def purchase_bill_number():
    last_purchase = PurchaseBill.objects.all().order_by('id').last()
    if not last_purchase:
         return 'PUR1'
    purchase_no = last_purchase.bill_no
    purchase_int = int(purchase_no.split('PUR')[-1])
    new_purchase_int = purchase_int + 1
    new_purchase_no = 'PUR' + str(new_purchase_int)
    return new_purchase_no

class PurchaseBill(models.Model):
    bill_no = models.CharField(max_length=500, default=purchase_bill_number, null=True, blank=True, unique=True)
    supplier = models.CharField(max_length=50)
    purchased_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bill_no


class PurchaseOrderItem(models.Model):
    bill_no = models.ForeignKey(PurchaseBill, on_delete=models.CASCADE, related_name = "bill_items")
    category = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, blank=False)
    sub_category = models.ForeignKey(ItemDetails, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    mrp_per_unit = models.IntegerField(default=0)
    

    def __str__(self):
        return self.category.name

# autogenerate issue bill no
def issue_bill_number():
    last_issued = IssueBill.objects.all().order_by('id').last()
    if not last_issued:
         return 'ISSUE_1'
    issue_no = last_issued.bill_no
    issue_int = int(issue_no.split('ISSUE_')[-1])
    new_issue_int = issue_int + 1
    new_issue_no = 'ISSUE_' + str(new_issue_int)
    return new_issue_no

class IssueBill(models.Model):
    bill_no = models.CharField(max_length=500, default=issue_bill_number, null=True, blank=True, unique=True)
    issued_by = models.CharField(max_length=50)
    issued_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bill_no

class IssueOrderItem(models.Model):
    bill_no = models.ForeignKey(IssueBill, on_delete=models.CASCADE, related_name = "issue_items")
    category = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, blank=False)
    sub_category = models.ForeignKey(ItemDetails, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    
    def clean(self):
        super().clean()
        if self.sub_category.stock < self.quantity:
            raise ValidationError("Insufficient Stock!")

    def __str__(self):
        return self.category.name

# Inventory update functions



@receiver(post_save, sender = PurchaseOrderItem, dispatch_uid = "update_item_stock")
def update_item_stock(sender, **kwargs):
    po_item = kwargs['instance']
    if po_item.pk:
        Item.objects.filter(pk = po_item.category_id).update(current_stock = F('current_stock') + po_item.quantity)
        ItemDetails.objects.filter(pk = po_item.sub_category_id).update(stock = F('stock') + po_item.quantity)
        

@receiver(post_save, sender = IssueOrderItem, dispatch_uid = "issue_item_stock")
def issue_item_stock(sender, **kwargs):
    io_item = kwargs['instance']
    if io_item.pk: 
        Item.objects.filter(pk = io_item.category_id).update(current_stock = F('current_stock') - io_item.quantity)
        ItemDetails.objects.filter(pk = io_item.sub_category_id).update(stock = F('stock') - io_item.quantity)


