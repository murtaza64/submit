from django.conf.urls import url
from .views import submit_challenge, ChallengeListView, deadline_missed
from django.contrib.auth import views as auth_views
from .models import Challenge
from django.shortcuts import render

urlpatterns = [
    url(r"^challenge/(?P<pk>\d+)/?", submit_challenge, name="challenge"),
    url(r"^submit/(?P<pk>\d+)/?", submit_challenge, name="submit"),
    url(r"^$", ChallengeListView.as_view(), name="list"),
    url(r'^login/?$', auth_views.login, 
        {
        'template_name': 'challenge/login.html'
        }
    ),
    url(
        r"^error/deadline_missed/?$",
        deadline_missed,
        name="deadline_missed"
    )
]