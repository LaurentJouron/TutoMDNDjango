from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', include('catalog.urls')),
]
