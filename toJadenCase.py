# capitalises the first letter of every word
def toJadenCase(string):
	split_text=string.split()
	revised_text = [i.capitalize()[0]+i[1:] for i in split_text]
	return " ".join(revised_text)