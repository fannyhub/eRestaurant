from django.urls import path

from .views import (MenuSortedById, MenuSortedByDishes, MenuSortedByName,
                    MenuDetailView)

app_name = 'menu'

urlpatterns = [
    path('menus/by_dish_number/', MenuSortedByDishes.as_view(),
         name="menu-by-dishes"),
    path('menus/by_name/', MenuSortedByName.as_view(), name='menu-by-name'),
    path('menus/<int:pk>/', MenuDetailView.as_view(), name="menu-detail"),
    path('menus/', MenuSortedById.as_view(), name="menu-by-id")
]
