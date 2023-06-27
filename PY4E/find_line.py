#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution. 

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
    #print(line)
    position = line.find(":")
    num = float(line[position+1:])
    count = count+1
    total = total+num
print("average", total/count)