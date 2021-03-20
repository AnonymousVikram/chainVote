from django.shortcuts import render
from .models import Candidates,Election
from django.views.generic import ListView
# Create your views here.

def election_view(request,id):
    election = Election.objects.get(id=id)
    candidate = Candidates.objects.filter(election=election)
    return render(request, "ElectionView.html", {'candidate':candidate})

