import cPickle as pickle

pdict = pickle.load(open('raw_tweets', 'rb'))
city_dict = {}

for pokemon, tweets in pdict.iteritems():
	print 'Sorting ' + pokemon
	for t in tweets:
		print t.place.full_name
		print t.place.full_name.encode('utf-8')
		city = t.place.full_name.encode('utf-8')
		if not city in city_dict:
			city_dict[city] = {}
			city_dict[city][pokemon] = [t]
		else:
			if not pokemon in city_dict[city]:
				city_dict[city][pokemon] = [t]
			else:
				city_dict[city][pokemon].append(t)

pickle.dump(city_dict, open('city_dict', 'wb'))