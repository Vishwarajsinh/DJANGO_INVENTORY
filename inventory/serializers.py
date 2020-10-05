from rest_framework import serializers

from .models import *

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many = True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'name', 'sub_categories',
        ]

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class UnitGroupSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many = True, read_only=True)

    class Meta:
        model = UnitGroup
        fields = [
            'name', 'units',
        ]

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDetails
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    item_detail = ItemDetailSerializer(many = True, read_only=True)

    class Meta:
        model = Item
        fields = [
            "name", "decs", "category",
            "sub_categories", "current_stock", "created_at", "updated_at", "item_detail",
        ]

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'

class PurchaseBillSerializer(serializers.ModelSerializer):
    bill_items = PurchaseOrderItemSerializer(many = True, read_only=True)

    class Meta:
        model = PurchaseBill
        fields = [
            "bill_no",
            "supplier",
            "purchased_at",
            "bill_items",
        ]

class IssueOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueOrderItem
        fields = '__all__'

class IssueBillSerializer(serializers.ModelSerializer):
    issue_items = IssueOrderItemSerializer(many = True, read_only=True)

    class Meta:
        model = IssueBill
        fields = [
            "bill_no",
            "issued_by",
            "issued_at",
            "issue_items",
        ]