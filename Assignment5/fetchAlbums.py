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

# Unit Testing, Un-Docstring to Test       
"""
fetchAlbumIds("23zg3TcAtWQy7J6upgbUnj") #Usher
fetchAlbumIds("31TPClRtHm23RisEBtV3X7") #Justin Timberlake"""




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


# Unit Testing, Un-Docstring to Test  
"""
fetchAlbumInfo("0fQdoem8dnrl80YcZzQ8f0")
fetchAlbumInfo("5w40WGuhOElvPC9Dy641Yw")"""
