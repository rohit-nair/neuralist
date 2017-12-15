#!/usr/bin/env python
import json
import sqlite3

DUPE_FILE = "lastfm_duplicates.txt"
DB_FILE = "data/lastfm_similars.db"

conn = sqlite3.connect(DB_FILE)

songs = open(DUPE_FILE)
for x in songs:
  if x.startswith("TR"):
    data = [x.rstrip()]

    c = conn.cursor()
    #c.execute('create table table_name (foo, bar)')
    c.execute('insert into dupes values (?)', data)

conn.commit()
c.close()