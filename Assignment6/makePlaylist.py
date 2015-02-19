# Import Modules
import sys, io, requests, random, subprocess
from artistNetworks import *
from analyzeNetworks import *
sys.path.append('../Assignment5/')
from fetchArtist import *
from fetchAlbums import *
from print_main import ARTIST


#Get Random Track
def get_random_track(album_id):
	"""Function to return an random song track given an albumID."""

	url = "https://api.spotify.com/v1/albums/"+album_id+"/tracks"
	#Error checking
	req = requests.get(url)
	assert req.ok, "Error: Sorry, no record was found."
	data = req.json()
	assert data.get('total'), "Error: Sorry, no tracks found for this record."
	tracks = [data['items'][i]['name'] for i in range(len(data['items']))]
	random_track = random.choice(tracks)
	return random_track


#Example to test. Unhash to test.
#Test Blink-182, Album Dude Ranch, as provided by ARTIST.
#ARTIST("Blink-182")
#print get_random_track("2CoVyQi2zIifUNBcVR0gEH")


#Make the function callable from command terminal
if __name__ == '__main__':
    Artists = sys.argv[1:]

    #Check to make sure there are artist inputs.
    assert Artists, "Error: Please provide one or more artists."
    
    #Define joint edge lists and combined network for the given artists.
    for x in Artists:
    	edgeLists = [getEdgeList_byArtist(x, 2)]
    #edgeLists = [getEdgeList_byArtist(x, 2) for x in Artists]
    Joint_edgeLists = edgeLists[0]
    for i in range(1, len(edgeLists)):
        next_edgeList = edgeLists[i]
        Joint_edgeLists = combineEdgeLists(Joint_edgeLists, next_edgeList)
    DiGraph = pandasToNetworkX(Joint_edgeLists)


    Random_artists = []
    Random_albumIds = []
    for i in range(30):
        is_run = False

        #Pick random central artist from inputDigraph
        artist = randomCentralNode(DiGraph)
        while not is_run:
            try:
            	#Pick random albumId based on above random artist.
                Random_albumIds.append(random.choice(fetchAlbumIds(artist)))
                is_run = True
            except AssertionError:
                artist = randomCentralNode(DiGraph)
        Random_artists.append(fetchArtistInfo(artist)['name'])

    #Assembling Random Playlist
    random_plist_albums = []
    random_plist_tracks = []
    for album in Random_albumIds:
        random_plist_albums.append(fetchAlbumInfo(album)['name'])
        random_plist_tracks.append(get_random_track(album))
    playlist = zip(Random_artists, random_plist_albums, random_plist_tracks)

    #Writing the Playist to a CSV
    with io.open('playlist.csv', 'w', encoding='utf-8') as f:
	    f.write(u"ARTIST   , ALBUM   , TRACK   \n")
	    for col1, col2, col3 in playlist:
	    	f.write(u'"%s","%s","%s"\n' % (col1, col2, col3))




#Test Results using tests.py
"""
.......
----------------------------------------------------------------------
Ran 7 tests in 48.974s

OK
"""

