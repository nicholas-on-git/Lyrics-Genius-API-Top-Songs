import lyricsgenius
import pandas as pd

genius = lyricsgenius.Genius('sampleapikey')

artist_list = ['beabadoobee',
               'clairo',
               'niki',
               'rina sawayama',
               'newdad',
               'crying city',
               'towa bird',
               'illit',
               'olivia rodrigo'
              ]

title_values = []
artist_values = []
pyongs = []
pageviews = []
annotations = []

index = 0 
while index < len(artist_list):
    
    for artist in artist_list:
        song = genius.search_artist(artist, max_songs=100, sort='popularity')

        for each in song.songs:
            title_values.append(each.title)
            artist_values.append(each.artist)
            pyongs.append(each.pyongs_count)
            pageviews.append(each._body['stats']['pageviews'])
            annotations.append(each._body['stats']['accepted_annotations'])

            index +=1

key_value_pair = {'Title' : title_values,
                  'Artist' : artist_values,
                  'Pyongs' : pyongs,
                  'Pageviews' : pageviews,
                  'annotations' : annotations
                 }

df_song_data = pd.DataFrame(key_value_pair)

unique_artists = df_song_data['Artist'].unique()

for artist in unique_artists:
    song_data = df_song_data[df_song_data['Artist'] == artist]
    song_data.to_excel(f'./MAX SONGS/{artist}.xlsx', index=False)
