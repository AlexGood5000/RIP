from .models import Manufacturers, Details
from rest_framework import serializers

class ManSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturers
        fields = "__all__"

class DetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = "__all__"