def word_count(text):
    return len(re.findall(r'\w+', text))

def character_count(book):
    return len(book['characters'])

def data_summary(books):
    print("There are {} books. ".format(len(books)))
    print("Average length of the summary is . ".format(len(books)))

def choose_k(input_list,k):
    n = len(input_list)
    def choose_range(n, k):
        if k == n:
            return [input_list]
        elif k == 0:
            return [[]]
        elif k == 1:
            return [[(i,input_list[i])] for i in xrange(len(input_list))]
        result = []
        for lst in choose_range(n-1, k-1):
            result.extend(lst + [(i,input_list[i])] for i in range(lst[-1][0] + 1, n))
        return result
    res = choose_range(n,k)
    return [[x[1] for x in items] for items in res]

def get_character_pair(lst):
    return choose_k(lst,2)

