def sum_of_n(n):
	array=[0]
	if n>0:
		count=0
		while count!=n:
			count=count+1
			array.append((array[count-1]+count))
		return array
	if n<0:
		count=0
		while count!=n:
			count=count-1
			array.append((array[count+1]+count))
		return array
	else:
		return array