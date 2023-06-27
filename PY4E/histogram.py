name = input("Enter file:")

try:
    handle = open(name)

except:
    print("the file cannot be opened", name)
    exit()

d = dict()

for line in handle:
    
    if not line.startswith('From '): continue
    
    words = line.rstrip().split()

    #print(words)
    
    word = words[1]

    #print(word)

    d[word] = d.get(word,0) + 1   #retrieve count

    
#print(d)
# oneway of doing
#maxcount = None
#maxword = None

#for word,count in d.items():
    #if maxcount is None or count>maxcount:
     #   maxcount = count
      #  maxword = word
#print(maxword, maxcount)

#anotherway
maxCount = max(d.values())

for word, count in d.items():
    if count == maxCount:
        print(word,count)