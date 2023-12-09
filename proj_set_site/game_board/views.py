from django.shortcuts import render
from .models import Card, PlayPosition
from django.urls import reverse
from django.http import HttpResponseRedirect

import random


# Create your views here.

def create_game(request):
    #num_points_on_cards = settings['num_points_on_cards']
    #num_cards_in_play = settings['num_cards_in_play']
    num_points_on_cards, num_cards_in_play = 6,7

    #create deck of cards
    for i in range(1,2**num_points_on_cards):
        n = i 
        point_str = ''
        while n > 0:
            point_str += str(n % 2)
            n //= 2
        point_str = point_str.ljust(6, '0')  # Add trailing zeros
        card = Card(points = point_str, loc = 'deck', selected = False)
        card.save()
    
    #create empty play positions
    for i in range(num_cards_in_play):
        pos = PlayPosition(pos_id=i)
        pos.save()
    
    _fill_empty_pos()

    return HttpResponseRedirect(reverse("game_board:board"))

    
def render_board(request):
    play_positions = PlayPosition.objects.all()
    deck_size = Card.objects.filter(loc='deck').count()

    context = {'play_positions':play_positions, 'deck_size':deck_size}
    return render(request, 'game_board/board.html', context)

def _fill_empty_pos():
    empty_positions = PlayPosition.objects.filter(card__isnull=True)
    if not empty_positions:
        return
    cards_in_deck = Card.objects.filter(loc='deck')
    cards_on_top = random.choices(cards_in_deck, k=len(empty_positions))

    for pos, card_on_top in zip(empty_positions, cards_on_top):
        pos.card = card_on_top
        card_on_top.loc = 'play'
        pos.save()
        card_on_top.save()

def card_selected(request, card_id):
    card = Card.objects.get(id=card_id)
    card.selected = not card.selected
    card.save()
    return HttpResponseRedirect(reverse("game_board:board"))

class cardFactory:
    def render(request, context):
        return render(request, 'game_board/card_display.html', context)