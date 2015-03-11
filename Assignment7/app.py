from flask import Flask, render_template, request, redirect, url_for
import pymysql

#Import Other Python Modules
import sys, io, random
import networkx as nx
import pandas as pd

#Import Past HW Modules
from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *


#Flask Database Info - Mac OSX, No Password
dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')


app = Flask(__name__)

def createNewPlaylist(inputName):
    """Function to make a new playlist, save the file to a MySQL database, and render the HTML file."""
    cur = db.cursor()
    CREATE_TABLE_playlist = '''CREATE TABLE IF NOT EXISTS playlists (id INTEGER PRIMARY KEY AUTO_INCREMENT, rootArtist VARCHAR(260));'''
    CREATE_TABLE_songs = '''CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY AUTO_INCREMENT, playlistId INTEGER, songOrder INTEGER, artistName VARCHAR(260), albumName VARCHAR(260), trackName VARCHAR(260));'''
    cur.execute(CREATE_TABLE_playlist)
    cur.execute(CREATE_TABLE_songs)
    db.commit()


    artistID = fetchArtistId(inputName)

    #Get edgeList for Depth of 2
    edgeList = getEdgeList(artistID, 2)
    Digraph = pandasToNetworkX(edgeList)

    #Pick random central artist from inputDigraph
    Random_artists = []
    for i in range(30):
        #Pick random albumId based on above random artist.
        random_artist = randomCentralNode(Digraph)
        Random_artists.append(random_artist)

    #Assembling Random Playlist
    artist_names = []
    album_list = []
    for artist_id in Random_artists:
        artist = fetchArtistInfo(artist_id)
        artist_name = artist['name']
        artist_names.append(artist_name)
        album_id_list = fetchAlbumIds(artist_id)


        #Exception for missing Spotify data
        if album_id_list == []:
            print "Error: Empty Spotify 'none type' album id for", artist_name, ". Pass and continue."
            continue
        random_album = random.choice(album_id_list)
        random_album_info = fetchAlbumInfo(random_album) 
        random_album_name = random_album_info['name']
        random_album_data = (random_album_name, random_album)
        album_list.append(random_album_data)

    #Get Random Track
    random_track_list = []
    for album in album_list:
        url = "https://api.spotify.com/v1/albums/"+album[1]+"/tracks"
        req = requests.get(url)
        assert req.ok, "Error: Sorry, no record was found."
        req.json()

        json_data = req.json()
        get_items = json_data.get('items')
        track_list = []
        for i in range(len(get_items)):
            get_track_name = get_items[i]['name']
            track_list.append(get_track_name)
            random_track = (random.choice(track_list))
        random_track_list.append(random_track)


    #Add artist's name to the playlists table.
    cur = db.cursor()
    add_to_playlist = '''INSERT INTO playlists (rootArtist) VALUES ('%s')''' % (inputName)
    cur.execute(add_to_playlist) 
    db.commit()


    #Sort the song order and append random tracks and information to playlist. 
    for i in range(len(random_track_list)):
        songOrder = i+1
        Artist_Name = '"' + artist_names[i] + '"'
        Artist_Name.replace("\'","")
        Artist_Name.replace("\"","")
        Album_Name = '"' + album_list[i][0] + '"'
        Album_Name.replace("\'","")
        Album_Name.replace("\"","")
        Track_Name = '"' + random_track_list[i] + '"'
        Track_Name.replace("\'","")
        Track_Name.replace("\"","")

        get_id_number = """SELECT MAX(id) from playlists;"""
        cur.execute(get_id_number)
        playlist_id = cur.fetchall()
        playlistId = playlist_id[0][0]

        #Write to MySQL
        sql = '''INSERT INTO songs (playlistId, songOrder, artistName, albumName, trackName) VALUES (%d, %d, %s, %s, %s)''' % (playlistId, songOrder, Artist_Name, Album_Name, Track_Name)
        cur.execute(sql)
        db.commit()



@app.route('/')
def make_index_resp():
    # Routes to local http://127.0.0.1:5000/    
    return(render_template('index.html'))


@app.route('/playlists/')
def make_playlists_resp():
    cur = db.cursor()
    sql = '''
        SELECT id,rootArtist
        FROM playlists
        ORDER BY id '''
    cur.execute(sql)
    playlists = cur.fetchall()
    return render_template('playlists.html',playlists=playlists)


@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
    cur = db.cursor()
    sql = '''
        SELECT songOrder, artistName, albumName, trackName
        FROM songs
        WHERE playlistId=''' + playlistId + '''
        ORDER BY songOrder;'''
    cur.execute(sql)
    songs = cur.fetchall()
    return render_template('playlist.html',songs=songs)


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # Execute when user visits page
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # Execute when user completes form
        artistName = request.form['artistName']

        #Use to avoid having the debugger crash from Spotify
        try:
            createNewPlaylist(artistName)
            return(redirect("/playlists/"))
        except:
            print "Random exception occured. Playlist may not have wrote or have a length less than thirty."
            print "Try to rerun the playlist. If error persists, try another artist."
            return(redirect("/playlists/"))




if __name__ == '__main__':
    app.debug=True
    app.run()