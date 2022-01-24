from notebooks.models import NoteBook
from rest_framework import serializers


class NoteBookSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = NoteBook
        # Поля, которые мы сериализуем
        fields = "__all__"