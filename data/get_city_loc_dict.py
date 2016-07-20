import cPickle as pickle
import numpy

city_dict = pickle.load(open('city_dict', 'rb'))
city_loc_dict = {}

for k, v in city_dict.iteritems():
	coord_set = city_dict[k][v.keys()[0]][0].place.bounding_box.coordinates[0]
	city_loc_dict[k] = numpy.mean(numpy.array(coord_set), axis=0)

# Florida's bounding box centroid is in the ocean, so nice-looking point provided
city_loc_dict['Florida, USA'] = numpy.array([-82.266389, 29.444939]) 

pickle.dump(city_loc_dict, open('city_loc_dict', 'wb')) 

