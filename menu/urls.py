from django.urls import path
from django.views.generic import TemplateView


app_name = "menus"

urlpatterns = [
    path('', TemplateView.as_view(template_name="menu_list.html"))

]
