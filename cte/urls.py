from django.urls import path
from .views import ctes_list

urlpatterns = [
    path('list/', ctes_list),
]