from django.urls import path, include
from rest.views import ReviewView, RestaurantView, CategoryView, SelectionView, SaleView

urlpatterns = [
    path('', RestaurantView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', RestaurantView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('category/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('category/<int:pk>/', CategoryView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('selection/', SelectionView.as_view({'get': 'list', 'post': 'create'})),
    path('selection/<int:pk>/', CategoryView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('sale/', SaleView.as_view({'get': 'list', 'post': 'create'})),
    path('sale/<int:pk>/', SaleView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('<int:product_pk>/review/create', ReviewView.as_view({'get': 'list', 'post': 'create'})),
]
