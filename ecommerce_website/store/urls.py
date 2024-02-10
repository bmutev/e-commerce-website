from django.urls import path

from . import views

urlpatterns = [
    # Empty string because this is the homepage
    path('', views.store, name='store'),
    path('product/<slug:slug>/', views.product_info, name='product-info'),
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
]
