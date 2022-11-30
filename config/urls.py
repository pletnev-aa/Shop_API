from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import path

from callback import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/city/', api.customer_get_cities),
    path('api/city/<int:pk>/addresses/', api.customer_get_address),
    path('api/shop/', api.customer_get_shops)
]


if settings.DEBUG:
    urlpatterns += static('static/', views.serve)
