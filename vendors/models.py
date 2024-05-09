from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, primary_key=True)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)
    
    def update_fulfilment_rate(self):
        total_orders = PurchaseOrder.objects.filter(vendor=self).count()
        print('Tot- ',total_orders)
        fulfilled_orders = PurchaseOrder.objects.filter(vendor=self, status='completed').count()
        print('Ful- ', fulfilled_orders)
        if total_orders > 0:
            fulfilment_rate = fulfilled_orders / total_orders
            self.fulfillment_rate = fulfilment_rate
            self.save()
    
    def update_average_response_time(self):
        completed_orders = PurchaseOrder.objects.filter(vendor=self, acknowledgment_date__isnull=False)
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            total_response_time = sum([(order.acknowledgment_date - order.issue_date).total_seconds() for order in completed_orders])
            avg_response_time = total_response_time / total_completed_orders
            self.average_response_time = avg_response_time
            self.save()


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)