from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token  # Import Token model
from django.contrib.auth.models import User
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, UserSerializer

class VendorAPITests(TestCase):
    def setUp(self):

        # Set up test data
        self.client = APIClient()
        
        # Create a test user
        self.user = User.objects.create_user(username='test_user', password='password123')
        
        # Create authentication token for the test user
        self.token = Token.objects.create(user=self.user)
        
        # Set token in the client's credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        self.vendor_data = {
            "name": "Test Vendor",
            "contact_details": "test@example.com",
            "address": "123 Test St, Testville",
            "vendor_code": "TEST001",
            "on_time_delivery_rate": None,
            "quality_rating_avg": None,
            "average_response_time": None,
            "fulfillment_rate": None
        }

    def test_create_vendor(self):
        # Test creating a new vendor
        response = self.client.post('/api/vendors/', self.vendor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_vendors(self):
        # Test listing all vendors
        Vendor.objects.create(**self.vendor_data)
        response = self.client.get('/api/vendors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_vendor(self):
        # Create a vendor
        Vendor.objects.create(**self.vendor_data)

        # Test retrieving an existing vendor
        response = self.client.get('/api/vendors/TEST001/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions to check the response data
        

    def test_update_vendor(self):
        # Create a vendor
        Vendor.objects.create(**self.vendor_data)

        # Test updating an existing vendor
        updated_data = {
            "name": "Updated Vendor",
            "contact_details": "9999999999",
            "address": "789 Test Street",
            "vendor_code": "TEST001",
            "on_time_delivery_rate": None,
            "quality_rating_avg": None,
            "average_response_time": None,
            "fulfillment_rate": None
        }
        response = self.client.put('/api/vendors/TEST001/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vendor(self):
        # Create a vendor
        Vendor.objects.create(**self.vendor_data)

        # Test deleting an existing vendor
        response = self.client.delete('/api/vendors/TEST001/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
class PurchaseOrderAPITests(TestCase):
    def setUp(self):
        # Set up test data
        self.client = APIClient()
        
        # Create a test user
        self.user = User.objects.create_user(username='test_user', password='password123')
        
        # Create authentication token for the test user
        self.token = Token.objects.create(user=self.user)
        
        # Set token in the client's credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        self.vendor_data = {
            "name": "Test Vendor",
            "contact_details": "test@example.com",
            "address": "123 Test St, Testville",
            "vendor_code": "TEST001",
            "on_time_delivery_rate": None,
            "quality_rating_avg": None,
            "average_response_time": None,
            "fulfillment_rate": None
        }

        self.vendor = Vendor.objects.create(**self.vendor_data)
        
        self.purchase_order_data = {
            "po_number": "PO001",
            "vendor": self.vendor,
            "order_date": "2024-05-01T10:00:00Z",
            "delivery_date": "2024-05-15T10:00:00Z",
            "items": [
                {"name": "Product A", "price": 10.99, "quantity": 100},
                {"name": "Product B", "price": 20.49, "quantity": 50}
            ],
            "quantity": 150,
            "status": "pending",
            "quality_rating": 4.5,
            "issue_date": "2024-04-30T10:00:00Z",
            "acknowledgment_date": None
        }
        # Additional purchase orders with the same vendor and status pending
        self.purchase_order_data_2 = {
            "po_number": "PO002",
            "vendor": self.vendor,
            "order_date": "2024-04-01T10:00:00Z",  # Adjusted order_date to a past date
            "delivery_date": "2024-04-16T10:00:00Z",
            "items": [
                {"name": "Product C", "price": 15.99, "quantity": 75},
                {"name": "Product D", "price": 30.99, "quantity": 25}
            ],
            "quantity": 100,
            "status": "pending",
            "quality_rating": 4.2,
            "issue_date": "2024-05-01T10:00:00Z",
            "acknowledgment_date": None
        }

        self.purchase_order_data_3 = {
            "po_number": "PO003",
            "vendor": self.vendor,
            "order_date": "2024-05-03T10:00:00Z",
            "delivery_date": "2024-05-17T10:00:00Z",
            "items": [
                {"name": "Product E", "price": 25.99, "quantity": 50},
                {"name": "Product F", "price": 40.99, "quantity": 30}
            ],
            "quantity": 80,
            "status": "pending",
            "quality_rating": 4.8,
            "issue_date": "2024-05-02T10:00:00Z",
            "acknowledgment_date": None
        }
        # Serialize the PurchaseOrder object using a serializer
        purchase_order_serializer = PurchaseOrderSerializer(self.purchase_order_data)
        serialized_purchase_order = purchase_order_serializer.data

        # Use the serialized purchase order data
        self.purchase_order_data_serialized = serialized_purchase_order

        purchase_order_serializer2 = PurchaseOrderSerializer(self.purchase_order_data_2)
        serialized_purchase_order2 = purchase_order_serializer2.data

        # Use the serialized purchase order data
        self.purchase_order_data_serialized2 = serialized_purchase_order2

        purchase_order_serializer3 = PurchaseOrderSerializer(self.purchase_order_data_3)
        serialized_purchase_order3 = purchase_order_serializer3.data

        # Use the serialized purchase order data
        self.purchase_order_data_serialized3 = serialized_purchase_order3
    def test_create_purchase_order(self):
        # Test creating a new purchase order
        response = self.client.post('/api/purchase_orders/', self.purchase_order_data_serialized, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create and test additional purchase orders
        response = self.client.post('/api/purchase_orders/', self.purchase_order_data_serialized2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('/api/purchase_orders/', self.purchase_order_data_serialized3, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_list_purchase_orders(self):
        # Test listing all purchase orders
        PurchaseOrder.objects.create(**self.purchase_order_data)
        PurchaseOrder.objects.create(**self.purchase_order_data_2)
        PurchaseOrder.objects.create(**self.purchase_order_data_3)

        response = self.client.get('/api/purchase_orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_purchase_order(self):
        # Test retrieving a purchase order
        purchase_order = PurchaseOrder.objects.create(**self.purchase_order_data)
        response = self.client.get(f'/api/purchase_orders/{purchase_order.po_number}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_purchase_order(self):
        # Test updating a purchase order
        purchase_order = PurchaseOrder.objects.create(**self.purchase_order_data)
        updated_data = {
            "po_number": "PO001",
            "vendor": self.vendor,
            "order_date": "2024-05-01T10:00:00Z",
            "delivery_date": "2024-05-15T10:00:00Z",
            "items": [
                {"name": "Product A", "price": 10.99, "quantity": 100},
                {"name": "Product B", "price": 20.49, "quantity": 50}
            ],
            "quantity": 150,
            "status": "completed",
            "quality_rating": 4.5,
            "issue_date": "2024-04-30T10:00:00Z",
            "acknowledgment_date": None
        }
        # Serialize the PurchaseOrder object using a serializer
        updated_data_serializer = PurchaseOrderSerializer(updated_data)
        serialized_updated_data = updated_data_serializer.data

        # Use the serialized purchase order data
        self.updated_data_serialized = serialized_updated_data
        response = self.client.put(f'/api/purchase_orders/{purchase_order.po_number}/', self.updated_data_serialized, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions as needed
    
    def test_delete_purchase_order(self):
        # Test deleting a purchase order
        purchase_order = PurchaseOrder.objects.create(**self.purchase_order_data)
        response = self.client.delete(f'/api/purchase_orders/{purchase_order.po_number}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Add more assertions as needed

class VendorPerformanceMetricsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test user
        self.user = User.objects.create_user(username='test_user', password='password123')
        
        # Create authentication token for the test user
        self.token = Token.objects.create(user=self.user)
        
        # Set token in the client's credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        self.vendor_data = {
            "name": "Test Vendor",
            "contact_details": "test@example.com",
            "address": "123 Test St, Testville",
            "vendor_code": "TEST001",
            "on_time_delivery_rate": None,
            "quality_rating_avg": None,
            "average_response_time": None,
            "fulfillment_rate": None
        }

        self.vendor = Vendor.objects.create(**self.vendor_data)
        # Create purchase orders
        self.purchase_order_data = {
            "po_number": "PO001",
            "vendor": self.vendor,
            "order_date": "2024-05-01T10:00:00Z",
            "delivery_date": "2024-05-15T10:00:00Z",
            "items": [
                {"name": "Product A", "price": 10.99, "quantity": 100},
                {"name": "Product B", "price": 20.49, "quantity": 50}
            ],
            "quantity": 150,
            "status": "pending",
            "quality_rating": 4.5,
            "issue_date": "2024-04-30T10:00:00Z",
            "acknowledgment_date": None
        }
        # Additional purchase orders with the same vendor and status pending
        self.purchase_order_data_2 = {
            "po_number": "PO002",
            "vendor": self.vendor,
            "order_date": "2024-04-01T10:00:00Z",  # Adjusted order_date to a past date
            "delivery_date": "2024-04-16T10:00:00Z",
            "items": [
                {"name": "Product C", "price": 15.99, "quantity": 75},
                {"name": "Product D", "price": 30.99, "quantity": 25}
            ],
            "quantity": 100,
            "status": "pending",
            "quality_rating": 4.2,
            "issue_date": "2024-05-01T10:00:00Z",
            "acknowledgment_date": None
        }

        self.purchase_order_data_3 = {
            "po_number": "PO003",
            "vendor": self.vendor,
            "order_date": "2024-05-03T10:00:00Z",
            "delivery_date": "2024-05-17T10:00:00Z",
            "items": [
                {"name": "Product E", "price": 25.99, "quantity": 50},
                {"name": "Product F", "price": 40.99, "quantity": 30}
            ],
            "quantity": 80,
            "status": "pending",
            "quality_rating": 4.8,
            "issue_date": "2024-05-02T10:00:00Z",
            "acknowledgment_date": None
        }
        PurchaseOrder.objects.create(**self.purchase_order_data)
        PurchaseOrder.objects.create(**self.purchase_order_data_2)
        PurchaseOrder.objects.create(**self.purchase_order_data_3)

    def test_performance_metrics_calculation(self):
        # Mark the first two purchase orders as completed
        PurchaseOrder.objects.filter(po_number__in=["PO001", "PO002"]).update(status="completed")

        # Acknowledge PO001 and PO002
        response = self.client.post('/api/purchase_orders/PO001/acknowledge/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post('/api/purchase_orders/PO002/acknowledge/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Calculate performance metrics
        response = self.client.get(f'/api/vendors/{self.vendor_data["vendor_code"]}/performance/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the calculated performance metrics
        # On-Time Delivery Rate
        total_completed_po_count = 2  # Total completed POs for this vendor
        on_time_delivery_count = 1  # Number of completed POs delivered on or before delivery_date
        anticipated_on_time_delivery_rate = on_time_delivery_count / total_completed_po_count
        self.assertAlmostEqual(response.data['on_time_delivery_rate'], anticipated_on_time_delivery_rate)

        # Quality Rating Average
        anticipated_quality_rating_avg = (4.5 + 4.2) / 2  # Average of quality ratings for all completed POs, PO003 is not completed
        self.assertAlmostEqual(response.data['quality_rating_avg'], anticipated_quality_rating_avg)

        # Average Response Time
        # Compute the average response time based on the issue_date and acknowledgment_date of each completed PO
        # Calculate the average response time in seconds
        completed_pos = PurchaseOrder.objects.filter(vendor=self.vendor_data["vendor_code"], status="completed")
        total_response_time_seconds = sum((po.acknowledgment_date - po.issue_date).total_seconds() for po in completed_pos)
        anticipated_average_response_time_seconds = total_response_time_seconds / len(completed_pos)

        self.assertAlmostEqual(response.data['average_response_time'], anticipated_average_response_time_seconds)

        # Fulfilment Rate
        total_po_count = 3  # Total number of POs issued to the vendor
        successful_fulfillment_count = 2  # Number of successfully fulfilled POs
        anticipated_fulfilment_rate = successful_fulfillment_count / total_po_count
        # Verify the calculated performance metrics
        #print('Check ',response.data['fulfillment_rate'])
        if response.data['fulfillment_rate'] is not None:
            self.assertAlmostEqual(response.data['fulfillment_rate'], anticipated_fulfilment_rate)
        else:
            self.assertIsNone(anticipated_fulfilment_rate)  # Ensure anticipated value is None