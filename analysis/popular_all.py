import operator
import numpy
import cPickle as pickle
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import matplotlib.image as mpimg

lendict = pickle.load(open('../data/lendict', 'rb'))

sort_tuples = sorted(lendict.items(), key=operator.itemgetter(1), reverse=True)
unzip_tuples = zip(*sort_tuples)
pokemon_names = unzip_tuples[0][1:51]
pokemon_numbers = unzip_tuples[1][1:51]

img_dict = {}
for name in pokemon_names:
	img_dict[name] = mpimg.imread('../fl-abra/'+name+'.png')

n = len(pokemon_names)
x_ind = numpy.arange(n)
width = 1

fig, ax = plt.subplots()
rects = ax.bar(x_ind, pokemon_numbers, width, color='#bfffa8')
ax.set_ylabel('Tweets')
ax.set_title('Pokemon tweet popularity (excluding pikachu)')
ax.set_xticks(x_ind+0.5)
ax.set_xticklabels(pokemon_names, rotation='vertical', size='x-small', weight='book')
ax.xaxis.set_tick_params(length=0, width=0)
ax.patch.set_facecolor('#1f8edd')
fig.patch.set_facecolor('white')

def place_images(rects):
	# attach pokemon sprite images to the top of bars
	for i, rect in enumerate(rects):
		x = rect.get_x()+rect.get_width()/2.
		y = rect.get_height()
		poke_img = img_dict[pokemon_names[i]]
		imagebox = OffsetImage(poke_img, zoom=1.9)
		xy= [x, y]

		ab = AnnotationBbox(imagebox, xy, 
			xybox=(1., 1.),
			xycoords='data',
			boxcoords="offset points",
			frameon=False)
		ax.add_artist(ab)

place_images(rects)
plt.tight_layout()
#plt.show()
plt.savefig('pokemon_popular_no_pikachu.png', dpi=300, frameon=False, format="png", facecolor='white')


