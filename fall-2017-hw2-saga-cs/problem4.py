import string
def fill_completions(fd):
	c_dic = {}
	punc = ['\'', '.', '?', ':', '"', ';', ',', '`', '<', '>', '-']
	for line in fd:
		line = line.replace('\n','')
		lis = line.split(" ")
		for word in lis:
			for p in punc:	
				word=word.strip(p)
				word = word.lower()
			if len(word)>1 and word.isalpha():
				for i in word:
					key = (word.index(i),i)
					c_dic.setdefault(key, set())
					c_dic[key].add(word)
	return c_dic

def find_completions(prefix, c_dict):
	predictions=[]
	for l in prefix:
		for k in c_dict.keys():
			if prefix.index(l)==k[0] and  l== k[1]:
				predictions.append(c_dict[k])
	if len(predictions)!=0:
		wordlist = set.intersection(*predictions)
		if len(wordlist)!=0:
			for i in wordlist:
				print(i + '\n' )
		else:
			print('No completions' +'\n')
	else:
		print('No completions' +'\n')
	

def main():
	while(1):
		pref = raw_input('Enter prefix: ')
		file = open("ap_docs.txt", 'rt')
		c_dic = fill_completions(file)
		find_completions(pref,c_dic)
if __name__ == '__main__':
	main()