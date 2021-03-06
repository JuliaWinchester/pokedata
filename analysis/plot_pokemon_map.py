import numpy
import operator
import matplotlib.pyplot as plt
import cPickle as pickle
from mpl_toolkits.basemap import Basemap
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import matplotlib.image as mpimg
import dict_func

def top_pokemon_by_city(city, n=10, exclude_pokemon=False):
	sort_list = sorted(city_len_dict[city].items(), key=operator.itemgetter(1), reverse=True)
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
	imagebox = OffsetImage(poke_img, zoom=1)
	xy= [x, y]

	ab = AnnotationBbox(imagebox, xy, 
		xybox=(1., 1.),
		xycoords='data',
		boxcoords="offset points",
		frameon=False)

	return ab
	#ax.add_artist(ab)

my_map = Basemap(projection='lcc', lat_1=32,lat_2=45,lon_0=-95, 
	resolution='i', area_thresh=1000, 
	llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49)

my_map.drawcoastlines(linewidth=0.25)
my_map.drawcountries(linewidth=0.5)
my_map.drawstates(linewidth=0.5)
my_map.fillcontinents(color = '#bfffa8', lake_color="#1f8edd")
my_map.drawmapboundary(fill_color="#1f8edd")

city_len_dict = pickle.load(open('../data/city_lendict', 'rb'))
city_loc_dict = pickle.load(open('../data/city_loc_dict', 'rb'))
city_sum_dict = dict_func.calc_sum_dict(city_len_dict)

e_p = ['pikachu', 'squirtle', 'bulbasaur', 'charmander', 'mewtwo', 'mew']

city_loc_list = [(k, v[0], v[1], city_sum_dict[k], top_pokemon_by_city(k, 1, e_p)[0][0]) for k, v in city_loc_dict.iteritems()]
city_loc_zip = zip(*city_loc_list)
city_names = city_loc_zip[0]
city_longs = city_loc_zip[1]
city_lats = city_loc_zip[2]
city_sums = city_loc_zip[3]
city_pokemons = city_loc_zip[4]


n_min = min(city_sums)
n_max = max(city_sums)

for lon, lat, n_sum, pokemon in zip(city_longs, city_lats, city_sums, city_pokemons):
	if n_sum > 25 and pokemon != None:
		x, y = my_map(lon, lat)
		ab = place_poke_img(x, y, pokemon)
		my_map._check_ax().add_artist(ab)

#	x, y = my_map(lon, lat)
#	my_map.plot(x, y, 'ro', markersize=siz)

plt.title('Popular pokemon for continental US locations, >25 poketweets')
#plt.show()
plt.savefig('pokemon_by_locs_25.png', dpi=300, frameon=False, format="png", facecolor='white')

