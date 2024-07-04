from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProductView.as_view()),
    path('<int:pk>/', views.ProductDetailView.as_view()),
    path('product-images/', views.ProductImageView.as_view()),
    path('categories/<slug:category_slug>/products/', views.ProductByCategoryView.as_view()),
    path('categories/', views.CaregoriesView.as_view())
]