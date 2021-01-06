# Some examples of the output of this function:
#
# accum("abcd")    # "A-Bb-Ccc-Dddd"
# accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt")    # "C-Ww-Aaa-Tttt"

def accum(s):
	split_text=list(s)
	print split_text
	output_text=[]
	count=0
	for i in split_text:
		print i
		if i.isupper()==False:
			if count==0:
				output_text.append(i.capitalize())
				count=count+1
			else:
				output_text.append((i.capitalize())+(i*(count)))
				count=count+1
		else:
			if count==0:
				output_text.append(i)
				count=count+1
			else:
				output_text.append(i+(i.lower())*count)
				count=count+1
	final_output="-".join(output_text)
	return final_output

accum("ZpglnRxqenU")