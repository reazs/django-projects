
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('novacafee.urls')),
    path('api/', include('novacafee.urls')),
]
