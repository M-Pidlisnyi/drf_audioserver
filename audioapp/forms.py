from django import forms

from audioapp.models import Track


class TrackForm(forms.Form):
    file_upload = forms.FileField(widget=forms.FileInput(attrs={'accept': 'audio/*'}))