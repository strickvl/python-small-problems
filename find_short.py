def find_short(s):
    words=s.split()
    word_lengths=[]
    for i in words:
    	word_lengths.append(len(i))
    l=min(word_lengths)
    return l

find_short("hope springs eternal")