from django.shortcuts import render
from rest_framework import viewsets
from Factory.models import Manufacturers, Details
from Factory.serializers import ManSerializer, DetSerializer


def index(request):
    return render(request, 'index.html')


class ManViewSet(viewsets.ModelViewSet):
    queryset = Manufacturers.objects.all().order_by("name_man")
    serializer_class = ManSerializer


class DetViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all().order_by("name_det")
    serializer_class = DetSerializer


def report(request):
    return render(request, 'report.html', {'data': {'details': Details.objects.select_related('mans')}})
