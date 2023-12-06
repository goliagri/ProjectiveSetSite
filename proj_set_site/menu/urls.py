from django.urls import path
from . import views

app_name = "menu"
urlpatterns = [
    path("", views.main_menu, name="main_menu"),
    path("start_game/", views.start_game, name="start_game"),
]