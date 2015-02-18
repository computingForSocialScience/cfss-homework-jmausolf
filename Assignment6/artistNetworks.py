import sys
import requests
import csv
import requests, pandas as pd

#Used in Additional Function writeEdgeList_byArtist(name, depth)
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


#Example to test. Unhash to test.
#Test Blink-182
#getRelatedArtists("6FBDaR13swtiWwGhX1WQsP")



def getDepthEdges(artistID, depth):
    """Generates a list of related artists for a given "depth" given
    an initial artistID and requested depth."""

    #Error Checking Inputs
    if type(depth) == type(1):
        pass
    else: 
        print "Error: Depth must be of type == integer."
        return
    
    #depth = int(Depth)  
    if depth > 0:
        pass
    else:
        print "Please return a depth of 1 or greater."
        return

    #Depth 1 Artist List
    pairs = [(artistID, rel_artist) for rel_artist in getRelatedArtists(artistID)]

    #Depth > 1, Artist List
    linked_artists = 0
    for i in range(0, depth-1):
        completed_pairs = linked_artists
        completed_artists = set(x[0] for x in pairs[:completed_pairs])
        new_pairs = []
        for pair in pairs[completed_pairs:]:
            linked_artists += 1
            artist = pair[1]
            if artist in completed_artists:
                continue
            current_pairs = frozenset(pairs + new_pairs)
            new_pairs += [(artist, artist2) for artist2 in getRelatedArtists(artist) if (artist, artist2) or (artist2, artist) not in current_pairs]
        pairs += new_pairs 


    #Removes Duplicate Artist Combinations
    final = set(map(frozenset, pairs))
    final_pairs = list(final)
    return final_pairs


#Example to test. Unhash to test.
#getDepthEdges("6FBDaR13swtiWwGhX1WQsP", 1)


def getEdgeList(artistID, depth):
    """Gets a list of 'edges' or artist1 to artist2 links
    writing the results to a Pandas DataFrame."""

    final_pairs = getDepthEdges(artistID, depth)
    fp_df = pd.DataFrame(final_pairs, columns=['Artist1', 'Artist2'])
    #print fp_df #Un-hash to test.
    return fp_df    


#Example to test. Unhash to test.
#getEdgeList("6FBDaR13swtiWwGhX1WQsP", 2)

def writeEdgeList(artistID, depth, filename_str):
    """Writes a CSV file of the artist and related artists for
    a given artistID and requested depth."""
    
    df = getEdgeList(artistID, depth)
    df.to_csv(filename_str+".csv", index=False) 

#Example to test. Unhash to test.
#writeEdgeList("6FBDaR13swtiWwGhX1WQsP", 2, "Blink-182")



def writeEdgeList_byArtist(artistname, depth):
    """Writes a CSV file of the artist and related artists for
    a given artistID and requested depth."""
    
    artistID = fetchArtistId(artistname)
    filename_str = artistname.replace(' ', '_')
    df = getEdgeList(artistID, depth)
    df.to_csv(filename_str+".csv", index=False)


#Example to test. Unhash to test.
#writeEdgeList_byArtist("Blink-182", 2)
#writeEdgeList_byArtist("Zac Brown Band", 2)
