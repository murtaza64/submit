from django.contrib import admin
from .models import StudentProfile, Subject, Answer, Challenge, ChallengeAttempt
# Register your models here.

admin.site.register(StudentProfile)
admin.site.register(Subject)
admin.site.register(Answer)
admin.site.register(Challenge)
admin.site.register(ChallengeAttempt)

