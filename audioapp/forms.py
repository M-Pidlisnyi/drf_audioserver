from django.forms import  ModelForm

from audioapp.models import Track


class TrackForm(ModelForm):

    class Meta:
        model = Track
        fields = ('track_file',)