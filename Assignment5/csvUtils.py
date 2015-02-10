from io import open
import csv


def writeArtistsTable(artist_info_list):
    """Given a list of dictionries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file header: ARTIST_ID, ARTIST_NAME, ARTIST_FOLLOWERS, ARTIST_POPULARITY, 
    ARTIST_GENRE, ARTIST_URL
    """

    f = open('artists.csv', 'w', encoding='utf-8')
    f.write(u'ARTIST_ID, ARTIST_NAME, ARTIST_FOLLOWERS, ARTIST_POPULARITY, ARTIST_GENRE, ARTIST_URL \n')
    for element in artist_info_list:
        artist_id = element['ID: ']
        artist_name = element['Name: ']
        artist_followers = element['Followers: ']
        artist_popularity = element['Popularity: ']
        if element['Genre: '] == None:
            continue
        elif element['Genre: '] != []:
            artist_genre = element['Genre: ']
        artist_url = element['URL: ']
        f.write(u'%s, "%s", %s, %s, "%s", %s\n' % (artist_id, artist_name, artist_followers, artist_popularity, artist_genre, artist_url))
    f.close()


#Test code: Un-docstring to test
"""artist_info_list = [{'ID: ': '6FBDaR13swtiWwGhX1WQsP', 'Name: ': 'blink-182', 'Followers: ': 803199, 'Popularity: ': 83, 'Genre: ': 'pop punk', 'URL: ':  'https://open.spotify.com/artist/6FBDaR13swtiWwGhX1WQsP'}]
writeArtistsTable(artist_info_list)"""




def writeAlbumsTable(album_info_list):
    """
    Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'.

    The csv file header: ARTIST_ID, ALBUM_ID, ALBUM_NAME, ALBUM_YEAR, ALBUM_POPULARITY, ARTIST_NAME, ALBUM_URL
    """

    f = open('albums.csv', 'w', encoding='utf-8')
    f.write(u'ARTIST_ID, ALBUM_ID, ALBUM_NAME, ALBUM_YEAR, ALBUM_POPULARITY, ARTIST_NAME, ALBUM_URL \n')
    for element in album_info_list:
        album_artist_id = element['Artist ID: ']
        album_id = element['Album ID: ']
        album_name = element['Album Name: ']
        album_year = element['Year: ']
        album_popularity = element['Popularity: ']
        album_artist_name = element['Artist Name: ']
        album_url = element['URL: ']
        f.write(u'%s, %s, "%s", %s, %s, "%s", %s\n' % (album_artist_id, album_id, album_name, album_year, album_popularity, album_artist_name, album_url))
    f.close()



#Test code: Un-docstring to test
"""album_info_list = [{'Artist ID: ': '6FBDaR13swtiWwGhX1WQsP', 'Album ID: ': '2CoVyQi2zIifUNBcVR0gEH', 'Album Name: ': 'Dude Ranch', 'Year: ': 1997, 'Popularity: ': 57, 'Artist Name: ': 'blink-182',  'URL: ': 'https://open.spotify.com/album/2CoVyQi2zIifUNBcVR0gEH'}]
writeAlbumsTable(album_info_list)"""
