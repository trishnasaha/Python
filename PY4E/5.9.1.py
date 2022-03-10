count=0
total=0.0
while True :
    sval = input ("enter a number:")
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print("invalid input")
        continue

    count = count + 1
    total = total + fval

    print(total,count,total/count)