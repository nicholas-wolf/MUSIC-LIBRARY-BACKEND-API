from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_table),
    path('<int:pk>/', views.song_detail)
]     