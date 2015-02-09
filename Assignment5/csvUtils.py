from io import open

def writeArtistsTable(artist_info_list):
    """Given a list of dictionries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY
    """

    header = u'ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY'
    

    f = open('artists.csv', 'w')
    f.write(header)
    f.write(u'\n')
    f.write(artist_info_list)
    f.close()
      

test_artist_list = u"6vWDO969PvNqNYHIOW5v0m, 'Beyonce', 2539238, 95"


writeArtistsTable(test_artist_list)

def writeAlbumsTable(album_info_list):
    """
    Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY
    """

    header = u'ARTIST_ID, ALBUM_ID, ALBUM_NAME, ALBUM_YEAR, ALBUM_POPULARITY'
    

    f = open('albums.csv', 'w')
    f.write(header)
    f.write(u'\n')
    f.write(album_info_list)
    f.close()


test_album_list = u"6vWDO969PvNqNYHIOW5v0m, 6oxVabMIqCMJRYN1GqR3Vf, 'Dangerously In Love', 2003, 74"

writeAlbumsTable(test_album_list)