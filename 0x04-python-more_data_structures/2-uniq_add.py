def uniq_add(my_list=0):
	'''adds all unique integers in a list'''
	it_set = set(my_list)

	s = 0
	for i in it_set:
		s += i
	return s
