#!/usr/bin/env python
import json
import sqlite3

DUPE_FILE = "lastfm_duplicates.txt"
DB_FILE = "data/lastfm_similars.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""Select * from top100_similars;""")
all_data = cursor.fetchall()
print "all_data", len(all_data)

cursor.execute("""CREATE TABLE IF NOT EXISTS top100_similars_mapped
                    (tid TEXT,
                    target TEXT,
                    similarity REAL)""")

count = 0
rows = 0
for single_data in all_data:
    countries = single_data[1].split(",")
    #print "length countries", len(countries), countries
    for i in range(0,len(countries)/2):
        #print "inserting {} {} {}".format(single_data[0],countries[i*2], float(countries[i*2+1]))
        cursor.execute("INSERT INTO top100_similars_mapped (tid, target, similarity) VALUES(?,?,?)",[single_data[0],countries[i*2], float(countries[i*2+1])])

    conn.commit()
    rows += len(countries)/2
    count += 1
    print "##### {} rows processed and {} inserted      \r".format(count, rows),

print ""
cursor.close()