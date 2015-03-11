import sys
import requests
import csv

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    
    name_space = name.lower().replace(" ", "%20")
    url = "https://api.spotify.com/v1/search?q="+name_space+"&type=artist"

    #Error checking
    req = requests.get(url)  
    assert req.ok, "Error: No record was found."
    data = req.json()
    assert data.get('artists').get('items'), "Error: Artist not found."

    # Get the ID for the first result [0] for a given artist name
    results = data['artists']['items']
    if len(results) > 0:
        artist_id = data['artists']['items'][0]['id']
        return artist_id

    elif len(results) <= 0:
        print "No artists were found matching this description.", "\n", "Artist ID = <null request>."

#print fetchArtistId("Blink 182")


def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
    returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """


    url = 'https://api.spotify.com/v1/artists/'+artist_id

    #Error checking    
    req = requests.get(url)  
    assert req.ok, "Error: Request error, no record."
    data = req.json()
    artist_info = {}  #dictionary key_name = data['value']

    #Build dictionary   
    assert data.get('name'), "Error: Artist not found."
    artist_info['followers'] = data['followers']['total']
    artist_info['genres'] = data['genres']
    artist_info['url'] = data['external_urls']['spotify']
    artist_info['id'] = artist_id
    artist_info['name'] = data['name']
    artist_info['popularity'] = data['popularity']

    #Return Dictionary
    return artist_info
