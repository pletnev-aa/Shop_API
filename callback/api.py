import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import status

from service import db
from shop.models import Address, City

from .serializers import (AddressSerializer, CitySerializer,
                          SaveShopSerializer, ShopSerializer)


@require_http_methods(['GET'])
def customer_get_cities(request):
    cities = CitySerializer(
        City.objects.all(),
        many=True
    ).data
    return JsonResponse(
        {
            'cities': cities
        }
    )


@require_http_methods(['GET'])
def customer_get_address(request, pk):
    addresses = AddressSerializer(
        Address.objects.filter(city=pk),
        many=True
    ).data
    return JsonResponse(
        {
            'addresses': addresses,
        }
    )


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def customer_get_shops(request):
    if request.method == 'POST':
        serializer = SaveShopSerializer(
            data=json.loads(request.body)
        )
        try:
            if serializer.is_valid():
                shop = db.save_shop(serializer.data)
                return JsonResponse(
                    {
                        'id': shop,
                        'status': status.HTTP_200_OK
                    }
                )
        except Exception as e:
            return JsonResponse(
                {
                    'message': f'Error: {e}',
                    'status': status.HTTP_400_BAD_REQUEST
                },
                status=400
            )
    if request.method == 'GET':
        try:
            shops = db.get_filtered_shops(request.GET)
            shops = ShopSerializer(
                shops,
                many=True
            ).data
            return JsonResponse(
                {
                    'shops': shops,
                    'status': status.HTTP_200_OK
                }
            )
        except Exception as e:
            return JsonResponse(
                {
                    'message': f'Error: {e}',
                    'status': status.HTTP_400_BAD_REQUEST
                },
                status=400
            )
