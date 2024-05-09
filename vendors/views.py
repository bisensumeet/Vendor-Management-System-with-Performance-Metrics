from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, UserSerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

class VendorListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_vendor(self, vendor_code):
        try:
            return Vendor.objects.get(vendor_code=vendor_code)
        except Vendor.DoesNotExist:
            raise Http404("Vendor does not exist")

    def get(self, request, vendor_code):
        vendor = self.get_vendor(vendor_code)
        if vendor:
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, vendor_code):
        vendor = self.get_vendor(vendor_code)
        if vendor:
            serializer = VendorSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, vendor_code):
        vendor = self.get_vendor(vendor_code)
        if vendor:
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class VendorPerformanceAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, vendor_code):
        try:
            vendor = Vendor.objects.get(vendor_code=vendor_code)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=404)

        # Calculate performance metrics
        performance_metrics = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate
        }
        # Create a new entry in HistoricalPerformance

        HistoricalPerformance.objects.create(
            vendor=vendor,
            date=timezone.now(),
            **performance_metrics
        )

        return Response(performance_metrics)

class PurchaseOrderListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, po_number):
        try:
            return PurchaseOrder.objects.get(po_number=po_number)
        except PurchaseOrder.DoesNotExist:
            raise Http404("PurchaseOrder does not exist")

    def get(self, request, po_number):
        purchase_order = self.get_object(po_number)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def put(self, request, po_number):
        purchase_order = self.get_object(po_number)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, po_number):
        purchase_order = self.get_object(po_number)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AcknowledgmentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, po_number):
        try:
            purchase_order = PurchaseOrder.objects.get(po_number=po_number)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=404)

        # Update acknowledgment_date
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()

        # Trigger recalculation of average_response_time
        vendor = purchase_order.vendor
        vendor.update_average_response_time()

        return Response({"message": "Purchase Order acknowledged successfully"})
    
class UserRegistrationAPIView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)