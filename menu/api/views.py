from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Count

from menu.models import Menu
from .serializers import MenuDetailSerializer, MenuSerializer


class MenuView:
    serializer_class = MenuSerializer
    non_empty_menus = Menu.objects.exclude(dishes__isnull=True)

    def get_queryset(self):
        print(type(self.non_empty_menus))
        return self.non_empty_menus


class MenuSortedById(MenuView, ListAPIView):
    pass


class MenuSortedByDishes(MenuView, ListAPIView):
    def get_queryset(self):
        annotated_menus = self.non_empty_menus.annotate(
            dishes_count=Count('dishes'))
        return annotated_menus.order_by('-dishes_count')


class MenuSortedByName(MenuView, ListAPIView):
    def get_queryset(self):
        return self.non_empty_menus.order_by('name')


class MenuDetailView(MenuView, RetrieveAPIView):
    serializer_class = MenuDetailSerializer
