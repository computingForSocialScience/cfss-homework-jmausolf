from io import open
import csv


def writeArtistsTable(artist_info_list):
    """Given a list of dictionries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY
    """

    f = open('artists.csv', 'w', encoding='utf-8')
    try:
        f.write(u'ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY\n')
        for element in artist_info_list:
            artist_id = element['id']
            artist_name = element['name']
            artist_followers = element['followers']
            artist_popularity = element['popularity']
            f.write(u'%s,"%s",%s,%s\n' % (artist_id, artist_name, artist_followers, artist_popularity))
    finally:
        f.close()


#Test code: Un-docstring to test
"""artist_info_list = [{'ID: ': '6FBDaR13swtiWwGhX1WQsP', 'Name: ': 'blink-182', 'Followers: ': 803199, 'Popularity: ': 83}]
writeArtistsTable(artist_info_list)"""
      



def writeAlbumsTable(album_info_list):
    """
    Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY
    """

    f = open('albums.csv', 'w', encoding='utf-8')
    try:
        f.write(u'ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY\n')
        for element in album_info_list:
            album_artist_id = element['artist_id']
            album_id = element['album_id']
            album_name = element['name']
            album_year = element['year']
            album_popularity = element['popularity']
            f.write(u'%s,%s,"%s",%s,%s\n' % (album_artist_id, album_id, album_name, album_year, album_popularity))
    finally:
        f.close()



#Test code: Un-docstring to test
"""album_info_list = [{'Artist ID: ': '6FBDaR13swtiWwGhX1WQsP', 'Album ID: ': '2CoVyQi2zIifUNBcVR0gEH', 'Album Name: ': 'Dude Ranch', 'Year: ': 1997, 'Popularity: ': 57}]
writeAlbumsTable(album_info_list)"""
