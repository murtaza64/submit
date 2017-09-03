from django.conf.urls import url
from .views import submit_challenge, ChallengeListView

from .models import Challenge

urlpatterns = [
    url(r"^challenge/(?P<pk>\d+)/?", submit_challenge, name="challenge"),
    url(r"^submit/(?P<pk>\d+)/?", submit_challenge, name="submit"),
    url(r"^$", ChallengeListView.as_view(), name="list")

]