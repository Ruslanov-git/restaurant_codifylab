from rest_framework import serializers
from rest.models import Category, Selection, Sale, Restaurant, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'restaurant': {'read_only': True}
        }


class CategorySerializer(serializers.ModelSerializer):
    rest_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'rest_count', ]


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
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'image', 'phone_number_1',
                  'address', ]


class RestaurantDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    menu_image = serializers.ImageField(read_only=True)
    review = ReviewSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'image', 'phone_number_1', 'phone_number_2', 'phone_number_3',
                  'address', 'openning_times', 'menu_image', 'review', ]
