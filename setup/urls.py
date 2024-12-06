from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from CodeLabTest.views import  CarrersView

router = routers.DefaultRouter()
router.register('career', CarrersView, basename='Carrers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
