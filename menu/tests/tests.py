from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from menu.models import Dish, Menu

MENU_LIST_BY_NAME = "menu:menu-by-name"
MENU_LIST_BY_DISHES = "menu:menu-by-dishes"
MENU_LIST_BY_ID = "menu:menu-by-id"
MENU_BASENAME = "menu:menu-detail"


class RestaurantAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data1 = dict(
            name="dish 1",
            description="lorem ipsum", price=20.50, preparation_time=15
        )
        self.data2 = dict(
            name="dish 2",
            description="dolor si amet", price=42.00, preparation_time=42
        )
        self.data3 = dict(
            name="dish 3",
            description="consectetur adipiscing elit", price=17.76,
            preparation_time=25
        )
        self.dish1 = Dish.objects.create(**self.data1)
        self.dish2 = Dish.objects.create(**self.data2)
        self.dish3 = Dish.objects.create(**self.data3)
        self.data4 = dict(
            name="zzz",
            description="z y x w v u t s r p o n m")
        self.data5 = dict(
            name="aaa",
            description="a b c d e f g h i j k l")
        self.data6 = dict(
            name="bbb",
            description="b c d e f g h i j k l m")
        self.data7 = dict(
            name="empty",
            description="empty menu")

        self.menu1 = Menu.objects.create(**self.data4)
        self.menu1.dishes.add(self.dish1, self.dish2)
        self.menu2 = Menu.objects.create(**self.data5)
        self.menu2.dishes.add(self.dish2)
        self.menu3 = Menu.objects.create(**self.data6)
        self.menu3.dishes.add(self.dish1, self.dish2, self.dish3)
        self.menu4 = Menu.objects.create(**self.data7)

    def test_retrieving_all_menus(self):
        res = self.client.get(reverse(MENU_LIST_BY_ID))
        assert res.status_code == status.HTTP_200_OK
        assert len(res.data.get("results")) == 3
        item1, item2, item3 = res.json().get("results")

        assert item1["name"] == self.menu1.name
        assert item2["name"] == self.menu2.name
        assert item3["name"] == self.menu3.name

    def test_getting_menus_sorted_by_name(self):
        res = self.client.get(reverse(MENU_LIST_BY_NAME))
        assert res.status_code == status.HTTP_200_OK
        assert len(res.data.get("results")) == 3
        item1, item2, item3 = res.json().get("results")

        assert item1["name"] == self.menu2.name
        assert item2["name"] == self.menu3.name
        assert item3["name"] == self.menu1.name

    def test_getting_menus_sorted_by_dish_number(self):
        res = self.client.get(reverse(MENU_LIST_BY_DISHES))
        assert res.status_code == status.HTTP_200_OK
        assert len(res.data.get("results")) == 3
        item1, item2, item3 = res.json().get("results")

        assert item1["name"] == self.menu3.name
        assert item2["name"] == self.menu1.name
        assert item3["name"] == self.menu2.name

    def test_retrieving_one_menu(self):
        res = self.client.get(reverse(MENU_BASENAME,
                                      kwargs={"pk": self.menu1.pk}))
        assert res.status_code == status.HTTP_200_OK
        item1 = res.json()
        assert item1['name'] == self.menu1.name
        self.assertEqual(item1["dishes"][0]["description"],
                         self.menu1.dishes.get(pk=self.dish1.id).description)
