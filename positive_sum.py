def positive_sum(arr):
	positive_numbers=[]
	for i in arr:
		if i>=0:
			positive_numbers.append(i)
	return sum(positive_numbers)