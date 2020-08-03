from django.db import models

class Band(models.Model):
    '''Band object'''
    band_name = models.CharField(max_length = 50)
    est_since = models.DateField()
    band_image_url = models.URLField(default='https://bit.ly/2xZwci2')
    bio = models.TextField(max_length = 1000, blank = True)

    def __str__(self):
        return self.band_name

    class Meta:
        ordering = ["band_name"]



class Instrument(models.Model):
    '''Instrument object'''
    instrument_name = models.CharField(max_length = 50)
    image_url = models.URLField(default = 'https://bit.ly/2WT4gop', blank = True)

    def __str__(self):
        return self.instrument_name

    class Meta:
        ordering = ["instrument_name"]



class Musician(models.Model):
    '''Musician object'''
    full_name = models.CharField(max_length = 70)
    instrument = models.ManyToManyField(Instrument, blank = True)
    band = models.ManyToManyField(Band, blank = True)

    def __str__(self):
        return str(self.full_name)

    class Meta:
        ordering = ["full_name"]



class Album(models.Model):
    '''Album Object'''
    album_name = models.CharField(max_length = 50)
    release_date = models.DateField()
    band = models.ForeignKey(Band, on_delete = models.CASCADE)
    musician = models.ManyToManyField(Musician, blank = True)

    def __str__(self):
        return self.album_name + ' | ' + str( self.band)



class Song(models.Model):
    '''Song Object'''
    song_title = models.CharField(max_length = 50)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    music_video_url = models.URLField(default = 'https://www.youtube.com/watch?v=Q4SxizAg6bk')

    def __str__(self):
        return self.song_title + ' | ' + str( self.album)
