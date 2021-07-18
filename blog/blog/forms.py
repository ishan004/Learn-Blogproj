from .models import comment
from django import forms

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ("name", "email", "comment_text")
        