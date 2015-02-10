import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

def ARTIST(artist_name):

    artist_info_list = []
    album_info_list = []

    #Make artist_info_list
    artist_id = fetchArtistId(artist_name)
    artist_info = fetchArtistInfo(artist_id)
    artist_info_list.append(artist_info)

    #Make album_info_list
    album_id = fetchAlbumIds(artist_id)
    for ID in album_id:
        album_info = fetchAlbumInfo(ID)
        album_info_list.append(album_info)

    


## Example syntax to run from terminal shell:
## python main.py "Zac Brown Band", "Usher", "Blink 182"

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "Input artists are : ", artist_names

    # Create Empty Info Lists
    artist_info_list = []
    album_info_list = []

    #Make artist_info_list
    for artist_name in artist_names:
        artist_id = fetchArtistId(artist_name)
        artist_info = fetchArtistInfo(artist_id)
        artist_info_list.append(artist_info)

    #Make album_info_list
        album_id = fetchAlbumIds(artist_id)
        for ID in album_id:
            album_info = fetchAlbumInfo(ID)
            album_info_list.append(album_info)

    #Write CSV Files from Info Lists
    writeArtistsTable(artist_info_list)
    writeAlbumsTable(album_info_list)

    #Plot and Open Bar Chart
    plotBarChart()



