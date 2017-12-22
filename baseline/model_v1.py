import csv, numpy as np
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

def cosine_sim(text1, text2):
    tfidf = vectorizer.transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

with open("master_dataset.csv") as f:
    reader = csv.reader(f)
    songs = [s for s in reader]
    print "{} songs loaded from file.".format(len(songs))
    
# Randomly shuffle data
np.random.seed(131)
shuffle_indices = np.random.permutation(np.arange(len(songs)))
print shuffle_indices.shape, len(songs)

song_shuffled = np.asarray(songs)[shuffle_indices]
train_split = 80*len(song_shuffled)//100

song_train, song_test = song_shuffled[:train_split], song_shuffled[train_split:]
print "Training songs shape: {}, test songs shape {}.".format(song_train.shape, song_test.shape)

# Train
x1 = []
x2 = []
for r in song_train:
    x1.append(r[0].strip().lower())
    x2.append(r[1].strip().lower())

vectorizer.fit_transform(np.concatenate((x1, x2), axis=0))

loss = []
# positive samples from file
for s in song_test:
    #print len(map), map
    actual_sim = abs(float(s[2]))
    cos_sim = cosine_sim(s[0].strip().lower(), s[1].strip().lower())
    print "Actual {}, Cosine {}".format(actual_sim, cos_sim)

    loss.append(1 if int(actual_sim*10) - abs(int(cos_sim*10)) == 0 else 0)

print "Accuracy is {}".format(sum(loss)*1./len(loss))
