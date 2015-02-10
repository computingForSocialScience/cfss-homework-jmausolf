#Background functions for running the script print_main.py


import sys
import requests


def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    
    name_space = name.replace(" ", "%20")
    url = "https://api.spotify.com/v1/search?q="+name_space+"&type=artist"

    req = requests.get(url)  
    if req.ok == False:
        return False
    data = req.json()
    # Get the ID for the first result [0] for a given artist name
    results = data['artists']['items']
    if len(results) > 0:
        artist_id = data['artists']['items'][0]['id']
        return artist_id
    elif len(results) <= 0:
        print "No artists were found matching this description.", "\n", "Artist ID = <null request>."
        
    


def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and 
    returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """

    url = 'https://api.spotify.com/v1/artists/'+artist_id
    #print url
    
    req = requests.get(url)  
    if req.ok == False:
        return False
    data = req.json()
    

    #Build dictionary   
    artist_info = {}  #dictionary key_name = data['value']
    artist_info['Followers: '] = data['followers']['total'] 
    if data['genres'] == None:
        artist_info['Genre: '] = 'NA'
        pass
    elif data['genres'] != []:
        artist_info['Genre: '] = data['genres'][0]
    artist_info['URL: '] = data['external_urls']['spotify']
    artist_info['ID: '] = data['id']
    artist_info['Name: '] = data['name']
    artist_info['Popularity: '] = data['popularity']
      
    
    #Print Dictionary
    print "*"*50
    print "*"*5, "ARTIST INFO", "*"*5
    for key, value in artist_info.items():
        print key, value
    print "*"*50    




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
    data = req.json()

    results = data['items']
    if len(results) > 0:
        print "Total Albums: ", len(results)
        print "*"*22
        print "ALBUM IDs: "
        print "*"*22

        for i in range(0, len(results)):
            album_id = data['items'][i]['id']
            print album_id
        
        albums = []
        for item in data['items']:
            albums.append(item['id'])
        return albums   
      
    elif len(results) <= 0:
        print "No albums were found matching this description."




def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'album name', 'year', 
    'popularity', and 'url'
    """
    album_url = "https://api.spotify.com/v1/albums/"+album_id

    
    #Error Checking
    req = requests.get(album_url)  
    if req.ok == False:
        bad_data = req.json()
        print "Error: ", bad_data['error']['message']
        return False
    
    data = req.json()

    #Build dictionary   
    album_info = {}  #dictionary key_name = data['value']
    album_info['Artist: '] = data['artists'][0]['name'] 
    album_info['Album ID: '] = data['id']
    album_info['Album Name: '] = data['name']
    album_info['URL: '] = data['external_urls']['spotify']
    year_raw = str(data['release_date'])
    album_info['Year: '] = year_raw[0:4]
    album_info['Popularity: '] = data['popularity']

    #Print Dictionary
    print "*"*60
    print "*"*10, "ALBUM INFO", "*"*10
    for key, value in album_info.items():
        print key, value
    print "*"*60







