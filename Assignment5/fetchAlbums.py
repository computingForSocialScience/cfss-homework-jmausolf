import requests
from datetime import datetime

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
   
    album_url = "https://api.spotify.com/v1/artists/"+artist_id+"/albums?offset=0&limit=50&market=US&album_type=album"


    #Error Checking for False ID's
    req = requests.get(album_url)  
    if req.ok == False:
    	bad_data = req.json()
    	print "Error: ", bad_data['error']['message']
    	return False
    elif req.ok == True:
        bad_data = req.json()
        assert bad_data.get('items'), "No albums found."


    data = req.json()


    results = data['items']
    if len(results) > 0:

        for i in range(0, len(results)):
            album_id = data['items'][i]['id']
            
        
        albums = []
        for item in data['items']:
            albums.append(item['id'])
        return albums        

    elif len(results) <= 0:
        print "No albums were found matching this description."




def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    album_url = "https://api.spotify.com/v1/albums/"+album_id

    #Error Checking
    req = requests.get(album_url)
    if req.ok == False:
    	bad_data = req.json()
    	print "Error: ", bad_data['error']['message']
        return False
    else:
        bad_data = req.json()
        assert bad_data.get('name'), "No albums found."
        
    
    data = req.json()

    #Build dictionary   
    album_info = {}  #dictionary key_name = data['value']
    album_info['Artist Name: '] = data['artists'][0]['name']
    album_info['Artist ID: '] = data['artists'][0]['id']
    album_info['Album ID: '] = data['id']
    album_info['Album Name: '] = data['name']
    year_raw = str(data['release_date'])
    album_info['Year: '] = year_raw[0:4]
    album_info['Popularity: '] = data['popularity']
    album_info['URL: '] = data['external_urls']['spotify']

    #Return Dictionary
    return album_info



