# capitalises the first letter of every word
def toJadenCase(string):
	split_text=string.split()
	revised_text=[]
	for i in split_text:
		revised_text.append(i.capitalize()[0]+i[1:])
	returned_text=" ".join(revised_text)
	return returned_text