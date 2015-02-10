import sys
import requests

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    
    name_space = name.replace(" ", "%20")
    url = "https://api.spotify.com/v1/search?q="+name_space+"&type=artist"

    #Error checking
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

    #Error checking    
    req = requests.get(url)  
    if req.ok == False:
        return False
    elif req.ok == True:
        bad_data = req.json()
        assert bad_data.get('genres'), "No genres found."


    data = req.json()  

    #Build dictionary   
    artist_info = {}  #dictionary key_name = data['value']
    artist_info['Followers: '] = data['followers']['total'] 
    if data['genres'] == None:
        artist_info['Genre: '] = data['genres'][0]
        pass
    elif data['genres'] != []:
        artist_info['Genre: '] = data['genres'][0]
    artist_info['URL: '] = data['external_urls']['spotify']
    artist_info['ID: '] = data['id']
    artist_info['Name: '] = data['name']
    artist_info['Popularity: '] = data['popularity']

    #Return Dictionary
    return artist_info




