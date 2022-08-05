from accounts.models import *
from django.db import models


class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user')
    general_manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='general_manager')
    hotel_name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True, unique=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    brand_colour = models.CharField(max_length=255, null=True, blank=True)
    cover_image = models.CharField(max_length=500, null=True, blank=True)


class Company(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.CharField(max_length=500, null=True, blank=True)
    owner = models.CharField(max_length=255, null=True, blank=True)
    subdomain = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Menu(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=500, null=True, blank=True)
    time_scheduling = models.BooleanField(default=False)
    earnings = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    item_stock = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class MenuCategory(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


# class Sliders(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     image = models.ImageField()
#     heading = models.CharField(max_length=100)
#     description = models.TextField()
#     link = models.URLField(max_length=10000)
#     orders = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)


# class Profile(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     user = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     destination = models.CharField(max_length=255)
#     type = models.CharField(max_length=255)


# class Guests(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     phone_number = models.BigIntegerField()


# class Coupons(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=255)
#     discount_type = models.CharField(max_length=255)
#     discount_amt = models.CharField(max_length=100)
#     valid_till = models.DateTimeField()
#     max_usage = models.IntegerField()
#     min_subtotal = models.CharField(max_length=255)
#     sub_text = models.TextField(max_length=1000)
#     type = models.CharField(max_length=255)
#     is_active = models.BooleanField()


# class Order(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     guest = models.ForeignKey(Guests, on_delete=models.CASCADE)
#     orders = models.ForeignKey(Coupons, on_delete=models.CASCADE)


class AddonCategory(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class AddonItem(models.Model):
    addon_category = models.ForeignKey(AddonCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Items(models.Model):
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=55, null=True, blank=True)
    disc_price = models.DecimalField(decimal_places=2, max_digits=55, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True, blank=True)
    addon_category = models.ForeignKey(AddonCategory, on_delete=models.CASCADE, null=True, blank=True)
    is_veg = models.BooleanField()
    is_recommended = models.BooleanField()
    is_popular = models.BooleanField()
    is_new = models.BooleanField()
    is_quick_link = models.BooleanField(default=False)
    is_uploaded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


# Standard Model
class Standard(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


# Room Model
Room_Choices = (('room', 'Room'), ('table', 'Table'))


class Room(models.Model):
    resident = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, null=True, blank=True)
    room_number = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, choices=Room_Choices, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Guests(models.Model):
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    # room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    phone = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    tag_along_guests = models.CharField(max_length=100, null=True, blank=True)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # wallet_amount = models.IntegerField(null=True, blank=True)
    # identity_proof = models.CharField(max_length=100, null=True, blank=True)



# class Room_service(models.Model):
#     room = models.ForeignKey(Company, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     company = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)
