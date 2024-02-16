from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from crudapp.views import ClientViewSet, RequestViewSet, OperatorViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'operators', OperatorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
