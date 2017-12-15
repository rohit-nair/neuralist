#!/usr/bin/env python
import json
import sqlite3

JSON_FILE = "billboard-top-100-lyrics/data/years/{}.json"
DB_FILE = "lastfm/lastfm_similars.db"

conn = sqlite3.connect(DB_FILE)

for y in range(1950, 2016):
  print y, JSON_FILE.format(y)
  songs = json.load(open(JSON_FILE.format(y)))
  for song in songs:
    lyrics = song["lyrics"]
    position = song["pos"]
    year = song["year"]
    title = song["title"]
    artist = song["artist"]

    data = [position, year, artist, title, lyrics]

    c = conn.cursor()
    #c.execute('create table table_name (foo, bar)')
    c.execute('insert into top100 values (?,?,?,?,?)', data)
  print "Completed year ", y

conn.commit()
c.close()