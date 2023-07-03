import re
datafile = input("enter afile:")
hand = open(datafile)

lst = list()
sum = 0

for line in hand:
    x= re.findall('[0-9]+', line)
    lst = lst+x

for z in lst:
    sum = sum + int(z)

print(sum)

# comprehension

#import re

#print (sum([ int(z) for z in re.findall('[0-9]+',open("actual_data.txt").read())]))
