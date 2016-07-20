import cPickle as pickle

def get_state_dict():
	city_len_dict = pickle.load(open('city_lendict', 'rb'))

	state_abbrevs = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 
		'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
		'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
		'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
		'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',}

	state_dict = {}
	unstated_list = []

	n_sorted_places = 0
	for place, pdict in city_len_dict.iteritems():
		if place[-2:] in state_abbrevs:
			n_sorted_places += 1
			if state_abbrevs[place[-2:]] not in state_dict:
				state_dict[state_abbrevs[place[-2:]]] = {}
			for pokemon, num in pdict.iteritems():
				if pokemon in state_dict[state_abbrevs[place[-2:]]]:
					state_dict[state_abbrevs[place[-2:]]][pokemon] += num
				else:
					state_dict[state_abbrevs[place[-2:]]][pokemon] = num
		else:
			unstated_list.append(place)

	print str(n_sorted_places) + ' places were successfully associated with states'
	print str(len(unstated_list)) + ' places could not be associated with states'

	return state_dict

state_len_dict = get_state_dict()
pickle.dump(state_len_dict, open('state_len_dict', 'wb'))

