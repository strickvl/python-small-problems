def count_sheeps(arrayOfSheeps):
	total_sheep=0
	for i in arrayOfSheeps:
		if i == True:
			total_sheep+=1
	return total_sheep

# an even cleverer solution listed on codewars was:


# def count_sheeps(arrayOfSheeps):
# 	return arrayOfSheeps.count(True)