from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('store/<str:pk>/', views.store_detail, name='store-detail'),
    path('profile/<str:pk>/', views.profile, name='user-profile'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register')
]