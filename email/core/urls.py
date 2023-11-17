from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('api/contacts/', include('apps.contacts.urls')),
    path('admin/', admin.site.urls),
]
