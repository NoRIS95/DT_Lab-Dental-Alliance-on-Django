from django import forms
from .models import Task, About
from django.forms import ModelForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = "__all__"