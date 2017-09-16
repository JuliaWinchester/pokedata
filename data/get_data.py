import cPickle as pickle
import os.path
import time
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def wait15():
	print 'Maximum number of calls reached, waiting 15 minutes'
	time.sleep(900)
	return 0

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

call_i = 0

# pokemon = [ 'dodrio', 'seel',
# 			'grimer', 'muk', 'shellder', 'cloyster', 'gastly', 'haunter',
# 			'gengar', 'onix', 'drowzee', 'hypno', 'krabby', 'kingler',
# 			'voltorb', 'electrode', 'exeggcute', 'exeggutor', 'cubone',
# 			'marowak', 'hitmonlee', 'hitmonchan', 'lickitung', 'koffing',
# 			'weezing', 'rhyhorn', 'rhydon', 'chansey', 'tangela', 'kangaskhan',
# 			'horsea', 'seadra', 'goldeen', 'seaking', 'staryu', 'starmie',
# 			'mr. mime', 'scyther', 'jynx', 'electabuzz', 'magmar', 'pinsir',
# 			'tauros', 'magikarp', 'gyarados', 'lapras', 'ditto', 'eevee', 
# 			'vaporeon', 'jolteon', 'flareon', 'porygon', 'omanyte', 'omastar',
# 			'kabuto', 'kabutops', 'aerodactyl', 'snorlax', 'articuno', 'zapdos',
# 			'moltres', 'dratini', 'dragonair', 'dragonite', 'mewtwo', 'mew']

pokemon = ['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 
            'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie',
            'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey',
            'pidgeotto', 'pidgeot', 'rattata', 'raticate', 'spearow', 'fearow',
            'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew', 'sandslash',
            'nidoran', 'nidorina', 'nidoqueen', 'nidorino', 'nidoking', 
            'clefairy', 'clefable', 'vulpix', 'ninetales', 'jigglypuff',
            'wigglytuff', 'zubat', 'golbat', 'oddish', 'gloom', 'vileplume', 
            'paras', 'parasect', 'venonat', 'venomoth', 'diglett', 'dugtrio',
            'meowth', 'persian', 'psyduck', 'golduck', 'mankey', 'primeape',
            'growlithe', 'arcanine', 'poliwag', 'poliwhirl', 'abra', 'kadabra',
            'alakazam', 'machop', 'machoke', 'machamp', 'bellsprout',
            'weepinbell', 'victreebel', 'tentacool', 'tentacruel', 'geodude', 
            'graveler', 'golem', 'ponyta', 'rapidash', 'slowpoke', 'slowbro',
            'magnemite', 'magneton', "farfetch'd", 'doduo', 'dodrio', 'seel',
            'grimer', 'muk', 'shellder', 'cloyster', 'gastly', 'haunter',
            'gengar', 'onix', 'drowzee', 'hypno', 'krabby', 'kingler',
            'voltorb', 'electrode', 'exeggcute', 'exeggutor', 'cubone',
            'marowak', 'hitmonlee', 'hitmonchan', 'lickitung', 'koffing',
            'weezing', 'rhyhorn', 'rhydon', 'chansey', 'tangela', 'kangaskhan',
            'horsea', 'seadra', 'goldeen', 'seaking', 'staryu', 'starmie',
            'mr. mime', 'scyther', 'jynx', 'electabuzz', 'magmar', 'pinsir',
            'tauros', 'magikarp', 'gyarados', 'lapras', 'ditto', 'eevee', 
            'vaporeon', 'jolteon', 'flareon', 'porygon', 'omanyte', 'omastar',
            'kabuto', 'kabutops', 'aerodactyl', 'snorlax', 'articuno', 'zapdos',
            'moltres', 'dratini', 'dragonair', 'dragonite', 'mewtwo', 'mew']

pdict = {'bulbasaur': [], 'ivysaur': [], 'venusaur': [], 'charmander': [], 'charmeleon': [], 
			'charizard': [], 'squirtle': [], 'wartortle': [], 'blastoise': [], 'caterpie': [],
			'metapod': [], 'butterfree': [], 'weedle': [], 'kakuna': [], 'beedrill': [], 'pidgey': [],
			'pidgeotto': [], 'pidgeot': [], 'rattata': [], 'raticate': [], 'spearow': [], 'fearow': [],
			'ekans': [], 'arbok': [], 'pikachu': [], 'raichu': [], 'sandshrew': [], 'sandslash': [],
			'nidoran': [], 'nidorina': [], 'nidoqueen': [], 'nidorino': [], 'nidoking': [], 
			'clefairy': [], 'clefable': [], 'vulpix': [], 'ninetales': [], 'jigglypuff': [],
			'wigglytuff': [], 'zubat': [], 'golbat': [], 'oddish': [], 'gloom': [], 'vileplume': [], 
			'paras': [], 'parasect': [], 'venonat': [], 'venomoth': [], 'diglett': [], 'dugtrio': [],
			'meowth': [], 'persian': [], 'psyduck': [], 'golduck': [], 'mankey': [], 'primeape': [],
			'growlithe': [], 'arcanine': [], 'poliwag': [], 'poliwhirl': [], 'abra': [], 'kadabra': [],
			'alakazam': [], 'machop': [], 'machoke': [], 'machamp': [], 'bellsprout': [],
			'weepinbell': [], 'victreebel': [], 'tentacool': [], 'tentacruel': [], 'geodude': [], 
			'graveler': [], 'golem': [], 'ponyta': [], 'rapidash': [], 'slowpoke': [], 'slowbro': [],
			'magnemite': [], 'magneton': [], "farfetch'd": [], 'doduo': [], 'dodrio': [], 'seel': [],
			'grimer': [], 'muk': [], 'shellder': [], 'cloyster': [], 'gastly': [], 'haunter': [],
			'gengar': [], 'onix': [], 'drowzee': [], 'hypno': [], 'krabby': [], 'kingler': [],
			'voltorb': [], 'electrode': [], 'exeggcute': [], 'exeggutor': [], 'cubone': [],
			'marowak': [], 'hitmonlee': [], 'hitmonchan': [], 'lickitung': [], 'koffing': [],
			'weezing': [], 'rhyhorn': [], 'rhydon': [], 'chansey': [], 'tangela': [], 'kangaskhan': [],
			'horsea': [], 'seadra': [], 'goldeen': [], 'seaking': [], 'staryu': [], 'starmie': [],
			'mr. mime': [], 'scyther': [], 'jynx': [], 'electabuzz': [], 'magmar': [], 'pinsir': [],
			'tauros': [], 'magikarp': [], 'gyarados': [], 'lapras': [], 'ditto': [], 'eevee': [], 
			'vaporeon': [], 'jolteon': [], 'flareon': [], 'porygon': [], 'omanyte': [], 'omastar': [],
			'kabuto': [], 'kabutops': [], 'aerodactyl': [], 'snorlax': [], 'articuno': [], 'zapdos': [],
			'moltres': [], 'dratini': [], 'dragonair': [], 'dragonite': [], 'mewtwo': [], 'mew': []}

places = api.geo_search(query="USA", granularity="country")
place_id = places[0].id
place_q = 'place:'+place_id

for p in pokemon:
	print 'Searching for tweets containing ' + p
	last_id = 0
	query = p + '%20' + place_q
	while True:
		try:
			print 'Call number: ' + str(call_i)
			if call_i == 170:
				call_i = wait15()
			tweets = api.search(q=query, count=100, max_id=str(last_id - 1))
			call_i += 1
			if not tweets:
				break
			filter_tweets = [t for t in tweets if not hasattr(t, 'retweeted_status') and t.place]
			print 'Appending ' + str(len(filter_tweets)) + ' tweets to pokemon dictionary'
			pdict[p].extend(filter_tweets)
			last_id = tweets[-1].id
		except tweepy.TweepError as e:
			print 'tweepy error'
			print e
			if call_i == 170:
				call_i = wait15()
			call_i += 1
	print 'Finished searching for tweets.'

print "All done"
pickle.dump(pdict, open('raw_tweets_july_24', 'wb'))