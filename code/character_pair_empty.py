def write_pair_one_book(book_name_author, character_list):
	size = len(character_list)
	with open('../relationship/{}.csv'.format(book_name_author),'w') as f:
		for i in xrange(size):
			for j in xrange(i+1,size):
				f.write(','.join([character_list[i],character_list[j],'']))
				f.write('\n')



if __name__ == '__main__':
	lst = ['A','B','C','D','E']
	write_pair_one_book('testbook',lst)