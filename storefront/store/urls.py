from django.urls import path
from store import views
urlpatterns = [
    # path('products/', views.product_list),
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProductDetail.as_view()),
    # path('products/<int:id>/', views.product_detail),
    path('collections/', views.collection_list),
    path('collection/<int:pk>/', views.collection_detail, name='collection-detail')
]
