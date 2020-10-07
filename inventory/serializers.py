from rest_framework import serializers

from .models import *



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
        fields = [
            'id',
            'name',
            'decs',
            'current_stock',
            'created_at',
            'updated_at',
        ]


class ItemSerializer(serializers.ModelSerializer):
    item_detail = ItemDetailSerializer(many = True, read_only=True)

    class Meta:
        model = Item
        fields = [
            "id", "name", "decs", "category", "current_stock", "created_at", "updated_at", "item_detail",
        ]

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many = True, read_only=True)

    class Meta:
        model = Category
        fields = [
           'id', 'name', 'items',
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