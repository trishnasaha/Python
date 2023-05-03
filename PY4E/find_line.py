fname = input("enter a file name: ")
try:
    fhand = open(fname)
except:
    print("file does not exist", fname)
    quit()
total = 0
count = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
    position = line.find(":")
    num = float(line[position+1:])
    count = count+1
    total = total+num
print("average", total/count)