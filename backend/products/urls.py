from django.urls import path 

from . import views

urlpatterns = [
    path('', views.product_list_create_view), # no slass because we already have one mapped in the main urls
    # path('', views.product_mixin_view), # no slass because we already have one mapped in the main urls
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_delete_view),
    # path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
]