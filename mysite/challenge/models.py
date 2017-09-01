from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model, CharField, DateField, TextField, IntegerField, ForeignKey, \
OneToOneField, ManyToManyField

class Challenge(models.Model):
    title = CharField(max_length=140)
    subject = ForeignKey("Subject")
    body = TextField(null=True)

class Subject(models.Model):
    name = CharField(max_length=30)

class StudentProfile(models.Model):
    user = OneToOneField(User)
    subjects = ManyToManyField(Subject)

class ChallengeAttempt(models.Model):
    student = ForeignKey(StudentProfile)
    challenge = ForeignKey(Challenge)
    date = DateField(auto_now=True)