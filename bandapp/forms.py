from django import forms
from .models import Band, Musician, Instrument, Album, Song


class BandForm(forms.ModelForm):
    '''Band model form'''
    class Meta:
        model = Band
        fields = ['band_name','est_since','band_image_url', 'bio']
        labels = {'band_name': 'Band Name','est_since' : "Established Date" , 'band_image_url': "URL Link for Band Image",'bio': 'A Bio or a Tale'}




class AlbumForm(forms.ModelForm):
    '''Album Model form
        Wide album name field with placeholder text for form'''
    album_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter an album title'}))

    class Meta:
        model = Album
        fields = ['album_name','release_date','band', 'musician']
        labels = {'album_name': 'Album Name','release_date' : "Release Date" , 'band': "The Band", 'musician' : 'Modify contributors'}



class ArtistForm(forms.ModelForm):
    '''Artist model form'''
    class Meta:
        model = Musician
        exclude= []



class SongForm(forms.ModelForm):
    '''Song Model form
        Wide Music video url & song title fields with placeholder text for form'''
    music_video_url = forms.URLField(initial = 'https://www.youtube.com/watch?v=Q4SxizAg6bk',  widget = forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder': 'Enter a URL path for a music video'}
        ))
    song_title = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter a song title'}))

    class Meta:
        model = Song
        fields = ['song_title', 'album', 'music_video_url']



class InstrumentForm(forms.ModelForm):
    '''Instrument model form'''
    class Meta:
        model = Instrument
        fields = ['instrument_name', 'image_url']
        labels = {'instrument_name': 'Description', 'image_url': 'URL for image'}
