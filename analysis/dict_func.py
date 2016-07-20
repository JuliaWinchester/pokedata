def dict_len(d):
	return sum([len(v) for k, v, in d.iteritems()])

def dict_len_2(d):
	return sum([dict_len(v) for k, v in d.iteritems()])

def process_dict(d):
	for k, v in d.iteritems():
		if isinstance(v, list):
			print '    ' + k + ' (list): ' + str(len(v))
		elif isinstance(v, int):
			print '    ' + k + ' (int): ' + str(v)
		elif isinstance(v, dict):
			print k + ' (dict): ' + str(dict_len(v))
			process_dict(v)

def len_summary(d):
	print 'Number of dictionary list entries'
	print '---------------------------------'
	process_dict(d)

def dict_sum(d):
	return sum([v for k, v in d.iteritems()])

def calc_sum_dict(d):
	return {k: dict_sum(v) for k, v in d.iteritems()}
