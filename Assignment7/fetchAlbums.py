import requests
from datetime import datetime

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
   
    album_url = "https://api.spotify.com/v1/artists/"+artist_id+"/albums?market=US&album_type=album"

    #Error Checking for False ID's
    req = requests.get(album_url)  
    assert req.ok, "Error: No record found."

    data = req.json()
    assert data.get('items'), "Error: No albums found for this request."

    albums = []
    results = data['items']
    for i in range(0, len(results)):
        album_id = data['items'][i]['id']  
        albums.append(album_id)
    return albums  



def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    album_url = "https://api.spotify.com/v1/albums/"+album_id

    #Error Checking
    req = requests.get(album_url)
    assert req.ok, "Error: No record found."
    data = req.json()
    assert data.get('name'), "Error: Album not found."

    #Build dictionary   
    album_info = {}  #dictionary key_name = data['value']
    album_info['artist_name'] = data['artists'][0]['name']
    album_info['artist_id'] = data['artists'][0]['id']
    album_info['album_id'] = album_id
    album_info['name'] = data['name']
    album_info['year'] = data['release_date'][0:4]
    album_info['popularity'] = data['popularity']
    album_info['url'] = data['external_urls']['spotify']

    #Return Dictionary
    return album_info

