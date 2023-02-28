
from django.contrib import admin
from django.urls import path, include
from signin import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('signin.urls'))
]
