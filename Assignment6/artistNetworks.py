import sys
import requests
import csv



def getRelatedArtists(artistID):
    """Using the Spotify API, take an artist ID and 
    returns a list of related artists in a list"""

    url = "https://api.spotify.com/v1/artists/"+artistID+"/related-artists"

    #Error checking    
    req = requests.get(url)  
    assert req.ok, "Error: Request error, no record."
    data = req.json()
    related_artists = data['artists']

    #Related Artist IDs
    artist_IDs = []
    for artist in related_artists:
        artist_IDs.append(artist['id'])
    return artist_IDs


#Test Blink-182
getRelatedArtists("6FBDaR13swtiWwGhX1WQsP")


def getDepthEdges(artistID, depth):
    """Generates a list of related artists for a given "depth" given
    an initial artistID and requested depth."""

    linked_artists = []
    for i in range(0, depth):
        related_artists = getRelatedArtists(artistID)
        for artist in related_artists:
            linked_artists.append((artistID, artist))
            if (depth-1)==0:
                pass
            else:
                linked_artists=linked_artists+(getDepthEdges(artist, depth-1))
    print linked_artists
    return linked_artists

#Test Depth 2, Initial Band Blink-182.
#getDepthEdges("6FBDaR13swtiWwGhX1WQsP", 2)
