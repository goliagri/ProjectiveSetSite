from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def main_menu(request):
    return render(request, "menu/main_menu.html")

def start_game(request):
    '''
    Interpret the settings to properly initialize the cards and pass to a game board view.
    '''
    settings = {'num_points_on_cards':6,'num_cards_in_play':7}
    return HttpResponseRedirect(reverse("game_board:create_game", args=()))

def open_settings(request):
    pass
    