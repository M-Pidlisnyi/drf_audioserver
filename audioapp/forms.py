from django import  forms
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from audioapp.models import Track, Author


class TrackForm(forms.ModelForm):
    #track_file = forms.FileField(widget=forms.FileInput(attrs={'accept': "audio/*"}))
    class Meta:
        model = Track
        fields = ('track_file',)

    def save(self, commit=True):
        """
            override save method to parse author name and song title
            from filename and save them to database

            returns saved instance
        """
        instance = self.instance
        file = self.cleaned_data['track_file']

        # get song info by parsing filename
        #    split 'author - song .mp3' into ['author - song' ,'mp3']
        filename, ext = file.name.split(".")

        #    split 'author - song' into ['author', 'song']
        author_name = filename.split("-")[0].strip().capitalize()
        song_title= filename.split("-")[1].strip().capitalize()

        author, is_new = Author.objects.get_or_create(name=author_name)
        instance.author = author
        instance.title = song_title

        if commit:
            instance.save()

        return instance