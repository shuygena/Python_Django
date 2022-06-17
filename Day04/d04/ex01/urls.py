from django.urls import path
from . import views
urlpatterns = [
    path('django', views.django, name="ex01/django"),
    path('display', views.display, name="ex01/base"),
    path('templates', views.templates, name="ex01/templates")
    ]