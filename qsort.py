#
#	punkiq130@gmail.com 
#	quicksort

import random

def qsort(qslist):
	

	if (len(qslist) < 2):
		return qslist

	big = []
	small = []

	pivot = random.choice(qslist)

	for x in qslist:
		if x <= pivot: 
			small.append(x)
		elif x > pivot:
			big.append(x)
			
	if(len(big) == 0):
		big.append(pivot)
		small.remove(pivot)

	return qsort(small) + qsort(big) 


def main():

	qslist = [9,1,1,2,3,2,7,3,6,4,5] * 200
	print(qsort(qslist))

if __name__ == "__main__":
	main()

