#8.16.4
fname = input("enter a file name:")
fhand = open(fname)
lst = list()

for line in fhand:
    splitted_words = line.rstrip().split()
    #print(splitted_words)
    for words in splitted_words:
        if words not in lst: 
            lst.append(words)
        else:
            continue
lst.sort()
print (lst)