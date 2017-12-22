#!/usr/bin/env python
import json
import sqlite3

DUPES_FILE = "lastfm_duplicates.txt"
DB_FILE = "./data/lastfm_similars.db"

conn = sqlite3.connect(DB_FILE)

dupes = open(DUPES_FILE)

count = 0
for dup in dupes.readlines():
  if not dup.startswith("TR"):
    continue

  c = conn.cursor()
  #c.execute('create table table_name (foo, bar)')
  c.execute('delete from songs where track_id = \'{}\''.format(dup))

  count += 1

print '{} records deleted.'.format(count)
conn.commit()
c.close()