import pymysql
dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

#Create Blank Tables
cur = db.cursor()
CREATE_TABLE_playlist = '''CREATE TABLE IF NOT EXISTS playlists (id INTEGER PRIMARY KEY AUTO_INCREMENT, rootArtist VARCHAR(260));'''
CREATE_TABLE_songs = '''CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY AUTO_INCREMENT, playlistId INTEGER, songOrder INTEGER, artistName VARCHAR(260), albumName VARCHAR(260), trackName VARCHAR(260));'''
cur.execute(CREATE_TABLE_playlist)
cur.execute(CREATE_TABLE_songs)
db.commit()


#Other Commands
"""
#Enter into BASH
mysql -h localhost -u root 


#Enter into MYSQL

create database playlists;
use playlists;

#Create Blank Tables
create table playlists (id INTEGER PRIMARY KEY AUTO_INCREMENT, rootArtist VARCHAR(255));

create table songs (id INTEGER PRIMARY KEY AUTO_INCREMENT, playlistId INTEGER, songOrder INTEGER, artistName VARCHAR(255), albumName VARCHAR(255), trackName VARCHAR(255));


#Show Entries

SELECT * FROM playlists;
SELECT * FROM songs;
"""