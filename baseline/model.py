# Accuracy 0.545\
import sqlite3
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]



conn = sqlite3.connect("data/lastfm_similars.db")
cursor = conn.cursor()

cursor.execute("""select t.lyrics as x1, t2.lyrics as x2, m.similarity 
    from top100_similar_top100 m 
    join songs s on s.track_id = m.tid 
    join top100 t on s.title = t.title and s.year - t.year between -1 and 1  
    join songs s2 on s2.track_id = m.target 
    join top100 t2 on s2.title = t2.title and s2.year - t2.year between -1 and 1 limit 1000;""")
all_data = cursor.fetchall()
print "{} mappings retrieved from DB".format(len(all_data))

loss = []
# positive samples from file
for map in all_data:
    #print len(map), map
    actual_sim = abs(float(map[2]))
    cos_sim = cosine_sim(map[0].lower(), map[1].lower())
    print "Actual {}, Cosine {}".format(actual_sim, cos_sim)

    loss.append(1 if int(actual_sim*10) - abs(int(cos_sim*10)) == 0 else 0)

print "Accuracy is {}".format(sum(loss)*1./len(loss))
