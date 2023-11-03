from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('api/posts/', include('apps.posts.urls')),
    path('api/category/', include('apps.category.urls')),
    path('admin/', admin.site.urls),
]