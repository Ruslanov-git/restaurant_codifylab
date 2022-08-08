from django.db.models import Count, F
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from rest.models import Category, Review, Restaurant, Selection, Sale
from rest.permissions import RestaurantPermission
from rest.serializers import RestaurantSerializer, RestaurantDetailSerializer, CategorySerializer, ReviewSerializer, \
    SelectionSerializer, SaleSerializer


class RestaurantView(ModelViewSet):
    serializer_class = RestaurantSerializer
    serializer_classes = {
        'retrieve': RestaurantDetailSerializer
    }
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', ]
    ordering_fields = ['name', 'price', ]
    permission_classes = (RestaurantPermission, )

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['name', ]
    permission_classes = (RestaurantPermission,)

    def get_queryset(self):
        queryset = Category.objects.annotate(
            rest_count=Count('restaurant')
        )
        return queryset


class SelectionView(ModelViewSet):
    serializer_class = SelectionSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['name', ]
    permission_classes = (RestaurantPermission,)

    def get_queryset(self):
        queryset = Selection.objects.annotate(
            restaurants_count=Count('restaurant')
        )
        return queryset


class SaleView(ModelViewSet):
    serializer_class = SaleSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'text', ]
    ordering_fields = ['name', ]
    permission_classes = (RestaurantPermission,)

    def get_queryset(self):
        queryset = Sale.objects.all()
        return queryset


class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'
    permission_classes = (RestaurantPermission,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            rest_id=kwargs.get('rest_pk')
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

