from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import VendorListAPIView, VendorDetailAPIView, PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView, VendorPerformanceAPIView, AcknowledgmentAPIView, UserRegistrationAPIView

urlpatterns = [
    # Vendor URLs
    path('api/vendors/', VendorListAPIView.as_view(), name='vendor-list'),
    path('api/vendors/<str:vendor_code>/', VendorDetailAPIView.as_view(), name='vendor-detail'),
    path('api/vendors/<str:vendor_code>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),

    # Purchase Order URLs
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchaseorder-list-create'),
    path('api/purchase_orders/<str:po_number>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchaseorder-retrieve-update-destroy'),
    path('api/purchase_orders/<str:po_number>/acknowledge/', AcknowledgmentAPIView.as_view(), name='acknowledge-purchase-order'),

    # Token URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='user_register'),
]
