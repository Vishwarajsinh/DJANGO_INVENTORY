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


class ItemSerializer(serializers.ModelSerializer):
    unit = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = [
            "id", "name", "decs", "category", "category_id", "current_stock", "unit", "created_at", "updated_at",
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
        fields = [
            "bill_no",
            "category",
            "quantity",
            "mrp_per_unit",
        ]

class PurchaseBillSerializer(serializers.ModelSerializer):
    bill_items = PurchaseOrderItemSerializer(many = True, read_only=True)

    class Meta:
        model = PurchaseBill
        fields = [
            "id",
            "bill_no",
            "notes",
            "purchased_at",
            "bill_items",
        ]

class IssueBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBill
        fields = [
            "bill_no",
            "item",
            "id",
            "quantity",
            "issued_at",
        ]