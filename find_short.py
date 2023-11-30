def find_short(s):
    words=s.split()
    word_lengths = [len(i) for i in words]
    return min(word_lengths)

find_short("hope springs eternal")