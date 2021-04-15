from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('', include('posts.urls')), # new
    path('admin/', admin.site.urls),
]
