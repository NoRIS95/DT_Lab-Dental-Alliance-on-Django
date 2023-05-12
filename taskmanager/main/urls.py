from django.urls import path
from . import  views

urlpatterns = [
    path('price', views.price_info, name="price"),
    path("about-us", views.about, name="about")

]
