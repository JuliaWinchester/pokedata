import numpy
import matplotlib.pyplot as plt
import cPickle as pickle
from mpl_toolkits.basemap import Basemap
import dict_func

def rel_n(n, n_min, n_max):
	proportion = (float(n) - float(n_min))/(float(n_max) - float(n_min))
	return (47.0*proportion+3.0)

my_map = Basemap(projection='lcc', lat_1=32,lat_2=45,lon_0=-95, 
	resolution='h', area_thresh=1000, 
	llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49)

my_map.drawcoastlines(linewidth=0.25)
my_map.drawcountries(linewidth=0.5)
my_map.drawstates(linewidth=0.5)
my_map.fillcontinents(color = '#bfffa8', lake_color="#1f8edd")
my_map.drawmapboundary(fill_color="#1f8edd")

city_len_dict = pickle.load(open('../data/city_lendict', 'rb'))
city_loc_dict = pickle.load(open('../data/city_loc_dict', 'rb'))
city_sum_dict = dict_func.calc_sum_dict(city_len_dict)

city_loc_list = [(k, v[0], v[1], city_sum_dict[k]) for k, v in city_loc_dict.iteritems()]
city_loc_zip = zip(*city_loc_list)
city_names = city_loc_zip[0]
city_longs = city_loc_zip[1]
city_lats = city_loc_zip[2]
city_sums = city_loc_zip[3]

n_min = min(city_sums)
n_max = max(city_sums)
city_marker_sizes = [rel_n(n, n_min, n_max) for n in city_sums]

for name, lon, lat, siz in zip(city_names, city_longs, city_lats, city_marker_sizes):
	x, y = my_map(lon, lat)
	my_map.plot(x, y, 'ro', markersize=siz)

plt.title('Pokemon tweets from US locations')
#plt.show()
plt.savefig('poketweets.png', dpi=300, frameon=False, format="png", facecolor='white')

