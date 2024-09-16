from django import  forms
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from audioapp.models import Track, Author
import os
from django.conf import  settings

class TrackForm(forms.ModelForm):
    """
        Form with a single file input field for creating a new track record in the database.
        Author name and song title are parse from filename,
        no two files with the same name are allowed.
        Allowed extensions are '.opus', '.flac', '.webm',
                              '.weba', '.wav', '.ogg',
                              '.m4a', '.oga', '.mid',
                              '.mp3', '.aiff', '.wma', '.au'
    """
    track_file = forms.FileField(widget=forms.FileInput(attrs={'accept': "audio/*"}))
    class Meta:
        model = Track
        fields = ('track_file', )


    def clean_track_file(self):
        """
            checks if the file has valid extension
            and whether the file already exists
        """
        track_file = self.cleaned_data['track_file']
        allowed_extensions = ('.opus', '.flac', '.webm',
                              '.weba', '.wav', '.ogg',
                              '.m4a', '.oga', '.mid',
                              '.mp3', '.aiff', '.wma', '.au')

        if not any(track_file.name.endswith(ext) for ext in allowed_extensions ):
            raise ValidationError("File extension not allowed")

        media_root = settings.MEDIA_ROOT
        upload_to = Track._meta.get_field('track_file').upload_to

        # either django or windows replaces whitespaces with underscores when saving file to filesystem,
        # so we have to preemptively change filename
        track_file_path = os.path.join(media_root, upload_to, track_file.name.replace(' ', '_'))
        print(os.path.isfile(track_file_path))
        if os.path.isfile(track_file_path):
            raise ValidationError("File already exists")


        return track_file



    def save(self, commit=True):
        """
            override save method to parse author name and song title from filename and save them to database

            returns saved instance
        """
        instance = self.instance
        file = self.cleaned_data['track_file']

        # get song info by parsing filename
        #    split 'author - song .mp3' into ['author - song' ,'mp3']
        filename, ext = file.name.split(".")

        #    split 'author - song' into ['author', 'song']
        author_name = filename.split("-")[0].strip().lower().capitalize()
        song_title= filename.split("-")[1].strip().lower().capitalize()

        author, is_new = Author.objects.get_or_create(name=author_name)
        instance.author = author
        instance.title = song_title

        if commit:
            instance.save()

        return instance