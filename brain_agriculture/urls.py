from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from brain_agriculture.farmers import views as farmers_view


router = DefaultRouter(trailing_slash=False)
router.register('city', farmers_view.CityViewSet, basename='city')
router.register('culture', farmers_view.CityViewSet, basename='culture')
router.register('farmer', farmers_view.CityViewSet, basename='farmer')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("rest_framework.urls")),
] + router.urls

