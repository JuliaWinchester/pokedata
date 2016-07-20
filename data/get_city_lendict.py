import cPickle as pickle

city_dict = pickle.load(open('city_dict', 'rb'))
city_lendict = {}

for city, pdict in city_dict.iteritems():
	city_lendict[city] = {}
	for pokemon, tweets in pdict.iteritems():
		city_lendict[city][pokemon] = len(tweets)

pickle.dump(city_lendict, open('city_lendict', 'wb'))