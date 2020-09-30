from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'sub_categories', SubCategoryViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'units_groups', UnitGroupViewSet)
router.register(r'units', UnitViewSet)
router.register(r'items_details', ItemDetailViewSet)
router.register(r'items', ItemViewSet)
router.register(r'po_items', PurchaseOrderItemViewSet)
router.register(r'po_bill', PurchaseBillViewSet)
router.register(r'io_items', IssueOrderItemViewSet)
router.register(r'io_bill', IssueBillViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]