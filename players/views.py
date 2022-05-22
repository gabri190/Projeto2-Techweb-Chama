from django.shortcuts import render

# Create your views here.
from .models import Player
from django.shortcuts import render, redirect
from django.http import Http404
import http.client
from get_dados import get_players

# from notes.forms import NoteForm  
from players.models import Player  
# Create your views here.  

def create_note(request):  
    if request.method == 'POST':
        try:
            player_id=request.POST.get('player_id')
            player,created = Player.objects.get_or_create(player_id=player_id)
            if created: 
                    dict = get_players(player_id)
                    print(dict)
                    player.player_id = dict['id']
                    player.first_name = dict['first_name']
                    player.last_name = dict['last_name']
                    player.position = dict['position']
                    player.team = dict['team']["full_name"]
                    player.save()

        except Player.DoesNotExist:
            raise Http404()

        else:  
            all_players=Player.objects.all()
            return render(request,'players/create_player.html',{'players':all_players})  
    else:
        all_players=Player.objects.all()
        return render(request,'players/create_player.html',{'players':all_players})  

def delete_player(request): 
    id=request.POST.get('delete')
    player = Player.objects.get(id=id)  
    player.delete() 
    
    return redirect("create_player")