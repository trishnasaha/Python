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
    
    word = words[1]

    d[word] = d.get(word,0) + 1

    
#print(d)

#maxcount = None
#maxword = None

#for word,count in d.items():
    #if maxcount is None or count>maxcount:
     #   maxcount = count
      #  maxword = word
#print(maxword, maxcount)

maxCount = max(d.values())

for word, count in d.items():
    if count == maxCount:
        print(word,count)