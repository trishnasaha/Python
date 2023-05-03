fname = input("enter a file name:")
try:
    fhand = open(fname)
except:
    print("file does not exist", fname)
    quit()

count = 0

for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print(count, "subject line")