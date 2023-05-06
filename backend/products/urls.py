from django.urls import path 

from . import views

urlpatterns = [
    path('', views.product_create_view), # no slass because we already have one mapped in the main urls
    path('<int:pk>/', views.ProductDetailAPIView.as_view())
]