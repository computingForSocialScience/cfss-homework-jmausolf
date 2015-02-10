# This function takes the artist id, artist info, album id, and album info and prints this
# outupt to the terminal. Note, this is not officially part of HW#5, but rather a byproduct
# of the struggles in creating it. Try running it for any number of bands. 

# E.G. if in the directory where these files are stored, run in terminal: 
# python print_main.py "Zac Brown Band", "Usher", "Blink 182"




import sys
from fetch_print import fetchArtistId, fetchArtistInfo, fetchAlbumIds, fetchAlbumInfo


def ARTIST(artist_name):
    fetchArtistId(artist_name)
    Artist_ID = str(fetchArtistId(artist_name))
    
    fetchArtistInfo(Artist_ID)
    #fetchAlbumIds(Artist_ID)

    Album_ID = fetchAlbumIds(Artist_ID)
    
    for ID in Album_ID:
    	fetchAlbumInfo(ID)


## Example syntax to run from terminal shell:
## python print_main.py "Zac Brown Band", "Usher", "Blink 182"

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "Input artists are : ", artist_names
    # YOUR CODE HERE
    for i in artist_names:
    	ARTIST(i)