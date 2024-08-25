from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('store/<str:pk>/', views.store_detail, name='store-detail')
]