fname = input("enter a file name:")
fhand = open(fname)
split_words= dict()
count = 0
for lines in fhand:
    splitted_words = lines.split()
    for words in splitted_words:
        count +=1
        if words in split_words:
            continue
        split_words[words] = count #assigning count as value to key which is "words" here
print(split_words)

if 'Python' in split_words:
    print('True')
else:
    print('False')
