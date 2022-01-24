from rest_framework import viewsets
from notebooks.serializers import NoteBookSerializer
from notebooks.models import NoteBook


class NoteBookViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = NoteBook.objects.all().order_by('name')
    serializer_class = NoteBookSerializer  # Сериализатор для модели