import operator
import cPickle as pickle

pdict = pickle.load(open('raw_tweets', 'rb'))
lendict = {}

for pokemon, tweets in pdict.iteritems():
	lendict[pokemon] = len(tweets)

pickle.dump(lendict, open('lendict', 'wb'))