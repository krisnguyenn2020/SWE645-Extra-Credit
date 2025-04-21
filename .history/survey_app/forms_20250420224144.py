from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'  # or list the fields you want to include
