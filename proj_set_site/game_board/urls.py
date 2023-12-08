from django.urls import path
from . import views

app_name = "game_board"
urlpatterns = [
    #path("<int:num_points_on_card>/<int:num_cards_in_play>", views.create_game, name="create_game"),
    path("create_game/", views.create_game, name="create_game"),
    path("", views.render_board, name="board"),
    path("<int:card_id>/select/", views.card_selected, name="card_selected"),
]