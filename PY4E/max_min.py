largest = None
smallest = None
count = 0
total = 0
while True:
    sval = input("enter a number:")
    if sval == 'done' :
        break
    try:
        fval = float(sval)        
    except:
        print ("invalid")
        continue
    count = count +1
    total = total + fval
    if largest == None and smallest == None :
        largest = sval
        smallest = sval
    elif largest == None or sval > largest :
        largest = sval
    elif smallest == None or sval < smallest :
        smallest = sval

    print (total, count, largest, smallest)

