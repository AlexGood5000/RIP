from django.contrib import admin
from django.urls import include, path
from Factory.views import ManViewSet, DetViewSet
import Factory.views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Manufacturer', ManViewSet)
router.register(r'Detail', DetViewSet)

urlpatterns = [
path('', include(router.urls)),
path('admin/', admin.site.urls),
path('report/', Factory.views.report),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]