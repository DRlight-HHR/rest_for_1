from django.urls import path
from .views import get_all, get_temp, update_temp

urlpatterns = [
    path('get-all/', get_all.as_view()),
    path('get-temp/', get_temp.as_view()),
    path('update-temp/<int:pk>/', update_temp.as_view())
]
