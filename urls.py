from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # enables browsable API of DRF
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('django_rest_demo.api.urls')),
]
