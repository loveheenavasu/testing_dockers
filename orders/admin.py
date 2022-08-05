from django.contrib import admin
from orders.models import *
admin.site.register(Affiliate)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderItem)
