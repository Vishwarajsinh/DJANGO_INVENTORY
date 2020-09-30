from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *

class SubCategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UnitViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class UnitGroupViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = UnitGroup.objects.all()
    serializer_class = UnitGroupSerializer

class ItemDetailViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = ItemDetails.objects.all()
    serializer_class = ItemDetailSerializer

class ItemViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PurchaseOrderItemViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer

class PurchaseBillViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = PurchaseBill.objects.all()
    serializer_class = PurchaseBillSerializer

class IssueOrderItemViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = IssueOrderItem.objects.all()
    serializer_class = IssueOrderItemSerializer

class IssueBillViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = IssueBill.objects.all()
    serializer_class = IssueBillSerializer
