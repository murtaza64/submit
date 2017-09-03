from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Challenge, ChallengeAttempt
from .forms import ChallengeAttemptForm

# Create your views here.

# class ChallengeView(DetailView):
#     model = Challenge
#     template_name = "challenge/challenge.html"

class ChallengeListView(ListView):
    model = Challenge
    template_name = "challenge/challenge_list.html"
    
def submit_challenge(request, pk):
    obj = Challenge.objects.get(pk=pk)
    if request.method == "POST":
        print(request.POST)
        form = ChallengeAttemptForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('/')
    else:
        form = ChallengeAttemptForm()
    return render(request, 'challenge/challenge.html', {'form': form, 'challenge': obj})