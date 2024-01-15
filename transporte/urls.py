from django.urls import path, include
from .views import index
from django.contrib import admin

urlpatterns = [
    # path('transporte/', include('transporte.urls')),
    path('', index, name="transporte_index"),
    path('admin/', admin.site.urls),
]

