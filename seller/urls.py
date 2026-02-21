from django.urls import path,include
from . import views
urlpatterns = [
    # path('', views.home, name='home'),
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'), 
    path('seller_password_change/', views.password_change_view, name='seller_password_change'),
]
