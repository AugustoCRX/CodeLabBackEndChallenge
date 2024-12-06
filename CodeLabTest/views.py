from rest_framework import viewsets
from CodeLabTest.serializers import CarrerSerializer
from CodeLabTest.models import Career
# Create your views here.

class CarrersView(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CarrerSerializer
    