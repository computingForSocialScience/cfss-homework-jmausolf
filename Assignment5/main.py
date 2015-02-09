import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

def ARTIST(artist_name):
    fetchArtistId(artist_name)
    Artist_ID = str(fetchArtistId(artist_name))
    
    fetchArtistInfo(Artist_ID)
    #fetchAlbumIds(Artist_ID)

    Album_ID = fetchAlbumIds(Artist_ID)
    
    for ID in Album_ID:
    	fetchAlbumInfo(ID)


## Example syntax to run from terminal shell:
## python main.py "Zac Brown Band", "Usher", "Blink 182"

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "Input artists are : ", artist_names
    # YOUR CODE HERE
    for i in artist_names:
    	ARTIST(i)








"""if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "Input artists are : ", artist_names
    # YOUR CODE HERE
    #artist_names = ["Justin Timberlake", "Usher", "Zac Brown Band"]
    for i in artist_names:
    	fetchArtistId(i)
    	Artist_ID = str(fetchArtistId(i))
    
    	fetchArtistInfo(Artist_ID)
    	#fetchAlbumIds(Artist_ID)

       	Album_ID = fetchAlbumIds(Artist_ID)
    
    	for ID in Album_ID:
    		fetchAlbumInfo(ID)"""