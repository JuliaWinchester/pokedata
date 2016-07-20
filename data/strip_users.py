import cPickle as pickle

pdict = pickle.load(open('raw_tweets', 'rb'))

for pokemon, tweets in pdict.iteritems():
	for i, tweet in enumerate(tweets):
		pdict[pokemon][i].user = None
		pdict[pokemon][i].author = None 

pickle.dump(pdict, open('tweets_no_users', 'wb'))
