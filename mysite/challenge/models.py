from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model, CharField, DateField, TextField, IntegerField, ForeignKey, \
OneToOneField, ManyToManyField, DateTimeField, BooleanField
import datetime

class Challenge(models.Model):
    title = CharField(max_length=140)
    subject = ForeignKey("Subject")
    body = TextField()
    start = DateTimeField(auto_now_add=True)
    deadline = DateTimeField(default=datetime.datetime(2100,1,1))
    correct_answers = ManyToManyField("Answer")
    auto_check = BooleanField(default=True)
    solution_only = BooleanField(default=False)

class Answer(models.Model):
    value = CharField(max_length=140)

class Subject(models.Model):
    name = CharField(max_length=30)

class StudentProfile(models.Model):
    user = OneToOneField(User)
    subjects = ManyToManyField(Subject)

class ChallengeAttempt(models.Model):
    student = ForeignKey(StudentProfile)
    challenge = ForeignKey(Challenge)
    date = DateField(auto_now_add=True)
    answer = CharField(max_length=140, null=True)
    solution = TextField(null=True)