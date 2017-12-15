#!/usr/bin/env python
import numpy as np
import os
import sys
import sqlite3

INPUT_FILE = "similar_songs.csv"
SHUFFLE = 42
TRAIN_FRAC = 0.8


if __name__ == '__main__':
    songs = open(INPUT_FILE).readlines()
    print '{} song mappings loadedd'.format(len(songs))
    if SHUFFLE == 42:
        rng = np.random.RandomState(SHUFFLE)
        rng.shuffle(songs)  # in-place
    train_frac = 0.8
    split_idx = int(TRAIN_FRAC * len(songs))
    train_lyrics = songs[:split_idx]
    test_lyrics = songs[split_idx:]

    print "Training set: %d sentences" % (len(train_lyrics))
    print "Test set: %d sentences" % (len(test_lyrics))

    status = 0
    with open('train_mapping.csv', 'w') as f:
      for m in train_lyrics:
        f.write(m)
        status += 1
    print 'Wrote {} lines to train_mapping.csv'.format(status)

    status = 0
    with open('test_mapping.csv', 'w') as f:
      for m in test_lyrics:
        f.write(m)
        status += 1
    print 'Wrote {} lines to test_mapping.csv'.format(status)

