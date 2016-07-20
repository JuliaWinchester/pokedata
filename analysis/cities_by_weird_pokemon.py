import operator
import numpy
import cPickle as pickle
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import matplotlib.image as mpimg
import dict_func

def make_weird_dict(lendict, city_lendict):
	total_n = sum([v for k, v in lendict.iteritems()])
	ratio_dict = {k: float(v)/float(total_n) for k, v in lendict.iteritems()}

	city_weird_dict = {}
	for city, pdict in city_lendict.iteritems():
		city_weird_dict[city] = {}
		pdict_n = sum([v for k, v in pdict.iteritems()])
		for pokemon, n in pdict.iteritems():
			city_weird_dict[city][pokemon] = (float(n) / float(pdict_n)) / ratio_dict[pokemon]
	return city_weird_dict

def top_weird_pokemon_by_city(city, n=10, exclude_pokemon=False):
	sort_list = sorted(city_weird_dict[city].items(), key=operator.itemgetter(1), reverse=True)
	if exclude_pokemon:
		for pokemon in exclude_pokemon:
			sort_list = [p for p in sort_list if not p[0] == pokemon]
	if len(sort_list) == 0:
		return [(None, None)]
	else:
		return sort_list[:n]

city_lendict = pickle.load(open('../data/city_lendict', 'rb'))
lendict = pickle.load(open('../data/lendict', 'rb'))
city_weird_dict = make_weird_dict(lendict, city_lendict)

def place_poke_img(x, y, pokemon, ax):
	# attach pokemon sprite images to bars
	poke_img = mpimg.imread('../fl-abra/'+pokemon+'.png')
	imagebox = OffsetImage(poke_img, zoom=1.50)
	xy= [x, y]

	ab = AnnotationBbox(imagebox, xy, 
		xybox=(1., 1.),
		xycoords='data',
		boxcoords="offset points",
		frameon=False)
	ax.add_artist(ab)

def plot_weird_pokemon_by_city_bar(exclude_pokemon):
	cities = ['Los Angeles, CA', 'Manhattan, NY', 'Houston, TX', 'Chicago, IL',
				'San Antonio, TX', 'San Diego, CA', 'Austin, TX', 
				'San Francisco, CA', 'Brooklyn, NY', 'Queens, NY', 'Seattle, WA',
				'Philadelphia, PA']

	pokemon_by_city = [top_weird_pokemon_by_city(city, 10, exclude_pokemon) for city in cities]

	fig, ax = plt.subplots()
	height = 1.0 # was 1.0

	for city in cities:
		c_i = cities.index(city)
		y = c_i
		rects = []
		rects.append(ax.barh(y, pokemon_by_city[c_i][0][1], height, color='#bfffa8'))
		rect_heights = [pokemon_by_city[c_i][0][1]]
		#label = ax.text(sum(rect_heights), y+0.1, pokemon_by_city[c_i][0][0], ha='right', va='bottom')
		place_poke_img(sum(rect_heights)/2, y+0.5, pokemon_by_city[c_i][0][0], ax)
		for i in range(1, len(pokemon_by_city[c_i])):
			rect = ax.barh(y, pokemon_by_city[c_i][i][1], height, left=sum(rect_heights), color='#bfffa8')
			rects.append(rect)
			rect_heights.append(pokemon_by_city[c_i][i][1])
			img_x = (sum(rect_heights)+sum(rect_heights[:-1]))/2
			place_poke_img(img_x, y+0.5, pokemon_by_city[c_i][i][0], ax)
			#label = ax.text(sum(rect_heights), y+0.1, pokemon_by_city[c_i][i][0], ha='right', va='bottom')
			

	ax.set_xlabel('Weirdness index')
	ax.set_ylabel('Cities')
	ax.set_title('Weirdly popular pokemon by city')
	ax.set_yticks(numpy.arange(len(cities))+0.5)
	ax.set_yticklabels(cities)
	ax.patch.set_facecolor('#1f8edd')
	fig.patch.set_facecolor('white')

	plt.tight_layout()
	#plt.show()
	plt.savefig('cities_by_weird_pokemon.png', dpi=300, frameon=False, format="png", facecolor='white')

plot_weird_pokemon_by_city_bar([])