from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Challenge, ChallengeAttempt, StudentProfile
from .forms import ChallengeAttemptForm
import datetime

# Create your views here.

# class ChallengeView(DetailView):
#     model = Challenge
#     template_name = "challenge/challenge.html"

class ChallengeListView(ListView):
    model = Challenge
    template_name = "challenge/challenge_list.html"
    ordering = ['-start']

def deadline_missed(request):
    return render(request, "challenge/deadline_missed.html")

def submit_challenge(request, pk):
    obj = Challenge.objects.get(pk=pk)
    if request.method == "POST":
        if not request.user.is_authenticated: #TODO
            redirect('/login')
        print(request.POST)
        form = ChallengeAttemptForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            att = ChallengeAttempt()
            student = StudentProfile.objects.get(user=request.user)
            att.student = student
            att.challenge = obj
            att.answer = form.cleaned_data['answer']
            att.solution = form.cleaned_data['solution']
            att.save()
            if att.timestamp > obj.deadline:
                att.delete()
                return redirect('/error/deadline_missed')
            return redirect('/') #TODO
    else:
        form = ChallengeAttemptForm()
    return render(request, 'challenge/challenge.html', {'form': form, 'challenge': obj})