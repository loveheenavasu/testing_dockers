from rest_framework import serializers
from .models import *
from .models import Company
from accounts.models import *

# company serializer
class CompanySerializer(serializers.ModelSerializer):
    # role = RoleSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


# class CompanyEditSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = '__all__'


# addon category serializers
class AddonCategoryGetSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = AddonCategory
        fields = '__all__'


class AddonCategoryEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddonCategory
        fields = '__all__'


# addon item serializers
class AddonItemEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddonItem
        fields = '__all__'


class AddonItemGetSerializer(serializers.ModelSerializer):
    addon_category = AddonCategoryGetSerializer(read_only=True)
    class Meta:
        model = AddonItem
        fields = '__all__'


# menu serializers
class MenuGetSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'


class MenuEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


# Menu Category serializers
class MenuCategoryGetSerializer(serializers.ModelSerializer):
    menu = MenuGetSerializer(read_only=True)

    class Meta:
        model = MenuCategory
        fields = '__all__'


class MenuCategoryEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = '__all__'


# item serializers
class ItemsGetSerializer(serializers.ModelSerializer):
    menu = MenuGetSerializer(read_only=True)
    menu_category = MenuCategoryGetSerializer(read_only=True)
    addon_category = AddonCategoryGetSerializer(read_only=True)

    class Meta:
        model = Items
        fields = '__all__'


class ItemsEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = '__all__'


# Standard serializers
class StandardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class StandardEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class UserRoomSerializer(serializers.ModelSerializer):
    """user serializer"""

    class Meta:
        model = User
        exclude = ["password", ]


# Room serializers
class RoomGetSerializer(serializers.ModelSerializer):
    resident = UserRoomSerializer(read_only=True)
    standard = StandardGetSerializer(read_only=True)
    class Meta:
        model = Room
        fields = '__all__'


class RoomEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
