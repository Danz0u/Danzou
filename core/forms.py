from django import forms
from django.forms import ModelForm
from .models import *


class RelatedBugForm(ModelForm):

    class Meta:
        model = RelatedBugs

        fields = '__all__'
