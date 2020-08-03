from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from bandapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),

    url(r'^bands/?$', views.band_list, name = 'band_list'),
    url(r'^band/detail/(\d+)?$', views.band_detail, name = 'band_detail'),
    url(r'^band/add/?$', views.band_add, name = 'band_add'),
    url(r'^band/add/album/(\d+)?$', views.band_add_album, name = 'band_add_album'),
    url(r'^band/edit/(\d+)?$', views.band_edit, name = 'band_edit'),
    url(r'^band/delete/(\d+)?$', views.band_delete, name = 'band_delete'),

    url(r'^artists/?$', views.artist_list, name = 'artist_list'),
    url(r'^artist/detail/(\d+)?$', views.artist_detail, name = 'artist_detail'),
    url(r'^artist/add/?$', views.artist_add, name = 'artist_add'),
    url(r'^artist/edit/(\d+)?$', views.artist_edit, name = 'artist_edit'),
    url(r'^artist/delete/(\d+)?$', views.artist_delete, name = 'artist_delete'),

    url(r'^band/album/(\d+)?$', views.album_view, name = 'album_view'),
    url(r'^band/album/add/?$', views.album_add, name = 'album_add'),
    url(r'^band/album/edit/(\d+)?$', views.album_edit, name = 'album_edit'),
    url(r'^band/album/delete/(\d+)?$', views.album_delete, name = 'album_delete'),

    url(r'^band/album/add/song/?$', views.song_add, name = 'song_add'),
    url(r'^band/album/song/edit/(\d+)?$', views.song_edit, name = 'song_edit'),
    url(r'^band/album/song/delete/(\d+)?$', views.song_delete, name = 'song_delete'),

    url(r'^instruments/?$', views.instrument_list, name = 'instrument_list'),
    url(r'^instrument/detail/(\d+)?$', views.instrument_detail, name = 'instrument_detail'),
    url(r'^instrument/add/?$', views.instrument_add, name = 'instrument_add'),
    url(r'^instrument/edit/(\d+)?$', views.instrument_edit, name = 'instrument_edit'),
    url(r'^instrument/delete/(\d+)?$', views.instrument_delete, name = 'instrument_delete'),

]
