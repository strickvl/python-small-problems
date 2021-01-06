def get_grade(s1, s2, s3):
    average_grade=(s1+s2+s3)/3
    if average_grade>=90:
    	return "A"
    elif average_grade>=80:
    	return "B"
    elif average_grade>=70:
    	return "C"
    elif average_grade>=60:
    	return "D"
    else:
    	return "F"