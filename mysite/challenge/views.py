from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Challenge, ChallengeAttempt

# Create your views here.

class ChallengeView(DetailView):
    model = Challenge
    template_name = "challenge/challenge.html"

class ChallengeListView(ListView):
    model = Challenge
    template_name = "challenge/challenge_list.html"
    
def submit_challenge(request, pk):
    if request.method == "POST":
        print("hello world")
        print(request.POST)
        return redirect('/')
    else:
        return ridrect('/challenge/pk')