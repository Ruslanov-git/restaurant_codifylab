from django.db.models import Count
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from rest.models import Category, Review
from rest.permissions import RestaurantPermission
from rest.serializers import RestaurantSerializer, RestaurantDetailSerializer, CategorySerializer, ReviewSerializer


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.annotate(
            rest_count=Count('restaurant')
        )
        return queryset


class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'
