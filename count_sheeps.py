def count_sheeps(arrayOfSheeps):
	return sum(1 for i in arrayOfSheeps if i == True)

# an even cleverer solution listed on codewars was:


# def count_sheeps(arrayOfSheeps):
# 	return arrayOfSheeps.count(True)