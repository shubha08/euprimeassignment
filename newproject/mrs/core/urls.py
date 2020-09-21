from django.urls import path, include
from rest_framework.authtoken import views
from .views import home,row

urlpatterns = [
    path('', home, name='core.home'),
    path('row/',row, name='core.row')
    ]
