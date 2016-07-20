import numpy
import operator
import matplotlib.pyplot as plt
import cPickle as pickle
from mpl_toolkits.basemap import Basemap
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import matplotlib.image as mpimg
import dict_func

def top_pokemon_by_loc(loc, loc_dict, n=10, exclude_pokemon=False):
	sort_list = sorted(loc_dict[loc].items(), key=operator.itemgetter(1), reverse=True)
	if exclude_pokemon:
		for pokemon in exclude_pokemon:
			sort_list = [p for p in sort_list if not p[0] == pokemon]
	if len(sort_list) == 0:
		return [(None, None)]
	else:
		return sort_list[:n]

def place_poke_img(x, y, pokemon):
	# attach pokemon sprite images to bars
	poke_img = mpimg.imread('../fl-abra/'+pokemon+'.png')
	imagebox = OffsetImage(poke_img, zoom=2)
	xy= [x, y]

	ab = AnnotationBbox(imagebox, xy, 
		xybox=(1., 1.),
		xycoords='data',
		boxcoords="offset points",
		frameon=False)

	return ab

my_map = Basemap(projection='lcc', lat_1=32,lat_2=45,lon_0=-95, 
	resolution='h', area_thresh=1000, 
	llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49)

my_map.drawcoastlines(linewidth=0.25)
my_map.drawcountries(linewidth=0.5)
my_map.drawstates(linewidth=0.5)
my_map.fillcontinents(color = '#bfffa8', lake_color="#1f8edd")
my_map.drawmapboundary(fill_color="#1f8edd")

state_len_dict = pickle.load(open('../data/state_len_dict', 'rb'))
state_loc_dict = pickle.load(open('../data/state_loc_dict', 'rb'))
state_sum_dict = dict_func.calc_sum_dict(state_len_dict)

e_p = ['ivysaur', 'venusaur', 'charmeleon', 
            'charizard', 'wartortle', 'blastoise', 'caterpie',
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

state_loc_list = [(k, v[0], v[1], state_sum_dict[k], top_pokemon_by_loc(k, state_len_dict, 1, e_p)[0][0]) for k, v in state_loc_dict.iteritems()]
state_loc_zip = zip(*state_loc_list)
state_names = state_loc_zip[0]
state_longs = state_loc_zip[1]
state_lats = state_loc_zip[2]
state_sums = state_loc_zip[3]
state_pokemons = state_loc_zip[4]

for lon, lat, n_sum, pokemon in zip(state_longs, state_lats, state_sums, state_pokemons):
	if n_sum > 0 and pokemon != None:
		x, y = my_map(lon, lat)
		ab = place_poke_img(x, y, pokemon)
		my_map._check_ax().add_artist(ab)

plt.title('Most popular starter pokemon for continental U.S. states')

#plt.show()
plt.savefig('starters_by_state.png', dpi=300, frameon=False, format="png", facecolor='white')