from django.urls import path,include
from . import views
urlpatterns = [
    # path('', views.home, name='home'),
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('c_password_change/', views.password_change_view, name='customer_password_change'),
]
