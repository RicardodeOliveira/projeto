from django.urls import path
from .views import ctes_list
from .views import ctes_new
from .views import ctes_update
from .views import ctes_delete

urlpatterns = [
    path('list/', ctes_list, name="ctes_list"),
    path('new/', ctes_new, name="ctes_new"),
    path('update/<int:id>/', ctes_update, name="ctes_update"),
    path('delete/<int:id>/', ctes_delete, name="ctes_delete"),
]