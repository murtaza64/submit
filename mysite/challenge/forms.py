from django import forms

class ChallengeAttemptForm(forms.Form):
    solution = forms.CharField(label="Solution", required=False)
    answer = forms.CharField(label="Answer", max_length=140, required=False)