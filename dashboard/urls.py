from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('learning/', views.learning, name='learning'),
    path('call/', views.call_screen, name='call'),
    path('learning/lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('standby/', views.standby, name='standby'),
]