from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Vendor, PurchaseOrder

@receiver(post_save, sender=PurchaseOrder)
def update_on_time_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        completed_orders_count = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
        on_time_delivery_orders_count = PurchaseOrder.objects.filter(vendor=vendor, status='completed', delivery_date__lte=instance.delivery_date).count()
        on_time_delivery_rate = on_time_delivery_orders_count / completed_orders_count if completed_orders_count > 0 else 0
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_avg(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.quality_rating is not None:
        vendor = instance.vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            avg_rating = sum([order.quality_rating for order in completed_orders if order.quality_rating is not None]) / total_completed_orders
            vendor.quality_rating_avg = avg_rating
            vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, **kwargs):
    if instance.acknowledgment_date is not None:
        vendor = instance.vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            total_response_time = sum([(order.acknowledgment_date - order.issue_date).total_seconds() for order in completed_orders])
            avg_response_time = total_response_time / total_completed_orders
            vendor.average_response_time = avg_response_time
            vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_fulfilment_rate(sender, instance, created, **kwargs):
    if not created:  # Check if the instance is being updated
        vendor = instance.vendor
        total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
        fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
        if total_orders > 0:
            fulfilment_rate = fulfilled_orders / total_orders
            vendor.fulfillment_rate = fulfilment_rate
            vendor.save()