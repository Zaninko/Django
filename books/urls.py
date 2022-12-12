
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]

# MVC (M - model, V - view, C - command)
# MTV (M - model, T - template, V - command(views))















