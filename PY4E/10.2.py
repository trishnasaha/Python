name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d= dict()
t= list()

for line in handle:
    if not line.startswith('From '): continue
        
    line = line.rstrip().split()
    
    word = line[5].split(':')
    
    #print(word)
    
    d[word[0]] = d.get(word[0],0)+ 1
    
    #print(d)

for k, v in sorted(d.items()):
    print(k, v)