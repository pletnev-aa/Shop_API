[![Maintainability](https://api.codeclimate.com/v1/badges/9c1d47149e2f4648b1c5/maintainability)](https://codeclimate.com/github/pletnev-aa/Shop_API/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9c1d47149e2f4648b1c5/test_coverage)](https://codeclimate.com/github/pletnev-aa/Shop_API/test_coverage)

## О проекте
Сервис для приема и ответа на HTTP запросы

## Функционал
* В случае успешной обработки сервис отвечает статусом 200
* В случае ошибки - статус 400
* Сохранение объектов в базе данных
* Запросы:
    + GET /city/ - получение всех городов из базы
    + GET /city/<city_id>/addresses/ - получение всех улиц города
    + POST /shop/ - создание магазина. Метод принимает json объект, в ответ возвращает id созданной записи.
    + GET /shop/?street=&city=&open=0/1 - получение списка магазинов
        - метод принимает параметры для фильтрации. Параметры не обязательны. В случае отсутствия выводятся все магазины
        - параметр OPEN: 0 - закрыт, 1 - открыт. Параметр определяется исходя из текущего времени сервера
* Пример принимаего json объекта магазина:
    + Название
    + Город
    + Улица
    + Дом
    + Время открытия
    + Время закрытия
```
{
    "name": "TestShop",
    "city": "TestCity",
    "street": "TestStreet",
    "number": "5",
    "opening_time": "09:00",
    "closing_time": "22:00"
}
```

## Инфраструктура
Для поднятия инфраструктуры использован Docker и Docker-compose
```
- docker-compose --env-file ./.env up --detach --build # поднимет всю инфраструктуру  проекта
- docker ps # отобразит список запущенных контейнеров
- docker exec -ti <container_id> bash # войдет в запущенный контейнер для выполнения команд:
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py createsuperuser
    * python manage.py collectstatic
- проект будет доступен по http://127.0.0.1:8000/
````

## Дисклеймер
.env файл добавлен для возможности локального запуска сервиса
