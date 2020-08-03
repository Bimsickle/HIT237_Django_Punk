from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from bandapp.models import Band, Musician, Instrument,  Album, Song
from .forms import BandForm, AlbumForm, SongForm, ArtistForm, InstrumentForm




def home(request):
    '''r'^$', views.home, name = 'home'
        returns the home page'''
    return render(request,'bandapp/index.html')


### BANDS ###

def band_list(request):
    ''' r'^bands/?$', views.band_list, name = 'band_list'
        View the list of all bands '''
    all_bands = Band.objects.order_by('band_name').all()
    context = {
        'bands': all_bands,
        }
    return render(request,'bandapp/band_list.html', context)


def band_detail(request, b_id):
    ''' r'^band/detail/(\d+)?$', views.band_detail, name = 'band_detail'
        detail view for selected band '''
    band = Band.objects.get(id=b_id)
    album = Album.objects.filter(band=b_id).order_by('-release_date')
    context = {
        'band' : band,
        'album' : album,
        }
    return render(request,'bandapp/band_details.html', context)


def band_add(request):
    ''' r'^band/add/?$', views.band_add, name = 'band_add'
        Form to add a new band '''
    if request.method != "POST":
        context = {'band_form': BandForm()}
    else:
        form = BandForm(request.POST)
        if form.is_valid() !=True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'band_form': form,}
        else:
            data = form.cleaned_data
            band = form.save()
            name = data.get('band_name')
            messages.success(request, (f"Successfully added {name} as a Band!"))
            bid = band.id
            return redirect('band_detail', bid)

    return render(request,'bandapp/band_add.html',context)


def band_edit(request, bandid):
    ''' r'^band/edit/(\d+)?$', views.band_edit, name = 'band_edit'
        Form to edit a band '''
    band = Band.objects.get(id = bandid)
    if request.method != "POST":
        context = {'band_form': BandForm(instance = band),
         'band' : band,}
    else:
        form = BandForm(request.POST, instance = band)
        if form.is_valid() !=True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'band_form': form,}
        else:
            band = form.save()
            name = band.band_name
            messages.success(request, (f"Successfully updated the band {name}!"))
            return redirect('band_detail', band.id)

    return render(request,'bandapp/band_edit.html', context)


def band_delete(request, bid):
    '''r'^band/delete/(\d+)?$', views.band_delete, name = 'band_delete'
        Delete a band view '''
    band = Band.objects.get(id=bid)
    album = Album.objects.filter(band=bid).order_by('-release_date')
    if request.method != "POST":
        context = {'band' : band,
                    'album' : album,
                    }
        return render(request,'bandapp/band_delete.html', context)
    else:
        name = band.band_name
        messages.warning(request, (f"Successfully deleted {name} as a band!"))
        band.delete()
        return HttpResponseRedirect(reverse('band_list'))


def band_add_album(request, bandid):
    ''' r'^band/add/album/(\d+)?$', views.band_add_album, name = 'band_add_album'
        Add an album for the current band '''
    form = AlbumForm(initial={'band': bandid})
    if request != "POST":
        band = Band.objects.get(id=bandid)
        context = {'album_form': form,
                    'band': band
                    }
    return render(request,'bandapp/album_add.html', context)



### ARTISTS ###

def artist_list(request):
    ''' r'^artists/?$', views.artist_list, name = 'artist_list'
        View grid list of all artists '''
    all_musos = Musician.objects.order_by('full_name').all()
    context = { 'musos': all_musos,
                }
    return render(request,'bandapp/artist_list.html', context)


def artist_detail(request, artid):
    ''' r'^artist/detail/(\d+)?$', views.artist_detail, name = 'artist_detail'
        View details for selected artist '''
    muso = Musician.objects.get(id = artid)
    bands = muso.band
    albums = Album.objects.all()
    context = {'muso': muso,
                'bands': bands,
                }
    return render(request,'bandapp/artist_details.html', context)


def artist_add(request):
    ''' r'^artist/add/?$', views.artist_add, name = 'artist_add'
        Form to add an artist '''
    if request.method != "POST":
        context = {'artist_form': ArtistForm()}
    else:
        form = ArtistForm(request.POST)
        if form.is_valid() !=True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'artist_form': form,}
        else:
            data = form.cleaned_data
            artist = form.save()
            name = data.get('full_name')
            messages.success(request, (f"Successfully added {name} as an Artist! "))
            return redirect('artist_detail', artist.id)

    return render(request,'bandapp/artist_add.html',context)


def artist_edit(request, artistid):
    ''' r'^artist/edit/(\d+)?$', views.artist_edit, name = 'artist_edit'
        Form to edit the selected Artist '''
    artist = Musician.objects.get(id = artistid)
    if request.method != "POST":
        context = {'artist_form': ArtistForm(instance = artist),
                     'artist': artist,
                     }
    else:
        form = ArtistForm(request.POST, instance = artist)
        if form.is_valid() !=True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'artist_form': form,}
        else:
            artist = form.save()
            name = artist.full_name
            messages.success(request, (f"Successfully updated {name} as an artist!"))
            return redirect('artist_detail',artist.id )

    return render(request,'bandapp/artist_edit.html',context)


def artist_delete(request, artistid):
    ''' r'^artist/delete/(\d+)?$', views.artist_delete, name = 'artist_delete'
        Delete selected artist view '''
    artist = Musician.objects.get(id = artistid)
    if request.method != "POST":
        bands = artist.band
        albums = Album.objects.all()
        context = {'artist': artist,
                    'bands': bands, }
        return render(request,'bandapp/artist_delete.html', context)
    else:
        name = artist.full_name
        artist.delete()
        messages.warning(request, (f"Successfully deleted artist {name}!"))
        return HttpResponseRedirect(reverse('artist_list'))


### ALBUMS ###

def album_view(request, albumid):
    '''r'^band/album/(\d+)?$', views.album_view, name = 'album_view'
        View selected album'''
    album = Album.objects.get(id= albumid)
    context = {'album' : album,
                }
    return render(request,'bandapp/album_view.html', context)


def album_add(request):
    ''' r'^band/album/add/?$', views.album_add, name = 'album_add'
        Form to add a new album '''
    if request.method != "POST":
        context = {'album_form': AlbumForm()}
    else:
        form = AlbumForm(request.POST)
        if form.is_valid() !=True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'album_form': form,}
        else:
            data = form.cleaned_data
            album = form.save()
            name = data.get('album_name')
            messages.success(request, (f"Successfully added {name} as an Album!"))
            albumid = album.id
            return redirect('album_view', albumid)

    return render(request,'bandapp/album_add.html',context)


def album_edit(request, albumid):
    ''' r'^band/album/edit/(\d+)?$', views.album_edit, name = 'album_edit'
        Form to edit an album with view to add songs to the album'''
    album_instance = Album.objects.get(id = albumid)
    if request.method != "POST":
        album = Album.objects.get(id= albumid)
        album_form = AlbumForm(instance = album)
        song_form = SongForm(initial={'album': albumid})
        context = {
        'album' : album,
        'album_form': album_form,
        'song_form': song_form, }
    else:
        form = AlbumForm(request.POST, instance = album_instance)
        if form.is_valid() != True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'album_form': form,}
        else:
            album = form.save()
            name = album.album_name
            messages.success(request, (f"Successfully updated album {name}! "))
            return redirect('album_view',albumid)

    return render(request,'bandapp/album_edit.html', context)


def album_delete(request, albumid):
    ''' r'^band/album/delete/(\d+)?$', views.album_delete, name = 'album_delete'
        function to delete an album '''
    album = Album.objects.get(id = albumid)
    if request.method != "POST":
        context = {'album' : album,
                    }
        return render(request, 'bandapp/album_delete.html', context)
    else:
        name = album.album_name
        band = album.band.id
        album.delete()
        messages.warning(request, (f"Successfully deleted the {album.band} album, {name}!"))
        return redirect('band_detail', band)



### SONGS ###

def song_add(request):
    ''' r'^band/album/add/song/?$', views.song_add, name = 'song_add'
        Form to add a song to the selected album '''
    if request.method != "POST":
        context = {'song_form': SongForm()}
    else:
        form = SongForm(request.POST)
        if form.is_valid() !=True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'song_form': form,}
        else:
            data = form.cleaned_data
            song = form.save()
            name = data.get('song_title')
            album_name = song.album.album_name
            messages.success(request, (f"Successfully added {name} as a song on album {album_name}!"))
            return redirect('album_edit',song.album.id )

    return render(request,'bandapp/album_edit.html',context)


def song_edit(request, songid):
    ''' r'^band/album/song/edit/(\d+)?$', views.song_edit, name = 'song_edit'
        Form to edit currently selected song '''
    song_instance = Song.objects.get(id = songid)
    if request.method != "POST":
        context = {'song_form': SongForm(instance = song_instance),
                     'song': song_instance,
                     }
    else:
        form = SongForm(request.POST, instance = song_instance)
        if form.is_valid() !=True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'song_form': form,
                        }
        else:
            song = form.save()
            name = song.song_title
            album_name = song.album.album_name
            messages.success(request, (f"Successfully updated {name} as a song on {album_name}!"))
            return redirect('album_view',song.album.id )

    return render(request,'bandapp/album_song_edit.html',context)


def song_delete(request, sid):
    ''' r'^band/album/song/delete/(\d+)?$', views.song_delete, name = 'song_delete'
        Confirm and delete current song on album '''
    song = Song.objects.get(id = sid)
    if request.method != "POST":
        context = {'song': song,
                    }
        return render(request, 'bandapp/album_song_delete.html', context)
    else:
        name = song.song_title
        album = song.album.id
        song.delete()
        messages.warning(request, (f"Successfully deleted {name} as a song on {song.album} album!"))
        return redirect('album_view', album)



### INSTRUMENTS ###

def instrument_list(request):
    ''' r'^instruments/?$', views.instrument_list, name = 'instrument_list'
        View list of instruments in a grid '''
    instruments = Instrument.objects.order_by('instrument_name').all()
    context = {'instruments': instruments,
                }
    return render(request,'bandapp/instrument_list.html', context)


def instrument_detail(request, instrumentid):
    ''' r'^instrument/detail/(\d+)?$', views.instrument_detail, name = 'instrument_detail'
        View details for selected instrument '''
    instrument = Instrument.objects.get(id = instrumentid)
    musos = Musician.objects.filter(instrument = instrumentid)
    context = {'instrument': instrument,
                'musos': musos,
            }
    return render(request,'bandapp/instrument.html', context)


def instrument_add(request):
    ''' r'^instrument/add/?$', views.instrument_add, name = 'instrument_add'
        Form to add new Instrument '''
    if request.method != "POST":
        context = {'instrument_form': InstrumentForm()}
    else:
        form = InstrumentForm(request.POST)
        if form.is_valid() !=True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'instrument_form': form,}
        else:
            data = form.cleaned_data
            instrument = form.save()
            name = data.get('instrument_name')
            messages.success(request, (f"Successfully added {name} as an Instrument!"))
            return redirect('instrument_detail', instrument.id)

    return render(request,'bandapp/instrument_add.html',context)


def instrument_edit(request, instrumentid):
    ''' r'^instrument/edit/(\d+)?$', views.instrument_edit, name = 'instrument_edit'
        Form to edit selected instrument '''
    instrument = Instrument.objects.get(id = instrumentid)
    if request.method != "POST":
        context = {'instrument_form': InstrumentForm(instance = instrument),
         'instrument' : instrument,}
    else:
        form = InstrumentForm(request.POST, instance = instrument)
        if form.is_valid() !=True:
            messages.warning(request, ('There was an error, please try again..'))
            context = {'instrument_form': form,}
        else:
            instrument = form.save()
            name = instrument.instrument_name
            messages.success(request, (f"Successfully updated {name}!"))
            return redirect('instrument_detail',instrument.id )
    return render(request,'bandapp/instrument_edit.html', context)


def instrument_delete(request, instrumentid):
    ''' r'^instrument/delete/(\d+)?$', views.instrument_delete, name = 'instrument_delete'
        Confirm and delete current instrument '''
    instrument = Instrument.objects.get(id = instrumentid)
    if request.method != "POST":
        musos = Musician.objects.filter(instrument = instrumentid)
        context = {'instrument': instrument,
                    'musos': musos, }
        return render(request, 'bandapp/instrument_delete.html', context)
    else:
        name = instrument.instrument_name
        instrument.delete()
        messages.warning(request, (f"Successfully deleted {name}! "))
        return redirect('instrument_list')
