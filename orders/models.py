from main_app.models import *


class Affiliate(models.Model):
    pass


class Coupon(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    discount_type = models.CharField(max_length=100, null=True, blank=True)
    discount_amount = models.IntegerField(null=True, blank=True)
    valid_till = models.DateTimeField(null=True, blank=True)
    max_usage = models.IntegerField(null=True, blank=True)
    min_subtotal = models.IntegerField(null=True, blank=True)
    subtext = models.TextField(max_length=300, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Order(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)
    guest = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

