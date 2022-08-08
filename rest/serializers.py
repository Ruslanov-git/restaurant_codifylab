from rest_framework import serializers
from rest.models import Category, Selection, Sale, Restaurant, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'restaurant': {'read_only': True}
        }


class CategorySerializer(serializers.ModelSerializer):
    rest_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['name', ]


class SelectionSerializer(serializers.ModelSerializer):
    restaurants_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Selection
        fields = ['name', 'image', 'restaurants_count', ]


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ['time_create', 'time_update', 'name', 'image', 'text', ]


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['name', 'image', 'phone_number_1',
                  'address', ]


class RestaurantDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'image', 'phone_number_1', 'phone_number_2', 'phone_number_3',
                  'address', 'openning_times', 'menu_image', 'reviews', ]
