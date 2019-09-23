from rest_framework.serializers import ModelSerializer

from menu.models import Dish, Menu


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        exclude = ('image',)


class MenuDetailSerializer(ModelSerializer):

    dishes = DishSerializer(many=True, required=False)

    class Meta:
        model = Menu
        fields = '__all__'


class MenuSerializer(ModelSerializer):

    class Meta:
        model = Menu
        exclude = ('dishes',)
