from rest_framework import serializers

from shop.models import Address, City, Shop


class CitySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='name')

    class Meta:
        model = City
        fields = ['city']


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Address
        fields = ['city', 'name', 'number']


class ShopSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Shop
        fields = ['name', 'address', 'opening_time', 'closing_time']


class SaveShopSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)
    number = serializers.CharField(max_length=20)
    opening_time = serializers.CharField(max_length=5)
    closing_time = serializers.CharField(max_length=5)
