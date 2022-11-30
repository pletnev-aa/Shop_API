from datetime import datetime

from django.db.models import Q

from shop.models import Address, City, Shop


def save_shop(data):
    difference_time = check_time_difference(
        opening_time=data['opening_time'],
        closing_time=data['closing_time']
    )
    if difference_time:
        city = get_city(data['city'])
        address = get_address(
            street=data['street'],
            number=data['number'],
            city=city
        )
        shop = get_shop(
            name=data['name'],
            address=address,
            opening_time=data['opening_time'],
            closing_time=data['closing_time']
        )
        return shop.id


def get_city(name):
    if not City.objects.filter(name=name).exists():
        City.objects.create(name=name)
    return City.objects.get(name=name)


def get_address(street, number, city):
    if not Address.objects.filter(name=street, city=city, number=number).exists():  # noqa: E501
        Address.objects.create(name=street, city=city, number=number)
    return Address.objects.get(name=street, city=city, number=number)


def get_shop(name, address, opening_time, closing_time):
    if not Shop.objects.filter(name=name, address=address).exists():
        Shop.objects.create(
            name=name,
            address=address,
            opening_time=opening_time,
            closing_time=closing_time
        )
    return Shop.objects.get(name=name, address=address)


def get_filtered_shops(filters):
    city = filters.get('city')
    street = filters.get('street')
    open = filters.get('open')
    shops = Shop.objects.all()
    if city:
        city = City.objects.get(name=city)
        shops = shops.filter(address__city=city.id)
    if street:
        shops = shops.filter(address__name=street)
    if open is not None:
        shops = is_open(open, shops)
    return shops


def is_open(parametr, shops):
    try:
        if int(parametr) == 1:
            shops = shops.filter(
                opening_time__lte=datetime.now().time(),
                closing_time__gt=datetime.now().time()
            )
        elif int(parametr) == 0:
            shops = shops.filter(
                Q(opening_time__gt=datetime.now().time()) |
                Q(closing_time__lte=datetime.now().time())
            )
        return shops
    except ValueError as e:
        raise ValueError('OPEN parameter must be a number: 0/1') from e


def check_time_difference(opening_time, closing_time):
    opening_time = datetime.strptime(opening_time, '%H:%M').time()
    closing_time = datetime.strptime(closing_time, '%H:%M').time()
    if opening_time < closing_time:
        return True
    raise ValueError(
        'The opening time cannot be later than the closing time'
    )
