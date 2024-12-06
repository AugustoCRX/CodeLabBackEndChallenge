from rest_framework import serializers
from CodeLabTest.models import Career

class CarrerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
